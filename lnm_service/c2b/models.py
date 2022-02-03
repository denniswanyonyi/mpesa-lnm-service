
from django.db import models

class LnmTransaction(models.Model):
   transaction_type = models.TextField(max_length=255)
   transaction_id = models.TextField(max_length=20, unique=True)
   mpesa_transaction_time = models.TextField(max_length=20)
   transaction_amount = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
   business_shortcode = models.TextField(max_length=12)
   bill_refnumber = models.TextField(max_length=128)
   invoice_number = models.TextField(max_length=128, null=True)
   org_account_balance = models.DecimalField(max_digits=19, decimal_places=2, null=True)
   third_party_trans_id = models.TextField(max_length=128, null=True)
   msisdn = models.TextField(max_length=20)
   first_name = models.TextField(max_length=128, null=True)
   middle_name = models.TextField(max_length=128, null=True)
   last_name = models.TextField(max_length=128, null=True)
   date_recorded = models.DateField(auto_now_add=True)
   transaction_status = models.TextField(max_length=30, null=True)
   validation_request_time = models.DateTimeField(null=True)
   confirmation_request_time = models.DateTimeField(null=True)
   validation_request = models.TextField(max_length=3000, null=True)
   confirmation_request = models.TextField(max_length=3000, null=True)