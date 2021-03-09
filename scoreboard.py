from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.content = file.read()
        self.high_score = int(self.content)
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-40, 350)
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='left', font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as fi:
                fi.write(str(self.score))

        self.score = 0
        self.updatescore()

    # def gameover(self):
    #     self.goto(-50, 0)
    #     self.write('GAME OVER ', align='left', font=("Arial", 20, "normal"))

    def increasescore(self):
        self.score += 1
        self.updatescore()






