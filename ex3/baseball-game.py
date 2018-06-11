# Baseball Game

import random


class BaseballGame:
    def run(self):
        self.myNums = self.randomGuess()
        print("Welcome to Baseball number game.")
        print("To stop the game, enter 000")

        # print("myNums = {}".format(self.myNums))
        while True:
            guess = self.readUserInput()
            if guess == (0, 0, 0):
                print("Bye.")
                break
            score = self.calcScore(self.myNums, guess)
            self.printScore(score)
            if score[0] == 3:
                print("Congratulations. You won!!")
                return

    @staticmethod
    def randomGuess():
        random.seed()
        v1 = random.randrange(1, 9)
        v2 = random.randrange(1, 9)
        while v1 == v2:
            v2 = random.randrange(1, 9)
        v3 = random.randrange(1, 9)
        while v1 == v3 or v2 == v3:
            v3 = random.randrange(1, 9)
        return (v1, v2, v3)

    @staticmethod
    def readUserInput():
        while True:
            str = input('Enter your guess: ').replace(' ', '')
            ret = ()
            try:
                if len(str) < 3:
                    raise ValueError
                ret = (int(str[0]), int(str[1]), int(str[2]))
            except ValueError:
                print('Please enter 3 digit number without zeros.')
                continue
            return ret

    @staticmethod
    def calcScore(ref, guess):
        strike = ball = 0
        for i in range(3):
            val = guess[i]
            index = ref.index(val) if val in ref else -1
            if index == -1:
                continue
            if index == i:
                strike += 1
            else:
                ball += 1
        return (strike, ball)

    @staticmethod
    def printScore(score):
        print("{} strike(s) {} ball(s)".format(score[0], score[1]))


if __name__ == '__main__':
    game = BaseballGame()
    game.run()
