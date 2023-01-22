import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse


@api_view(['GET'])
def home_send_email(request):
    return render(request, 'send_email.html')


@api_view(['POST'])
def send_mail(request):
    try:
        to_email = request.POST['to_email']
        subject = request.POST['subject']
        message = request.POST['message']
        mail_body = "\nDear : " + str(to_email) + "\n\n" + str(message)
        return base_send_excel_mail(subject, mail_body, to_email)
    except Exception as E:
        print('ERROR SEND MAIL : ',E)
        

def base_send_excel_mail(subject_mail: str, body: str, to_email: str):
    try:
        mail_receiver = {"email_list": [to_email]}
        mail_receiver_list = mail_receiver["email_list"]
        msg = MIMEMultipart()
        msg["Subject"] = subject_mail
        msg["To"] = ", ".join(mail_receiver_list)
        msg.attach(MIMEText(body, "plain"))
        try:
            sender_email = "watsanak@botnoigroup.com"
            msg["From"] = sender_email
            server = smtplib.SMTP_SSL("smtp.zoho.com", 465)
            server.login("watsanak@botnoigroup.com", "Watsana3107")
            server.sendmail(sender_email, mail_receiver_list, msg.as_string())
            server.quit()
        except Exception as e:
            print("error send mail with watsanak-mail", e)

        return JsonResponse({'status': 'success'})
    except Exception as e:
        print("error base_send_excel_mail : ", e)
        return "error base_send_excel_mail"


