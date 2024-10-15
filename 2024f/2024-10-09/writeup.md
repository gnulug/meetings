# 2024-10-09

### GLUG News

Slides uploaded into the same directory.



### Lightning talk by Leslie

https://github.com/SleepyLeslie/uiuc-auto-passwd 

Using your own hardware security key for UIUC 2FA

- If you add from the NetID center, they will only allow keys that are bought from the University Bookstore.

- Login to UIUC email on the Microsoft web client. After entering your credentials, the Duo prompt should show up.

- Click on "other options" -> "Manage Devices"

- You'll be prompted to verify your identity first. You can use any of the methods that you already have registered with Duo.

- You'll now be redirected to a page that shows your current devices. Click on "Add a device" -> "Security Key" and follow the instructions for inserting and using the security key

- Done!

Duo now supports TOTP (TOTP is used by the [GitHub - SleepyLeslie/uiuc-auto-passwd: Resets your UIUC password efficiently.](https://github.com/SleepyLeslie/uiuc-auto-passwd) project)

- TOTP = Time-based one-time password

- Generates a OTP using the current time and a secret key

- TOTP replaces HOTP, which uses a counter and a secret a key to generate the OTP, this makes it harder to automate, because you have maintain the count across your devices
  
  

### Lightning talk by Sam

About the Python GIL

Why have GIL? How does it slow us down: http://dabeaz.com/python/UnderstandingGIL.pdf

What is hyperthreading: https://en.wikipedia.org/wiki/Hyperthreading

Use different subinterpreter objects on different threads: https://realpython.com/python312-subinterpreters/

Python with optional GIL (biased ref-counts and fine-grained locking): https://peps.python.org/pep-0703/

Biased ref counting (from UIUC prof): https://dl.acm.org/doi/abs/10.1145/3243176.3243195

Async programming in Python, which you can use today: https://realpython.com/python-async-features/
