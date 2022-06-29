from ast import Try
from tkinter import E
from dbhelper import DBhelper
from flask import Flask, render_template, request

app= Flask(__name__)
DB= DBhelper()

@app.route("/")
def home():
    try:
        data = DB.getAllInputs()
    except Exception as e:
        print (e)
        data = None
    return render_template("home.html", data=data)


@app.route("/add" methods = ["POST"])
def add():
    try:
        request.form.get("userinput")
        DB.addInput(data)
    except Exception as e:
        print (e)
    return home()


@app.route("/clear")
def clear():
    try:
        DB.clearAll()
    except Exception as e:
        print (e)
    return home    


if __name__ == '__main__':
    app.run(port=5000, debug=True)