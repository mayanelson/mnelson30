'''
TNPG: Unnamed :( (Maya, Jasmine)
SoftDev
K20
2022-11-21
30 mins
'''


from flask import Flask, render_template #import modules
import requests

app = Flask(__name__)    #create Flask object

@app.route("/")
def main():
    key = open(r"key_nasa.txt","r").read()
    api = f"https://api.nasa.gov/planetary/apod?api_key={key}"
    response = requests.get(api)
    data = response.json()
    title = data['title']
    text = data['explanation']
    url = data['url']

    return render_template("main.html",title=title,url=url,text=text)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()'''
