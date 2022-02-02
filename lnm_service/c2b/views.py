from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Lower
from django.db.models import CharField
import json

from datetime import datetime

from .models import LnmTransaction

CharField.register_lookup(Lower)

@csrf_exempt
def index(request):

    transactions = LnmTransaction.objects.order_by('-date_recorded')[:100]

    data = {
        'transactions': transactions
    }

    return render(request, "index.html", data)

@csrf_exempt
def details(request, tid):

    transaction = get_object_or_404(LnmTransaction.objects.filter(transaction_id = tid.upper()))

    print(transaction.transaction_id)

    data = {
        'title': tid.upper(),
        'transaction': transaction
    }

    return render(request, "details.html", data)




@csrf_exempt
def c2b_validation(request):

    print("Logging validation request")
    data = json.loads(request.body)

    c2b = LnmTransaction()

    c2b.transaction_type = data["TransactionType"]
    c2b.transaction_id = data["TransID"].upper()
    c2b.mpesa_transaction_time = data["TransTime"]
    c2b.transaction_amount = data["TransAmount"]
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