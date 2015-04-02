from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

def contact_form(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject',''):
			errors.append('Enter a subject.')
		if not request.POST.get('message',''):
			errors.append('Enter a message')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid email address')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email', t.nishank1990@gmail.com),
				['1990.nishank.tripathi@gmail.com'],
			)
			return HttpResponseRedirect('contact/thanks')
	return render(request, 'contact_form.html',
		{'errors':errors}) 