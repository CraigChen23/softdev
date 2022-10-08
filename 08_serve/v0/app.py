# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # it creates an instance of class Flask within a directory

@app.route("/") # assign fxn to route
def hello_world():
    print(__name__) # prints name of class in terminal
    return "No hablo queso!"  # prints string on website

app.run()  # runs site
                