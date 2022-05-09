from flask import Flask, render_template, request, redirect, url_for
import smtplib

smtp_server = 'smtp.gmail.com'
port = 587
# context = ssl.create_default_context()
app = Flask('app', template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    sender_email = request.form['account']
    password = request.form['password']
    subject = request.form['subject']
    body = request.form['body']
    message = 'Subject: {}\n\n{}'.format(subject, body)
    try:
      server = smtplib.SMTP(smtp_server, port)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(sender_email, password)
      server.sendmail(sender_email, sender_email, message)
    except Exception as e:
      print(e)
    finally:
      server.quit()
    return render_template('index.html', value = password)
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/email', methods=['GET', 'POST'])
def email():
  return redirect(url_for('login'))

app.run(host='0.0.0.0', port=8080)