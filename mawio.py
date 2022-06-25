import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def notify():
    sender_email = "kunonutechnologies@gmail.com"
    receiver_email = "kaiza@kunonu.co.tz"

    port = 465  # For SSL
    # password = input("Type your password and press enter: ")
    password = "cwbxbxmjmbkqgtwe"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           You have a new ticket. 
           <a href="http://127.0.0.1:8000/admin/login/">Please attend the ticket,</a> 
           integrity is our Motto.
           <div id="footer"><div style="text-align: center">
            <p>Crafted with <span style="color:red;">&hearts;</span> from University of Dar es Salaam.</p>
    <p><a href="https://github.com/evsmms/evmms/tree/v0.0.0-alpha">v0.0.0-alpha</a>
        <strong>&copy;2021-
            <script>document.write(new Date().getFullYear().toString());</script>
            <a href="https://evsmms.github.io/evrsms/" title="VRSMS Software">
                VRSMS&#153 Software</a>
        </strong>
    </p>
    <p> Some rights reserved.</p>
            <a href="https://www.djangoproject.com/">
                <img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif"
                     style="border: #003366;" alt="Made with Django." title="Made with Django." />
            </a>
</div>
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
