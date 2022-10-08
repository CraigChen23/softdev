# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...") # prints string in terminal while website runs
    print(__name__)   #where will this go? terminal
    return "No hablo queso!" # prints on site

app.run()