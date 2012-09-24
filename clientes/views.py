# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import ClienteForm
from clientes.models import Cliente


def list(request):
	clientes = Cliente.objects.all()
	context = RequestContext(request, {'clientes': clientes})
	return render_to_response('cliente/list.html', context)


def create(request):
	form = ClienteForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		return HttpResponseRedirect('/clientes/')

	context = RequestContext(request, {'form': form})
	return render_to_response('cliente/create.html', context)


def delete(request, id):
    cliente = Cliente.objects.get(pk=id)

    if request.method == "POST":
        cliente.delete()
        return HttpResponseRedirect('/clientes/')

    context = RequestContext(request, {'cliente': cliente})
    return render_to_response('cliente/delete.html', context)


def update(request, id):
	cliente = Cliente.objects.get(pk=id)
	
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance=cliente)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/clientes/')

	else:
		form = ClienteForm(instance=cliente)
		
	context = RequestContext(request, {'form': form, 'id': id})
	return render_to_response('cliente/update.html', context)	
