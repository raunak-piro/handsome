from django.shortcuts import render
from basicapp import forms
def form_name_view(request):
	form = forms.FormName()
	return render (request,'basicapp/form_page.html',{'form':form})
# Create your views here.
