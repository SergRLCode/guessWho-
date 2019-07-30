from Character import Character
from pyknow import *
from pyknow.fact import *
import random as r
from data import *
import re as regex
import os

class TotalQuestions(Fact):
    total_questions = Field(int, default = 0)

class DefiningQuestion(Fact):
    question = Field(str, mandatory=True)
    attrib = Field(str, mandatory=True)

class Action(Fact):
    pass

class GuessWho(KnowledgeEngine):
    @DefFacts()
    def defining_questions(self):
        self.matrix = getMatrix()
        print("You'll choose YES (y) or NO (n)")
        is_woman = input('1.- Tu maestre es mujer? ').upper().startswith('Y')
        self.questions = list()
        if not is_woman:
            self.matrix = self.matrix[self.matrix['isWoman'].isin([False])]
            print(self.matrix)
            questions = menQuestions()
            r.shuffle(questions)
            for val in questions:
                yield DefiningQuestion(question=val[0], attrib=val[1])
        else:
            self.matrix = self.matrix[self.matrix['isWoman'].isin([True])]
            print(self.matrix)
            questions = womenQuestions()
            r.shuffle(questions)
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
        answer = input('%s.- %s ' % (tq+2, self.questions[tq][0])).upper().startswith('Y')
        self.matrix = self.matrix[self.matrix[self.questions[tq][1]].isin([answer])]
        self.modify(nq, total_questions=tq+1)
        print(self.matrix)
        if("vello facial" in self.questions[tq][0] and answer == True):
            self.declare(Action('add-more-questions'))
        if(len(self.matrix)==1):
            self.declare(Action('guessing-character'))

    @Rule(AS.f1 << Action('next-question'))
    def _human_choice(self, f1):
        self.retract(f1)
        self.declare(Action('next-question'))

    @Rule(Action('add-more-questions'),
            AS.f1 << Action('next-question'),
            AS.nq << TotalQuestions(total_questions=MATCH.tq))
    def addMoreQuestions(self, f1, nq, tq):
        self.retract(f1)
        self.questions.insert(tq, ['Tu profe tiene barba?', 'haveBeard'])
        self.questions.insert(tq+1, ['Tu profe tiene bigote?', 'haveMoustache'])

    @Rule(AS.f1 << Action('add-more-questions'))
    def _add_more_questions(self, f1):
        self.retract(f1)
        self.declare(Action('next-question'))

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
            # print(getMatrix())
            gw.reset()
            gw.run()
        elif ans == 2:
            qualities = ['Is woman? ', 'Have long hair? ', 'Have curly hair? ', 'Have gray hair? ', 'Use glasses? ', 'Is nigga? ', 'Is tall? ', 'Is doctor? ']
            nQ = []
            nQ.append(input('Name: '))
            for val in qualities:
                nQ.append(input(val).upper().startswith('Y'))
            if nQ[1] != True:
                if input('Have facial hair? ').upper().startswith('Y'):
                    nQ.append(True)
                    nQ.append(input('Have beard? ').upper().startswith('Y'))
                    nQ.append(input('Have moustache? ').upper().startswith('Y'))
                else:
                    nQ.append(False)
                    nQ.append(False)
                    nQ.append(False)
            else:
                nQ.append(False)
                nQ.append(False)
                nQ.append(False)
            newChar = Character(nQ[0], nQ[1], nQ[2], nQ[3], nQ[4], nQ[5], nQ[6], nQ[7], nQ[8], nQ[9], nQ[10], nQ[11])
            print(addCharacter(newChar.getQualities()))
        else:
            exitGame = False
        input('Press Enter key...')
