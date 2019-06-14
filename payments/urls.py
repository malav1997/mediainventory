from django.conf.urls import url
from django.urls import path

from . import views

from payments.views import ViewAllChannels, PaymentDetails, get_price, generate_receipt

urlpatterns = [
    path('channel/view/all', views.ViewAllChannels.as_view(), name='viewallchannel'),
    url(r'payments/payment_details/(?P<id>\d+)/$', views.PaymentDetails.as_view(), name='paymentdetails'),
    url(r'payments/payment_process/(?P<id>\d+)/$', views.get_price, name='getprice'),
    url(r'payments/receipt_generate/', views.generate_receipt, name='generatereceipt')

]