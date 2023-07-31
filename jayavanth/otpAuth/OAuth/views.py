from email.message import EmailMessage
from django.shortcuts import render
from .models import OAuth
# Create your views here.
def generateOTP():
    import random
    otp=""
    for i in range(5):
        otp+=str(random.randint(0,9))
    otp=int(otp)
    return otp
    
def sendMail(emailId,otp):
    from smtplib import SMTP
    try:
        s=SMTP('smtp.gmail.com',587)
        s.starttls()
        s.ehlo()
        mailid="otpauthenticator220@gmail.com"
        password="ugtaenoevkiksqpf"
        s.login(mailid,password)
        sent_from = mailid
        to = emailId
        msg=EmailMessage()
        msg.set_content(str(otp) + ". OTP is valid for 5 minutes.")
        msg['Subject'] = 'Here is your OTP'
        msg['From'] = sent_from
        msg['To'] = to
        s.send_message(msg)
        s.quit()
        return True
    except Exception as e:
        print(e)
        return False

def otpAuth(request):
    if request.method == "POST":
        print(request.POST)
        emailId=request.POST['emailId']
        otp=generateOTP()
        if(sendMail(emailId,otp)):
            o = OAuth(emailId=emailId, otp=otp)
            o.save()
            print("OTP sent")
            return render(request, 'forms.html', {'status':"Otp sent"})
        else:
            return render(request, 'forms.html', {'status':"Error in sending OTP"})
    return render(request, 'forms.html')

def usersList(request):
    users = OAuth.objects.all()
    return render(request, 'users.html', {'users':users})