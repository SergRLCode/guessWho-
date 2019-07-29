from pyknow import *
from pyknow.fact import *
import random as r
from data import dfMen, dfWomen, menQuestions, womenQuestions

class TotalQuestions(Fact):
    total_questions = Field(int, default = 0)

class DefiningQuestion(Fact):
    question = Field(str, mandatory=True)
    attrib = Field(str, mandatory=True)

class Action(Fact):
    pass

class GuessWho(KnowledgeEngine):
    print('Guess who?')
    print("You'll choose YES (y) or NO (n)")

    @DefFacts()
    def defining_questions(self):
        is_woman = input('Tu maestre es mujer? ').upper().startswith('Y')
        self.questions = list()
        if not is_woman:
            print(dfMen)
            self.matrix = dfMen
            r.shuffle(menQuestions)
            for val in menQuestions:
                yield DefiningQuestion(question=val[0], attrib=val[1])
        else:
            print(dfWomen)
            self.matrix = dfWomen
            r.shuffle(womenQuestions)
            for val in womenQuestions:
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
        answer = input('%s ' % self.questions[tq][0]).upper().startswith('Y')
        self.matrix = self.matrix[self.matrix[self.questions[tq][1]].isin([answer])]
        self.modify(nq, total_questions=tq+1)
        print(self.matrix)
        if(len(self.matrix)==1):
            self.declare(Action('guessing-character'))

    @Rule(AS.f1 << Action('next-question'))
    def _human_choice(self, f1):
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
    gw.reset()
    gw.run()
