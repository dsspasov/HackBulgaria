from questions import Question
from player import Player
from connection import *
import random


class Game:

    def __init__(self):
        Base.metadata.create_all(engine)

    def setQuestions(self):
        self.addQuestions("What is the answer to 8+1", 9)
        self.addQuestions(
            "What is the answer to square root (sqrt) of 169?", 13)
        self.addQuestions("What is the answer to (5*5)", 25)
        self.addQuestions("What is the answer to 1024/1024", 2)
        self.addQuestions("What is the answer to 2^10", 1024)
        self.addQuestions("What is the answer to 2^3 + 2", 10)
        self.addQuestions("What is the answer to -9*-5", 45)
        self.addQuestions("What is the answer to lg(10)", 1)

    def printText(self):
        print("Welcome to Do You Even Math")
        print("Your task is to give a correct answer!")
        print("You have 2 options:")
        print("-start      ---> to start the game")
        print("-highscores ---> to see the Top10 highscores")

    def addQuestions(self, questions, answers):
        session.add(Question(question=questions, answer=answers))
        session.commit()

    def chooseName(self):
        player = input("Enter your nickname> ")
        session.add(Player(name=player))
        session.commit()
        return player

    def addScore(self, name, score):
        player = session.query(Player).filter(Player.name == name).one()
        player.score = score
        session.commit()

    def askQuestion(self):
        random_id = random.randint(1, 8)
        question_to_ask = session.query(Question).filter(
            Question.id == random_id).one()
        return question_to_ask

    def input(self):
        answer = input("?>")
        return answer

    def isCorrect(self, correct_answer):
        if correct_answer == int(self.input()):
            return True
        return False

    def start(self):
        name = self.chooseName()
        answer = True
        score = -1
        while(answer):
            score += 1
            asked_question = self.askQuestion()
            print(asked_question.question)
            answer = self.isCorrect(asked_question.answer)
        score = score * score
        #print(score)
        self.addScore(name, score)

    def highscores(self):
        highscore = session.query(Player.name, Player.score).order_by(Player.score.desc()).limit(10)
        for player in highscore:
            print(player[0])
            print("----")
            print(player[1])

    def play(self):
        self.setQuestions()
        self.printText()
        while(True):
            option = self.input()
            if option == 'start':
                self.start()
            elif option == 'highscores':
                self.highscores()
            elif option == 'exit':
                break
            else:
                print("choose normal commad")


def main():
    x = Game()
    x.play()

if __name__ == '__main__':
    main()
