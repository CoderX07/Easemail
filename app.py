from flask import Flask, render_template, request, redirect, url_for
import smtplib

smtp_server = 'smtp.gmail.com'
port = 587
# login = False
# context = ssl.create_default_context()
app = Flask('app', template_folder='templates', static_folder='static')

@app.route('/')
def reroute():
  return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  global sender_email, server
  if request.method == 'POST':
    sender_email = request.form['account']
    password = request.form['password']
    # login = True
    # message = 'Subject: {}\n\n{}'.format(subject, body)
    try:
      server = smtplib.SMTP(smtp_server, port)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(sender_email, password)
    except Exception as e:
      print(e)
    return redirect(url_for('email'))
    # return render_template('index.html', value = login)
  if request.method == 'GET':
    return render_template('index.html')

# def check_login():
#  try:
#    sender_email
#  except NameError as e:
#    print(e)
#    return "return redirect(url_for('login'))"
#  else:
#    return "return render_template('email.html', email=sender_email)"

@app.route('/email', methods=['GET', 'POST'])
def email():
  global sender_email, server
  #if login == False:
   # return redirect(url_for('login'))
  if request.method == 'POST':
    if request.form['log_server'] == 'Logout':
      del sender_email
      server.quit()
      return redirect(url_for('login'))
    subject = request.form['subject']
    body = request.form['body']
    message = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail(sender_email, sender_email, message)
    return render_template('email.html', email=sender_email)
  if request.method == 'GET':
    try:
      sender_email
    except NameError as e:
      print(e)
      return redirect(url_for('login'))
    else:
      return render_template('email.html', email=sender_email)

app.run(host='0.0.0.0', port=8080)