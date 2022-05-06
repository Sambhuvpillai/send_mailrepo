from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from mailapp.forms import StudentForm
# Create your views here.

def stdform(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'learning software'
            message = 'you are successfully registered our company'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, message,settings.EMAIL_HOST_USER, [recipient])
            # send_mail(subject, message, from_email, recipient_list)
            return redirect('/')
    return render(request, 'register.html',{'form':form})
    
