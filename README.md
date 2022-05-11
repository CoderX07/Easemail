# Easemail
Easemail is an easy way to send Gmails from an external website.

`No CSS`
`No JS`

`Built purely with a HTML Front-End and a Python Backend`

## Features
- Secure login process
- Does not store data
- Debugged so that only if logged in can you route to `/email`
- Ability to logout and sign-in with a different Gmail
- Checks with Google to see if email address + password is valid
- Actually works 

*Recommended using a spam Gmail Address

#### Note
To use less secure applications* such as this one:
[Google Security](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Nbq5oQ2lday8wQJpXDS3lazD2V33KeEmU5nI66hEnijo-koUomxhUEk1XdCWknNEBESPJkeae75-lVxfBODcJkkADG2A)


## Sample Code For Security Reasons
```python 
import smtplib
server = smtplib.SMTP('smt.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
# ...
server.quit()
```

*Less secure applications are apps that do not require a google key and all the hassle of google authenticated logins which is why using a spam email is recommended
