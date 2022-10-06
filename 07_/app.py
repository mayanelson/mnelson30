'''
ZEMZEM is AWZOME Ziying Jian, Maya Nelson, Elizabeth Paperno
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
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''