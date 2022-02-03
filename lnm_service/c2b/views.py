from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

import json
import base64
from datetime import datetime

from .models import LnmTransaction

@csrf_exempt
def index(request):

    # print('query is ', q)
    transactions = LnmTransaction.objects.order_by('-date_recorded')[:100]

    data = {
        'transactions': transactions
    }

    return render(request, "index.html", data)

@csrf_exempt
def details(request, tid):

    try:
        transaction = LnmTransaction.objects.filter(transaction_id = tid.upper()).values()[0]

        print('type is ', type(transaction), "validation_request" in transaction)

        if transaction["validation_request"] is not None:
            transaction["validation_request"] = base64.b64decode(transaction["validation_request"].encode('utf-8')).decode('utf-8') 

        if transaction["confirmation_request"] is not None:
            transaction["confirmation_request"] = base64.b64decode(transaction["confirmation_request"].encode('utf-8')).decode('utf-8') 
    
        data = {
            'title': tid.upper(),
            'transaction': transaction
        }

        return render(request, "details.html", data)
    
    except IndexError:

        return render(request, "notfound.html", { 'title': 'Transaction Not Found'})

    # except Exception as ex:
    #     print(ex)

    #     return render(request, "error.html", { 'title': 'An Error Occurred'})




@csrf_exempt
def c2b_validation(request):

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
    c2b.validation_request = base64.b64encode(str(data).encode('utf-8')).decode('utf-8')
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

    data = json.loads(request.body)

    if LnmTransaction.objects.filter(transaction_id = data["TransID"].upper()).exists():

        transaction = LnmTransaction.objects.get(transaction_id = data["TransID"].upper())

        transaction.transaction_status = "Successful"
        transaction.confirmation_request = base64.b64encode(str(data).encode("utf-8")).decode('utf-8')
        transaction.confirmation_request_time = datetime.now()

        transaction.save()
    
    else:
        # If we get here, we know that the transaction doesn't exist on the database table because C2B validation
        # is disabled on M-Pesa for the Business Short Code. As such we need to save the transaction at this point 
        transaction = LnmTransaction()

        transaction.transaction_status = "Successful"
        transaction.confirmation_request = base64.b64encode(str(data).encode("utf-8")).decode('utf-8')
        transaction.confirmation_request_time = datetime.now()
        transaction.transaction_type = data["TransactionType"]
        transaction.transaction_id = data["TransID"].upper()
        transaction.mpesa_transaction_time = data["TransTime"]
        transaction.transaction_amount = data["TransAmount"]
        transaction.business_shortcode = data["BusinessShortCode"]
        transaction.bill_refnumber = data["BillRefNumber"]
        transaction.invoice_number = data["InvoiceNumber"]
        transaction.org_account_balance = data["OrgAccountBalance"]
        transaction.third_party_trans_id = data["ThirdPartyTransID"]
        transaction.msisdn = data["MSISDN"]
        transaction.first_name = data["FirstName"]
        transaction.middle_name = data["MiddleName"]
        transaction.last_name = data["LastName"]

        transaction.save()

    
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