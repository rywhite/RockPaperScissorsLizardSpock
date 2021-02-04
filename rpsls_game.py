import pygame, random, os

# Import pygame.locals for easier access to key coordinates
from pygame.locals import *

# Define constants for the screen width and height
WIN_WD = 350
WIN_HT = 500
WIN_CENT =  ( WIN_WD//2, WIN_HT//2 )
WIN_BLUE = (35, 37, 58)
BUTTON_WD = 62
BUTTON_HT = 62
BUTTON_ROW = WIN_HT - BUTTON_HT - 20
ROCK_POS = (WIN_WD//2 - BUTTON_WD//2 - BUTTON_WD*2 - 12, BUTTON_ROW)
SCISSORS_POS = (WIN_WD//2 - BUTTON_WD//2 - BUTTON_WD - 6, BUTTON_ROW)
PAPER_POS = (WIN_WD//2 - BUTTON_WD//2, BUTTON_ROW)
LIZARD_POS = (WIN_WD//2 - BUTTON_WD//2 + BUTTON_WD + 6, BUTTON_ROW)
SPOCK_POS = (WIN_WD//2 - BUTTON_WD//2 + BUTTON_WD*2 + 12, BUTTON_ROW)



# Dictionary of Characters, Actions, and Images
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

# Initialize pygame
pygame.init()
pygame.font.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
WIN = pygame.display.set_mode((WIN_WD, WIN_HT))
WIN.fill(WIN_BLUE)
clock = pygame.time.Clock()
TEXT_RECT = pygame.Surface((WIN_WD,100))
TEXT_RECT.fill(WIN_BLUE)
base_font = pygame.font.Font(None,25)


# Game functions
def display_buttons(rock,paper,scissors,lizard,spock):
	ROCK_BUTTON = WIN.blit(rock.button_surf, ROCK_POS )
	PAPER_BUTTON = WIN.blit(paper.button_surf, SCISSORS_POS )
	SCISSORS_BUTTON = WIN.blit(scissors.button_surf, PAPER_POS )
	LIZARD_BUTTON = WIN.blit(lizard.button_surf, LIZARD_POS )
	SPOCK_BUTTON = WIN.blit(spock.button_surf, SPOCK_POS )


def random_hand():
	hands = [key for key in combos.keys()]
	return hands[random.randint(0,4)]

def get_result(obj):
	op_hand = random_hand()
	TEXT_RECT.fill(WIN_BLUE)

	if op_hand in combos[obj.name]:
		results = "{} {} {}. You win.".format(obj.name, combos[obj.name][op_hand], op_hand)
		results_surf = base_font.render(results,True,(255,255,255))
		results_size = base_font.size(results)
		return TEXT_RECT.blit(results_surf,( (WIN_WD-results_size[0]) //2  , 0) ) 

	elif op_hand == obj.name:
		results = "It's a tie."
		results_surf = base_font.render(results,True,(255,255,255))
		results_size = base_font.size(results)
		return TEXT_RECT.blit(results_surf,( (WIN_WD-results_size[0]) //2  , 0) )

	else:
		results = "{} {} {}. You lose.".format(op_hand, combos[op_hand][obj.name], obj.name)
		results_surf = base_font.render(results,True,(255,255,255))
		results_size = base_font.size(results)
		return TEXT_RECT.blit(results_surf,( (WIN_WD-results_size[0]) //2  , 0) )



# Define a RPSLS object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'RPSLS'
class RPSLS(pygame.sprite.Sprite):
	def __init__(self, name):
		super(RPSLS, self).__init__()
		
		self.name = name
# Button Images
		self.button_img = pygame.image.load(combos[self.name]['Button']).convert_alpha()
		self.button_surf = pygame.transform.scale(self.button_img,(BUTTON_WD,BUTTON_HT))
		self.button_rect = self.button_surf.get_rect( center = (BUTTON_WD//2, BUTTON_HT//2) )
		self.button_flip = pygame.transform.flip(self.button_surf, 1, 0)
		self.button_flip_rect = self.button_flip.get_rect( center = (BUTTON_WD//2, BUTTON_HT//2) )
# Action Dictionary, self.action['opponents hand'] > action
		self.action = combos[self.name]
		

rock = RPSLS('Rock')
paper = RPSLS('Paper')
scissors = RPSLS('Scissors')
lizard = RPSLS('Lizard')
spock = RPSLS('Spock')



# Variable to keep the main loop running
running = True

# Main loop
while running:
	clock.tick(60)

# Draw the button on the screen
	display_buttons(rock,paper,scissors,lizard,spock)
	WIN.blit(TEXT_RECT,(0,20))

# Look at every event in the queue
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
# Button mapping
		elif event.type == MOUSEBUTTONDOWN:
			click = pygame.mouse.get_pos()
			
			
			if ROCK_POS[0] <= click[0] <= ROCK_POS[0] + BUTTON_WD and ROCK_POS[1] <= click[1] <= ROCK_POS[1] + BUTTON_HT:
				get_result(rock)
			elif SCISSORS_POS[0] <= click[0] <= SCISSORS_POS[0] + BUTTON_WD and SCISSORS_POS[1] <= click[1] <= SCISSORS_POS[1] + BUTTON_HT:
				get_result(paper)
			elif PAPER_POS[0] <= click[0] <= PAPER_POS[0] + BUTTON_WD and PAPER_POS[1] <= click[1] <= PAPER_POS[1] + BUTTON_HT:
				get_result(scissors)
			elif LIZARD_POS[0] <= click[0] <= LIZARD_POS[0] + BUTTON_WD and LIZARD_POS[1] <= click[1] <= LIZARD_POS[1] + BUTTON_HT:
				get_result(lizard)
			elif SPOCK_POS[0] <= click[0] <= SPOCK_POS[0] + BUTTON_WD and SPOCK_POS[1] <= click[1] <= SPOCK_POS[1] + BUTTON_HT:
				get_result(spock)
				
			
	




# Update the display
	pygame.display.flip()

