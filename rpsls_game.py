import pygame, random

# Import pygame.locals for easier access to key coordinates
from pygame.locals import *
clock = pygame.time.Clock()

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 710
SCREEN_CENTER =  ( int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2) )
BUTTON_WIDTH = 124
BUTTON_ROW = int(SCREEN_HEIGHT/1.4)
BUTTON_SURF = (150,800)
SPACING = 15

combos = {
	'Rock': {
		'Scissors': 'crushes',
		'Lizard': 'crushes',
		'Sprites': 'rock_sprite.png',
		'Button': 'rock.png'},
	'Paper':{
		'Rock': 'covers',
		'Spock': 'disproves',
		'Sprites': '',
		'Button': 'paper.png'},
	'Scissors':{
		'Paper': 'cuts',
		'Lizard': 'decapitates',
		'Sprites': '',
		'Button': 'scissors.png'},
	 'Lizard':{
		'Paper': 'eats',
		'Spock': 'poisons',
		'Sprites': [
			'lizard_sprite.png',
			'lizard_sprite2.png',
			'lizard_sprite3.png',
			'lizard_sprite4.png',
			'lizard_sprite_death.png',
			'lizard_sprite_death2.png',
			'lizard_sprite_death3.png',
			'lizard_sprite_death4.png',
			'lizard_sprite_death5.png'],
		'Button': 'lizard.png' },
	 'Spock':{
		'Rock': 'vaporizes',
		'Scissors': 'smashes',
		'Sprites': '',
		'Button': 'spock.png'}
	}

history = []




# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
button_screen = pygame.Surface(BUTTON_SURF)




def opp_hand():
	hands = [key for key in combos.keys()]
	return hands[random.randint(0,4)]

def button_click(x, y):
	if (rock_button.left <= x <= rock_button.right and rock_button.top <= y <= rock_button.bottom):
			rock.play()
	elif (paper_button.left <= x <= paper_button.right and paper_button.top <= y <= paper_button.bottom):
			paper.play()
	elif (scissors_button.left <= x <= scissors_button.right and scissors_button.top <= y <= scissors_button.bottom):
			scissors.play()
	elif (lizard_button.left <= x <= lizard_button.right and lizard_button.top <= y <= lizard_button.bottom):
			lizard.play()
	elif (spock_button.left <= x <= spock_button.right and spock_button.top <= y <= spock_button.bottom):
			spock.play()
	elif (op_rock_button.left <= x <= op_rock_button.right and op_rock_button.top <= y <= op_rock_button.bottom):
			rock.play()
	elif (op_paper_button.left <= x <= op_paper_button.right and op_paper_button.top <= y <= op_paper_button.bottom):
			paper.play()
	elif (op_scissors_button.left <= x <= op_scissors_button.right and op_scissors_button.top <= y <= op_scissors_button.bottom):
			scissors.play()
	elif (op_lizard_button.left <= x <= op_lizard_button.right and op_lizard_button.top <= y <= op_lizard_button.bottom):
			lizard.play()
	elif (op_spock_button.left <= x <= op_spock_button.right and op_spock_button.top <= y <= op_spock_button.bottom):
			spock.play()

# Define a RPSLS object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'RPSLS'

class RPSLS(pygame.sprite.Sprite):
	def __init__(self, name):
		super(RPSLS, self).__init__()
		self.name = name

		self.button = combos[self.name]['Button']
		self.button_surf = pygame.image.load(self.button).convert_alpha()
		self.button_flip = pygame.transform.flip(self.button_surf, 1, 0)

		self.button_rect = self.button_surf.get_rect( center=(62,62) )
		self.button_flip_rect = self.button_flip.get_rect( center=(62,62) )

	def play(self):
		op_hand = opp_hand()
		if op_hand in combos[self.name]:
			print(f'{self.name} {combos[self.name][op_hand]} {op_hand}. You win.')
			return history.append((self.name, op_hand, 'Win'))

		elif op_hand == self.name:
			print("It's a tie.")
			return history.append((self.name, op_hand, 'Tie'))

		else:
			print(f'{op_hand} {combos[op_hand][self.name]} {self.name}. You lose.')
			return history.append((self.name, op_hand, 'Loss'))


rock = RPSLS('Rock')
rock.walk = combos[rock.name]['Sprites']

paper = RPSLS('Paper')
paper.walk = combos[paper.name]['Sprites']

scissors = RPSLS('Scissors')
scissors.walk = combos[scissors.name]['Sprites']

lizard = RPSLS('Lizard')
lizard.walk = combos[lizard.name]['Sprites'][:4]
lizard.die = combos[lizard.name]['Sprites'][4:]


spock = RPSLS('Spock')
spock.walk = combos[spock.name]['Sprites']



# Variable to keep the main loop running

running = True

# Main loop

while running:

# Look at every event in the queue

	for event in pygame.event.get():
# Did the user hit a key?

		if event.type == KEYDOWN:
# Was it the Escape key? If so, stop the loop.

			if event.key == K_ESCAPE:
				running = False
# Did the user click the window close button? If so, stop the loop.

		elif event.type == QUIT:
			running = False
# Button mapping

		elif event.type == MOUSEBUTTONDOWN:
			click = pygame.mouse.get_pos()
			button_click(click[0],click[1])

			
			
# Fill the screen with color

	screen.fill((35, 37, 58))
	button_screen.fill( (15, 13, 38) )


# Draw the button on the screen

	screen.blit(button_screen, (0,0) )
	screen.blit(button_screen, (850,0) )

	rock_button = screen.blit(rock.button_flip, (13, 0 + SPACING) )
	op_rock_button = screen.blit(rock.button_surf, (850 + 13, 0 + SPACING) )

	paper_button = screen.blit(paper.button_surf, (13, 124 + 2 * SPACING) )
	op_paper_button = screen.blit(paper.button_flip, (850 + 13, 124 + 2 * SPACING) )

	scissors_button = screen.blit(scissors.button_flip, (13, 248 + 3 * SPACING) )
	op_scissors_button = screen.blit(scissors.button_surf, (850 + 13, 248 + 3 * SPACING) )

	lizard_button = screen.blit(lizard.button_surf, (13, 372 + 4 * SPACING) )
	op_lizard_button = screen.blit(lizard.button_flip, (850 + 13, 372 + 4 * SPACING) )

	spock_button = screen.blit(spock.button_flip, (13, 496 + 5 * SPACING) )
	op_spock_button = screen.blit(spock.button_surf, (850 + 13, 496 + 5 * SPACING) )

# Update the display

	pygame.display.flip()

	clock.tick(60)
