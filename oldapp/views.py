from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
	context = RequestContext(request)
	return render_to_response('oldapp/oldhome.html', {}, context)


def credit_card(request):
	context = RequestContext(request)
	return render_to_response('oldapp/credit_card_form.html', {}, context)