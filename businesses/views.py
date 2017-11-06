# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
	context = {
		'title': 'Random Business',


	}
 	return render(request, 'home.html', context)


 def business_list(request):

 	context = {
 	 'object': 'business_list',
 	}
 	return render (request, 'business_list.html', context)




def business_detail(request):
 	context = {


 	}
 	return render (request, "business_detail.html", context)