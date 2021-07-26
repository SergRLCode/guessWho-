import numpy as np
import pandas as p
from pymongo import MongoClient

mongo = MongoClient()

character = mongo.Expsys.character

def addCharacter(data):
    character.insert_one(data)
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

def genericQuestions(gender):
    char = 'o' if gender == 'M' else 'a'
    return [
        ['Tu docente tiene cabello largo?', 'haveLongHair'],
        ['Tu docente tiene cabello chino?', 'haveCurlyHair'],
        ['Tu docente tiene el cabello de color negro?', 'haveBlackHair'],        
        ['Tu docente usa lentes?', 'useGlasses'],
        ['Tu docente es de piel morena?', 'isNigga'],
        ['Tu docente es alt%s?'%char, 'isTall'],
        ['Tu docente es se ve joven?', 'looksYoung'],
        ['Tu docente es delgad%s?'%char, 'isThin']
    ]

def menQuestions():
    return [
        ['Tu profe tiene vello facial?', 'haveFacialHair']
    ]

def womenQuestions():
    return [
        ['Tu maistra usa maquillaje?', 'useMakeup']
    ]