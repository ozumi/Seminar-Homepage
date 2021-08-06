from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here
#import ipdb;

def register_form(request):
	if request.method == "POST":
		form = RegisterForm()
#		if form.is_valid():
		register = form.save(commit=False)
		register.name = request.POST.get('name')
		register.email = request.POST.get('email')
		register.phone = request.POST.get('phone')
		register.affiliation = request.POST.get('affiliation')
		register.department = request.POST.get('department')
		register.position = request.POST.get('position')
		register.save()

#		return redirect('register_form')
		return HttpResponseRedirect(reverse("register_list"))
	else:
		form = RegisterForm()

	return render(request, 'myapp/new_index.html', {'form': form})


def register_list(request):
	return render(request, 'myapp/register_list.html', {})

