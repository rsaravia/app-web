import urllib.request
import tempfile
import shutil
import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/formulario', methods=['POST'])
def attend_formu():
    userid = request.form.get("userid")
    state  = request.form.get("hm")
    userid = int(userid)
    if state =="True":
        state = True
    else:
        state = False

    url = 'https://jsonplaceholder.typicode.com/todos/'
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)

    with open(tmp_file.name, "r") as html:
        data = json.load(html)

    titles = ["userId","id","title","completed"]
    #my_list = [{"userId":1 ,"id":24,"title":"quiero ver","completed":True}]
    my_list = []

    for element in data:
        if (element["completed"] == state) and (element["userId"] == userid):
            my_list.append(element)

    return render_template("tabla.html", titles=titles, my_list=my_list)


if __name__ == '__main__':
    app.run()
