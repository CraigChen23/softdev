"""
Craig Chen, Aaron Gershkovich, Kosta Dubovskiy
SoftDev
-Dictionaries and Random- 
2022-09-22
time spent:
DISCO:
    * The key in the dictionary can be anything, and it's useful for categorization of many things
    * Need to import random with lowercase
    * Need to randint needs two arguments
    * randint is inclusive on both ends
QCC:
    * Is there a way to generate a random item from an input list, with a built in random method
OPS SUMMARY:
"""

krewes = {2:["devo1", "devo2", "devo3", "devo4", "devo5"], 7:["devo1", "devo2", "devo3", "devo4", "devo5"], 8:["devo1", "devo2", "devo3", "devo4", "devo5"]}

import random

def get_devo(dictionary):
    randKeyInd = random.randint(0, 2)
    randKey = list(dictionary.keys())[randKeyInd]
    randDevo = random.randint(0, len(dictionary[randKey]) - 1)
    return dictionary[randKey][randDevo]

print(get_devo(krewes))
