
from django.db import models

class LnmTransaction(models.Model):
   transaction_type = models.TextField(max_length=255)
   transaction_id = models.TextField(max_length=20)
   mpesa_transaction_time = models.TextField(max_length=20)
   trans_amount = models.IntegerField()
   business_shortcode = models.TextField(max_length=12)
   bill_refnumber = models.TextField(max_length=128)
   invoice_number = models.TextField(max_length=128)
   org_account_balance = models.DecimalField(max_digits=19, decimal_places=2)
   third_party_trans_id = models.TextField(max_length=128)
   msisdn = models.TextField(max_length=20)
   first_name = models.TextField(max_length=128)
   middle_name = models.TextField(max_length=128)
   last_name = models.TextField(max_length=128)
   date_recorded = models.DateField(auto_now_add=True)
   transaction_status = models.TextField(max_length=30)
   validation_request_time = models.DateTimeField(null=True)
   confirmation_request_time = models.DateTimeField(null=True)