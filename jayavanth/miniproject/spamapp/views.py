from spamapp.nb import nb
from .models import spammail
from email.message import EmailMessage
from spamapp.forms import email_form
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
	return HttpResponse("<h1>'Hello World'</h1>")

def spam(request):
    form = email_form()
    if request.method == "POST":
        form = email_form(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email_Body']
            if(nb(email)=='ham'):
                email= email+' is a '+ nb(email) + '  email'
                return render(request,'ham.html',{'Mail':email})
            else:
                email= email+' is a '+ nb(email) + '  email'
                return render(request,'spam.html',{'Mail':email})               
        else:
            return render(request,'email.html',{'status':'failure'})
    else:
        form = email_form() 
        return render(request,'email.html',{'form':form})




