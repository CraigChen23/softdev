# Tic-Tac, Talia Hsia, Ayman Habib, Craig Chen
# SoftDev, Period 2
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask


import csv
import random

occupations = {}

def populate_occupations_with_csv():
    with open('occupations.csv') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader) # [['Job Class', 'Percentage'], ['Management', '6.1'], ...]
        rows = rows[1:-1] # remove first and last row

    for row in rows:
        occupations[row[0]] = float(row[1])

def pick_occupation_with_choices():
    occupation = random.choices(list(occupations.keys()), list(occupations.values()))
    return occupation[0] # random.choices() returns a list

'''
def populate_occupations():
    with open('occupations.csv') as f:
        rows = f.read().split("\n") # ['job class,percentage', 'management,6.1', ...]
        rows = rows[1:-1] # remove first and last row

    for row in rows:
        values = row.split(',')
        occupation = ",".join(values[0:-1])
        weight = float(values[-1])
        occupations[occupation] = weight

def pick_occupation_with_choice():
    weighted_occupations = []
    for occupation in list(occupations.keys()):
        weight = int(occupations[occupation] * 10)
        for _ in range(weight):
            weighted_occupations.append(occupation)

    return random.choice(weighted_occupations)
'''

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ") 
    print(__name__)
    populate_occupations_with_csv()
    occupation = pick_occupation_with_choices()
    new_line = '\n'
    content = f"TNPG: Tic-Tac, Talia Hsia, Ayman Habib, Craig Chen <br> <br> {occupation} <br> <br> From list: {occupations}"
    return(content)
    

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
