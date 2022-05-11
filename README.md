# Easemail
Easemail is an easy way to send Gmails from an external website.

`No CSS`
`No JS`

`Built purely with a HTML Front-End and a Python Backend`


# Features
- Secure login process
- Does not store data
- Debugged so that only if logged in can you route to `/email`
- Ability to logout and sign-in with a different Gmail
- Actually works 

*Recommended using a spam Gmail Address


# Sample Code For Security Reasons
```python 
import smtplib
server = smtplib.SMTP('smt.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
# ...
```
