import numpy as np
import pandas as p


menQuestions = [
    ['Tu profe tiene barba?', 'haveBeard'],
    ['Tu profe tiene bigote?', 'haveMoustache'],
    ['Tu profe tiene canas?', 'haveGreyHair'],
    ['Tu profe usa lentes?', 'useGlasses'],
    ['Tu profe es de piel morena?', 'isNigga'],
    ['Tu profe es alto?', 'isTall'],
    ['Tu profe es doctor?', 'isDoctor']
]

womenQuestions = [
    ['Tu maestra tiene cabello largo?', 'haveLongHair'],
    ['Tu maestra tiene cabello chino?', 'haveCurlyHair'],
    ['Tu maestra es rubia?', 'isBlonde'],
    ['Tu profe usa lentes?', 'useGlasses'],
    ['Tu profe es de piel morena?', 'isNigga'],
    ['Tu profe es alta?', 'isTall']
]

men = p.Series(['Jaime', 'Horacio', 'Hugo', 'Leopoldo', 'Marban', 'Uribe', 'Mata', 'Gil', 'Peraza', 'Omar', 'Chapito', 'Jefe Banda', 'Camacho'])

women = p.Series(['Dalia', 'Anita', 'Lupita', 'Alba', 'Claudia', 'Chi', 'Antonieta', 'Vicky', 'Miss There'])

columnsMen = ['haveBeard', 'haveMoustache', 'haveGreyHair', 'useGlasses', 'isNigga', 'isTall', 'isDoctor']

columnsWomen = ['haveLongHair', 'haveCurlyHair', 'isBlonde', 'useGlasses', 'isNigga', 'isTall']

dataMen = [
    [True, False, False, True, False, True, False],
    [True, False, True, False, True, False, False],
    [True, False, False, False, False, True, False],
    [False, True, False, True, True, True, False],
    [False, True, True, True, True, False, False],
    [False, False, True, False, True, True, False],
    [False, False, True, True, True, True, False],
    [False, False, False, False, False, False, False],
    [False, False, True, False, False, False, True],
    [True, False, True, False, False, True, True],
    [False, True, False, False, False, False, False],
    [False, False, False, False, False, True, False],
    [False, False, True, False, False, False, False],
]

dataWoman = [
    [True, False, False, False, False, False],
    [True, False, False, False, True, False],
    [True, True, True, True, False, True],
    [True, False, False, True, False, True],
    [True, True, False, False, True, False],
    [True, False, False, False, False, True],
    [False, True, True, False, False, False],
    [False, True, False, False, True, False],
    [False, False, False, False, False, False]
]

dfMen = p.DataFrame(dataMen, index=men, columns=columnsMen)

dfWomen = p.DataFrame(dataWoman, index=women, columns=columnsWomen)

# print(dfMen.describe())
# print(dfWomen.describe())


# print(dfMen[dfMen['haveGreyHair'].isin([True])])
