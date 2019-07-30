import numpy as np
import pandas as p
from pymongo import MongoClient

mongo = MongoClient()

character = mongo.Expsys.character

def addCharacter(data):
    character.insert(data)
    return('%s added!' % data['name'])

def getNames():
    names = [char['name'] for char in character.find()]
    return names

def getColums():
    col = []
    for char in character.find():
        for val in char:
            if val != 'name' and val != '_id' and (val not in col):
                col.append(val)
    return col

def matrixData():
    matrix = []
    serie = []
    for char in character.find():
        for val in char:
            if val != 'name' and val != '_id':
                serie.append(char[val])
        matrix.append(serie)
        serie = []
    return matrix

def getMatrix():
    matrix = p.DataFrame(matrixData(), index=getNames(), columns=getColums())
    return matrix

def menQuestions():
    menQuestions = [
        ['Tu profe tiene vello facial?', 'haveFacialHair'],
        ['Tu profe tiene canas?', 'haveGreyHair'],
        ['Tu profe usa lentes?', 'useGlasses'],
        ['Tu profe es de piel morena?', 'isNigga'],
        ['Tu profe es alto?', 'isTall'],
        ['Tu profe es doctor?', 'isDoctor']
    ]
    return menQuestions

def womenQuestions():
    womenQuestions = [
        ['Tu maestra tiene cabello largo?', 'haveLongHair'],
        ['Tu maestra tiene cabello chino?', 'haveCurlyHair'],
        ['Tu maestra es rubia?', 'isBlonde'],
        # ['Tu profe usa lentes?', 'useGlasses'],
        ['Tu profe es de piel morena?', 'isNigga'],
        ['Tu profe es alta?', 'isTall']
    ]
    return womenQuestions

# x = 0.4
# for x in range(0, 10):
#     print('-', end='\r')
#     t.sleep(x)
#     print('\\', end='\r')
#     t.sleep(x)
#     print('|', end='\r')
#     t.sleep(x)
#     print('/', end='\r')
#     t.sleep(x)
