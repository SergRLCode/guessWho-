from Character import Character
from pyknow import *
from pyknow.fact import *
import random as r
from data import *
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
            # print(self.matrix)
            questions = genericQuestions('profe')
            questions.extend(menQuestions())
            r.shuffle(questions)
            for val in questions:
                yield DefiningQuestion(question=val[0], attrib=val[1])
        else:
            self.matrix = self.matrix[self.matrix['isWoman'].isin([True])]
            # print(self.matrix)
            questions = genericQuestions('maistra')
            questions.extend(womenQuestions())
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
        self.matrix = self.matrix[self.matrix[self.questions[tq][1]] == answer]
        self.modify(nq, total_questions=tq+1)
        # print(self.matrix)
        if("vello facial" in self.questions[tq][0] and answer == True):
            self.declare(Action('add-more-questions-about-facial-hair'))
        if(len(self.matrix)==1):
            self.declare(Action('guessing-character'))

    @Rule(AS.f1 << Action('next-question'))
    def _human_choice(self, f1):
        self.retract(f1)
        self.declare(Action('next-question'))

    @Rule(Action('add-more-questions-about-facial-hair'),
            AS.f1 << Action('next-question'),
            AS.nq << TotalQuestions(total_questions=MATCH.tq))
    def addMoreQuestions(self, f1, nq, tq):
        self.retract(f1)
        self.questions.insert(tq, ['Tu profe tiene barba?', 'haveBeard'])
        self.questions.insert(tq+1, ['Tu profe tiene bigote?', 'haveMoustache'])

    @Rule(AS.f1 << Action('add-more-questions-about-facial-hair'))
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
            qualities = ['Is woman? ', 'Looks young? ', 'Have long hair? ', 'Have curly hair? ', 'Have flamboyant color hair? ', 'Have gray hair? ', 'Have black hair? ', 'Have brown hair? ', 'Is blonde? ', 'Is redhead? ', 'Use glasses? ', 'Is nigga? ', 'Is tall? ', 'Is thin? ']
            allAnswers = []
            allAnswers.append(input('Name: '))
            for val in qualities:
                allAnswers.append(input(val).upper().startswith('Y'))
            if allAnswers[1] != True:
                if input('Have facial hair? ').upper().startswith('Y'):
                    allAnswers.append(True)
                    allAnswers.append(input('Have beard? ').upper().startswith('Y'))
                    allAnswers.append(input('Have moustache? ').upper().startswith('Y'))
                else:
                    allAnswers.append(False)
                    allAnswers.append(False)
                    allAnswers.append(False)
                allAnswers.append(False)
            else:
                allAnswers.append(False)
                allAnswers.append(False)
                allAnswers.append(False)
                if input('Use makeup? ').upper().startswith('Y'):
                    allAnswers.append(True)                
                else:
                    allAnswers.append(False)
            newChar = Character(allAnswers[0], allAnswers[1], allAnswers[2], allAnswers[3], allAnswers[4], allAnswers[5], allAnswers[6], allAnswers[7], allAnswers[8], allAnswers[9], allAnswers[10], allAnswers[11], allAnswers[12], allAnswers[13], allAnswers[14], allAnswers[15], allAnswers[16], allAnswers[17], allAnswers[18])
            print(addCharacter(newChar.getQualities()))
        else:
            exitGame = False
        input('Press Enter key...')
