import pygame
import random

# Import pygame.locals for easier access to key coordinates
from pygame.locals import *
clock = pygame.time.Clock()

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 124
BUTTON_ROW = int(SCREEN_HEIGHT/1.5)
BUTTON_SPACING = 14
BUTTON_CENTER = int( (SCREEN_WIDTH / 2) - (BUTTON_WIDTH / 2) )
BUTTON_SECOND = BUTTON_CENTER - BUTTON_WIDTH - BUTTON_SPACING
BUTTON_FIRST = BUTTON_SECOND - BUTTON_WIDTH - BUTTON_SPACING
BUTTON_FORTH = BUTTON_CENTER + BUTTON_WIDTH + BUTTON_SPACING
BUTTON_FIFTH = BUTTON_FORTH + BUTTON_WIDTH + BUTTON_SPACING

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

def opp_hand():
	hands = [key for key in combos.keys()]
	return hands[random.randint(0,4)]

# Define a RPSLS object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'RPSLS'
class RPSLS(pygame.sprite.Sprite):
	def __init__(self, name):
		super(RPSLS, self).__init__()
		self.name = name
		self.button = combos[self.name]['Button']
		self.button_surf = pygame.image.load(self.button).convert_alpha()
		#self.button_surf.set_colorkey((0,0,0), RLEACCEL)
		self.button_rect = self.button_surf.get_rect( center=(62,62) )

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

		elif event.type == MOUSEBUTTONDOWN:
			click = pygame.mouse.get_pos()
			if click[0] in range(BUTTON_FIRST, BUTTON_FIRST + BUTTON_WIDTH + 1) and click[1] in range(BUTTON_ROW, BUTTON_ROW + BUTTON_WIDTH):
				rock.play()
			elif click[0] in range(BUTTON_SECOND, BUTTON_SECOND + BUTTON_WIDTH + 1) and click[1] in range(BUTTON_ROW, BUTTON_ROW + BUTTON_WIDTH):
				paper.play()
			elif click[0] in range(BUTTON_CENTER, BUTTON_CENTER + BUTTON_WIDTH + 1) and click[1] in range(BUTTON_ROW, BUTTON_ROW + BUTTON_WIDTH):
				scissors.play()
			elif click[0] in range(BUTTON_FORTH, BUTTON_FORTH + BUTTON_WIDTH + 1) and click[1] in range(BUTTON_ROW, BUTTON_ROW + BUTTON_WIDTH):
				lizard.play(), 
			elif click[0] in range(BUTTON_FIFTH, BUTTON_FIFTH + BUTTON_WIDTH + 1) and click[1] in range(BUTTON_ROW, BUTTON_ROW + BUTTON_WIDTH):
				spock.play()

	# Fill the screen with color
	screen.fill((14.9, 13.3, 38.4))

	# Draw the button on the screen
	screen.blit(rock.button_surf, ( BUTTON_FIRST, BUTTON_ROW ) )
	screen.blit(paper.button_surf, ( BUTTON_SECOND, BUTTON_ROW ) )
	screen.blit(scissors.button_surf, ( BUTTON_CENTER, BUTTON_ROW ) )
	screen.blit(lizard.button_surf, ( BUTTON_FORTH, BUTTON_ROW ) )
	screen.blit(spock.button_surf, ( BUTTON_FIFTH, BUTTON_ROW ) )

	# Update the display
	pygame.display.flip()

	clock.tick(60)
