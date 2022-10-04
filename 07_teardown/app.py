'''
ZIMZIM is AWZOME Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K07 -- Flask
2022-10-03
time spent: 
''' 

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
* Flask builds on similar object-oriented programming fundamentals as Java and Python
* Name the file with the same name as the Flask variable
* The hello_world() function is defined but never called. However, we receive the output in the console and the message in the
webpage - maybe this means hello_world() is called within the app.run() invocation.
* Changing the string in @app.route causes the provided webpage to lead to an unfound URL. So it appears that this @app.route line
indicates where the web page lives and how to properly get there. We think that it's probably a good idea to leave the string unchanged as a preset so as not to interfere with the webpage.

QCC:
0.Similar to initializing an instance of a class, learned in Java 
1.Based on using terminal commands in class, we have used this backslash when
constructing file paths 
2.In the previous line, a file path to the app was denoted. This will also be
where __name__ will be printed -- in that file in the file path. 
3.It will not print anything, because __name__ does not have a stored value
4.The print statement will appear wherever the file path leads to when we call app.run()
5.Similar to the way you would call any method, such as main() 
...
INVESTIGATIVE APPROACH:
* First, we didn't modify the code at all, and we just made comparisons to Java and answered the provided questions.
* Without changing the content of the given code, we ran the file for the first time, and we immediately received a ModuleNotFoundError:
"No module named 'flask'"
* We replaced __name__ with a string ("bob"), since we assumed __name__ was a placeholder.
* We SSHed into a lab computer and ran the app.py file from there -- we did not receive the ModuleNotFoundError, but we were unable to
open the provided webpage on our own machine, since it was the address on the lab machine.
* We realized Flask might be a package that is necessary for Thonny to install. We went to Tools --> Manage packages... --> Flask -->Install
* The next time we ran, we didn't receive the ModuleNotFoundError. We received:
     Serving Flask app 'bob'
     Debug mode: off
     WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    bob
    127.0.0.1 - - [03/Oct/2022 20:56:37] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [03/Oct/2022 20:56:38] "GET /favicon.ico HTTP/1.1" 404 -
* When we visited the http://127.0.0.1:5000 page, we saw "No hablo queso!" on the page.
* We tried modifying the "/" on line 13. We changed it to "/testing," and we didn't receive any errors in the console, but when we opened the webapge, we received a URL Not Found message. We changed back to "/"
'''
