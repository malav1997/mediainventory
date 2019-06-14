from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings

import stripe

from users.models import UserProfile
from channels.models import Channel, Program, Slot
from payments.models import Payment


class ViewAllChannels(ListView):

	template_name= 'payments/view_allchannels.html'

	def get_queryset(self):
		queryset = Channel.objects.all()
		return queryset


class PaymentDetails(ListView):

	template_name= 'payments/payment_details.html'

	def get_queryset(self, **kwargs):
		pk = self.kwargs['id']
		queryset = Slot.objects.filter(id=pk)
		return queryset


def get_price(request, id):
	if request.method == 'POST':
		amount = request.POST.get('price', '')
		amount = amount.split('.')[0]
		slot = request.POST.get('slot', '')
		key=settings.STRIPE_PUBLISHABLE_KEY
		print(key)
		print(amount)
		print(slot)
		if '.' in amount:
			amount_temp = amount.split('.')[1]
			amount_count = len(amount_temp)
			amount_zero = ''
			for k in range(0,amount_count):
				if amount_zero == '':
					amount_zero = '0'
				else:
					amount_zero = amount_zero +'0'
					amount_main = amount.replace('.','') + '.' + amount_zero
		else:
			amount_main = amount + '00'
	context= {'key': key, 'amount': amount, 'amount_main': amount_main, 'slot': slot }
	return render(request, 'payments/payment_process.html', context)


def generate_receipt(request):

	stripe.api_key = settings.STRIPE_SECRET_KEY

	if request.method == 'POST':
		amount_main = request.POST.get('amount_main', '')
		amount = request.POST.get('amount', '')
		user = request.POST.get('user', '')
		slot = request.POST.get('slot', '')
		print(user)
		print(slot)
		print(amount)
		if '.' in amount:
			amount_send = amount.replace('.','')
		else:
			amount_send = amount_main
		
		customer = stripe.Customer.create(
			email=request.POST.get('stripeEmail', ''),
			source=request.POST.get('stripeToken', '')
			)

		charge = stripe.Charge.create(
			customer=customer.id,
			amount=int(amount_send),
			currency='usd',
			description='Slot'
			)
		
		payment_id = charge.id
		
		print(payment_id)
		
		Payment.objects.create(payment_id=payment_id, user_id=user, slot_id=slot )
		Slot.objects.filter(pk=slot).update(status='sold')


		
	receipt_url = charge['receipt_url']
	receipt= {'amount': amount, 'receipt_url': receipt_url,}
	return render(request, 'payments/charge.html', receipt)