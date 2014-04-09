# Create your views here.
# from app.templates import render_jinja
from portfolio.models import Project

from pprint import pprint
# from app import helpers
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext


def home(request):
	data={}
	# data['uris']=helpers.getURI(request.path)
	data['seo_title'] = "Our Portfolio - Clients and Projects"
	data['highlights'] = Project.objects.filter(use_in=2)
	data['other']= Project.objects.filter(use_in=1)
	return render_to_response("portfolio/base_portfolio.html",data, context_instance=RequestContext(request))
	# return render_jinja(request, 'portfolio/base_portfolio.html', uris=uris, highlights=highlights, other=other, seo_title=seo_title)


def single(request, portfolio_id):
	data={}
	# data['uris']=helpers.getURI(request.path)
	p = Project.objects.get(id=portfolio_id)
	p.lrg = Image.objects.filter(project=p.id).filter(size=610)
	data['p']=p
	data['seo_title'] = p.name + " :: Our Portfolio - Clients and Projects"
	data['did'] = helpers.nl2br(p.what_we_did)
	#send_mail('Subject here 01', 'Here is the message.', 'from@example.com', ['petar@mgpepe.com'], fail_silently=False)
	return render_to_response("portfolio/single.html",data, context_instance=RequestContext(request))
	# return render_jinja(request, 'portfolio/single.html',uris=uris, p=p, did=did, seo_title=seo_title)

