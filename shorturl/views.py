from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Shortner
from .forms import CreateShortenerForm

def home_view(request):
    template='urlshortner/home.html'
    context={}
    context['form']=CreateShortenerForm()
    if request.method=='GET':
        return render(request,template,context)
    elif request.method=='POST':
        used_form=CreateShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object=used_form.save()
            new_url=request.build_absolute_uri('/')+shortened_object.short_url
            long_url=shortened_object.long_url
            context['new_url']=new_url
            context['long_url']=long_url
            context['short_code']=shortened_object.short_url
            return render(request,template,context)
        context['errors']=used_form.errors
        return render (request,template,context)

def redirect_url_view(request,shorten_part):
    if shorten_part == 'admin':
        return admin.site.urls

    try:
        shortner=Shortner.objects.get(short_url=shorten_part)    
        shortner.times_followed+=1
        shortner.save()
        return HttpResponseRedirect(shortner.long_url)
    
    except Shortner.DoesNotExist:
        raise Http404('Sorry ,This link is broken')
        