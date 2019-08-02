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
    genericQuestions = [
        ['Tu %s tiene cabello largo?'%gender, 'haveLongHair'],
        ['Tu %s tiene cabello chino?'%gender, 'haveCurlyHair'],
        ['Tu %s tiene el cabello de color negro?'%gender, 'haveBlackHair'],        
        ['Tu %s usa lentes?'%gender, 'useGlasses'],
        ['Tu %s es de piel morena?'%gender, 'isNigga'],
        ['Tu %s es alt%s?'%(gender, 'o' if gender=='profe' else 'a'), 'isTall'],
        ['Tu %s es se ve joven?'%gender, 'looksYoung'],
        ['Tu %s es delgad%s?'%(gender, 'o' if gender=='profe' else 'a'), 'isThin']
    ]
    return genericQuestions

def menQuestions():
    menQuestions = [
        ['Tu profe tiene vello facial?', 'haveFacialHair']
    ]
    return menQuestions

def womenQuestions():
    womenQuestions = [
        ['Tu maistra usa maquillaje?', 'useMakeup']
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

# print(deleteQuestion(genericQuestions('profe'), colsOneAttrib(getMatrix())))

# deleteQuestion(self.questions, colsOneAttrib(self.matrix))