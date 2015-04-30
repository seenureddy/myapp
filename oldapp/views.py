from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import braintree


def home(request):
    context = RequestContext(request)
    return render_to_response('oldapp/oldhome.html', {}, context)


def credit_card(request):
    context = RequestContext(request)
    return render_to_response('oldapp/credit_card_form.html', {}, context)


@csrf_exempt
def client_token(request):
    a_customer_id = 1
    token =braintree.ClientToken.generate({
      "customer_id": a_customer_id
    })
    return HttpResponse("ClientToken : %s" % (token)) 


@csrf_exempt
def purchase(request):
    nonce = request.POST.get("payment_method_nonce")
    result = braintree.Transaction.sale({
        "amount": "10.00",
        "payment_method_token": str(nonce)
    })
    return HttpResponse(" payment_method_nonce, result : %s %s" % (nonce, result))