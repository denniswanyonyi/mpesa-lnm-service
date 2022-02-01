from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from datetime import datetime

from .models import LnmTransaction

@csrf_exempt
def c2b_validation(request):

    print("Logging validation request")
    data = json.loads(request.body)

    c2b = LnmTransaction()

    c2b.transaction_type = data["TransactionType"]
    c2b.transaction_id = data["TransID"]
    c2b.mpesa_transaction_time = data["TransTime"]
    c2b.trans_amount = data["TransAmount"]
    c2b.business_shortcode = data["BusinessShortCode"]
    c2b.bill_refnumber = data["BillRefNumber"]
    c2b.invoice_number = data["InvoiceNumber"]
    c2b.org_account_balance = data["OrgAccountBalance"]
    c2b.third_party_trans_id = data["ThirdPartyTransID"]
    c2b.msisdn = data["MSISDN"]
    c2b.first_name = data["FirstName"]
    c2b.middle_name = data["MiddleName"]
    c2b.last_name = data["LastName"]
    # c2b.transaction_status = data[""]
    c2b.validation_request_time = datetime.now()

    # print(c2b)

    c2b.save()

    response = {
        "ResultCode": 0,
        "ResultDesc": "Request accepted successfully"
    }

    return JsonResponse(response)

@csrf_exempt
def c2b_confirmation(request):
    
    response = {
        "ResultCode": 0,
        "ResultDesc": "Request accepted successfully"
    }

    return JsonResponse(response)

@csrf_exempt
def c2b_status_query(request):

    response = {
        "ResultCode": 0,
        "ResultDesc": "Request accepted successfully"
    }

    return JsonResponse(response)