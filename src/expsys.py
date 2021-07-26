from Character import Character
from experta import *
from tkinter import *
from PIL import Image, ImageTk
from experta.fact import *
import random as r
from data import *
import os

selectedAnswerFromUser = bool()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        samuel = Image.open("hawk3.jpg")
        render = ImageTk.PhotoImage(samuel)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

def openForm():
    form = Tk()
    form.title("Add teacher")
    frame = Frame(master=form, width=800, height=600)

    propierties = ["Name: ", "Is woman?", "Looks young?", "Have long hair?", "Have curly hair?", "Have flamboyant color hair?", "Have gray hair?", "Have black hair?", "Have brown hair?", "Is blonde?", "Is redhead?", "Use glasses?", "Is nigga?", "Is tall?", "Is thin?", "Have facial hair?", "Have beard?", "Have moustache?", "Use makeup?"]
            
    Label(master=form, text='Yes = y, No = n').grid(column=1)
    
    entriesList = list()

    for index in range(0, len(propierties)):
        Label(master=form, text=propierties[index]).grid(row=index+1)
        entriesList.append(Entry(master=form))
        entriesList[index].grid(row=index+1, column=1)

    def getData():
        newChar = Character(entriesList[0].get(),
            entriesList[1].get().upper().startswith('Y'), entriesList[2].get().upper().startswith('Y'),
            entriesList[3].get().upper().startswith('Y'), entriesList[4].get().upper().startswith('Y'),
            entriesList[5].get().upper().startswith('Y'), entriesList[6].get().upper().startswith('Y'),
            entriesList[7].get().upper().startswith('Y'), entriesList[8].get().upper().startswith('Y'),
            entriesList[9].get().upper().startswith('Y'), entriesList[10].get().upper().startswith('Y'),
            entriesList[11].get().upper().startswith('Y'), entriesList[12].get().upper().startswith('Y'),
            entriesList[13].get().upper().startswith('Y'), entriesList[14].get().upper().startswith('Y'),
            entriesList[15].get().upper().startswith('Y'), entriesList[16].get().upper().startswith('Y'),
            entriesList[17].get().upper().startswith('Y'), entriesList[18].get().upper().startswith('Y')
        )
        print(addCharacter(newChar.getQualities()))
        form.destroy()
        
    Button(master=form, text='Add!', command=getData).grid(row=20, column=0)            
    
    form.mainloop()

class TotalQuestions(Fact):
    total_questions = Field(int, default = 0)

class DefiningQuestion(Fact):
    question = Field(str, mandatory=True)
    attrib = Field(str, mandatory=True)

class Action(Fact):
    pass

class GuessWho(KnowledgeEngine):
    
    @DefFacts()
    def defining_questions(self, is_woman):
        self.matrix = getMatrix()
        # print(self.matrix.index)
        self.questions = list()
        self.hairColorQuestions = [
            ['¿Tu docente tiene el cabello de color extravagante?', 'haveFlamboyantColorHair'],
            ['¿Tu docente tiene el cabello de color rubio?', 'isBlonde'],
            ['¿Tu docente tiene el cabello de color pelirrojo?', 'isRedhead'],
            ['¿Tu docente tiene canas?', 'haveGreyHair'],
            ['¿Tu docente tiene el cabello de color cafe?', 'haveBrownHair']
        ]
        if not is_woman:
            self.matrix = self.matrix[self.matrix['isWoman'].isin([False])]
            questions = genericQuestions('M')
            questions.extend(menQuestions())
            r.shuffle(questions)
            print(self.matrix.index)
            for val in questions:
                yield DefiningQuestion(question=val[0], attrib=val[1])
        else:
            self.matrix = self.matrix[self.matrix['isWoman'].isin([True])]
            questions = genericQuestions('F')
            questions.extend(womenQuestions())
            r.shuffle(questions)
            print(self.matrix.index)
            for val in questions:
                yield DefiningQuestion(question=val[0], attrib=val[1])

    @Rule(NOT(Action()), DefiningQuestion(question=MATCH.question, attrib=MATCH.attrib))
    def definingQuestions(self, question, attrib):
        self.questions.append([question, attrib])

    @Rule()
    def initGame(self):
        self.declare(TotalQuestions(total_questions=0))
        self.declare(Action('next-question'))

    @Rule(Action('next-question'),
            AS.nq << TotalQuestions(total_questions=MATCH.tq))
    def human_choice(self, nq, tq):
        answer = bool(input('%s.- %s ' % (tq+2, self.questions[tq][0])))
        self.matrix = self.matrix[self.matrix[self.questions[tq][1]] == answer]
        # print(self.matrix.index)
        self.modify(nq, total_questions=tq+1)
        
        if (("canas" in self.questions[tq][0] or "color" in self.questions[tq][0]) and answer == False):
            self.declare(Action('add-hair-color-questions'))
        
        if "vello facial" in self.questions[tq][0] and answer == True:
            self.declare(Action('add-more-questions-about-facial-hair'))
        
        if len(self.matrix) == 1:
            self.declare(Action('guessing-character'))
        
        elif len(self.matrix) == 0:
            self.declare(Action('failed'))

    @Rule(AS.f1 << Action('next-question'))
    def _human_choice(self, f1):
        self.retract(f1)
        self.declare(Action('next-question'))

    @Rule(Action('add-hair-color-questions'),
            AS.f1 << Action('next-question'),
            AS.nq << TotalQuestions(total_questions=MATCH.tq))
    def add_questions(self, f1, nq, tq):
        self.retract(f1)
        selected = r.randint(0, len(self.hairColorQuestions)-1)
        self.questions.insert(tq, self.hairColorQuestions[selected])
        del self.hairColorQuestions[selected]

    @Rule(AS.f1 << Action('add-hair-color-questions'))
    def _add_questions(self, f1):
        self.retract(f1)
        self.declare(Action('next-question'))

    @Rule(Action('add-more-questions-about-facial-hair'),
            AS.f1 << Action('next-question'),
            AS.nq << TotalQuestions(total_questions=MATCH.tq))
    def addMoreQuestions(self, f1, nq, tq):
        self.retract(f1)
        self.questions.insert(tq, ['¿Tu docente tiene barba?', 'haveBeard'])
        self.questions.insert(tq+1, ['¿Tu docente tiene bigote?', 'haveMoustache'])

    @Rule(AS.f1 << Action('add-more-questions-about-facial-hair'))
    def _add_more_questions(self, f1):
        self.retract(f1)
        self.declare(Action('next-question'))

    @Rule(Action('failed'),
            AS.f1 << Action('next-question'))
    def machine_failed(self, f1):
        self.retract(f1)
        print("Error 404, character not found :c")
        confirm = input('Os gustaria agregar a ese personaje a mi base de datos? ').upper().startswith('Y')
        if confirm:
            openForm()            
        self.halt()

    @Rule(Action('guessing-character'), 
            AS.f1 << Action('next-question'),
            AS.nq << TotalQuestions(total_questions=MATCH.tq))
    def guessing_character(self, f1, nq, tq):
        self.retract(f1)
        print('En %s preguntas puedo adivinar que tu personaje es %s ' % (tq+1, self.matrix.index[0]))
        self.halt()

if __name__ == '__main__':
    gw = GuessWho()
    exitGame = True
    while exitGame != False:
        os.system('clear')
        print('Guess who?')
        main_message = """
        1.- Play game
        2.- Add character
        .- exit()
        """
        print(main_message)
        ans = int(input('Select an option: '))
        if ans == 1:
            gw.reset()
            gw.run()
        elif ans == 2:
            openForm()
        else:
            exitGame = False
        input('Press Enter key...')
