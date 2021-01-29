import random

combos = {'Rock': {'Scissors': 'crushes', 'Lizard': 'crushes'},
                 'Paper':{'Rock': 'covers','Spock': 'disproves'},
                 'Scissors': {'Paper': 'cuts', 'Lizard': 'decapitates'},
                 'Lizard': {'Paper': 'eats', 'Spock': 'poisons'},
                 'Spock': {'Rock': 'vaporizes', 'Scissors': 'smashes'}}
                 
hands = {1: 'Rock', 2: 'Paper', 3: 'Scissors', 4: 'Lizard', 5: 'Spock'}

history = []


class RPSLS:
    
    def throw(self):
        return hands[random.randrange(1,6)]

    def get_result(self):
        op_throw = self.throw()
        
        if op_throw in combos[self.name]:
            print(f'{self.name} {combos[self.name][op_throw]} {op_throw}. You win.')
            return history.append((self.name, op_throw, 'win'))
            
        elif op_throw == self.name:
            print("It's a tie.")
            return history.append((self.name, op_throw, 'tie'))
            
        else:
            print(f'{op_throw} {combos[op_throw][self.name]} {self.name}. You lose.')
            return history.append((self.name, op_throw, 'loss'))


class Rock(RPSLS):
    def __init__(self):
        self.name = 'Rock'


class Paper(RPSLS):
    def __init__(self):
        self.name = 'Paper'


class Scissors(RPSLS):
    def __init__(self):
        self.name = 'Scissors'


class Lizard(RPSLS):
    def __init__(self):
        self.name = 'Lizard'


class Spock(RPSLS):
    def __init__(self):
        self.name = 'Spock'


rock = Rock()
paper = Paper()
scissors = Scissors()
lizard = Lizard()
spock = Spock()
