
import pygame
import random
import button
from pygame import mixer
from fight import Fighter

mixer.init()
pygame.init()

# Définit la taille de la fenêtre
largeur = 1375
hauteur = 700
screen = pygame.display.set_mode((largeur, hauteur))

# Définit le titre de la fenêtre
pygame.display.set_caption("Fatal Fighter")

# On définit l'état du jeu
game_paused = False
game_state = "main"


#############################################################################

clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#jeu variable
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#fighter variable
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#load music et sons
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.75)


#load spritesheets
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

#load vicory image
victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

#define animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#define font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


def draw_bg():
  scaled_bg = pygame.transform.scale(bg_image, (largeur, hauteur))
  screen.blit(scaled_bg, (0, 0))


def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, RED, (x, y, 400, 30))
  pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


fighter_1 = Fighter(1, 300, 410, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Fighter(2, 900, 410, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)


#############################################################################


# Les FPS du jeu
clock = pygame.time.Clock()
FPS = 60

fond = random.randint(0,30)
if fond<10:
    image_fond = pygame.image.load("assets/images/background/menu1.png") #Changer en fonction du dossier ou se trouve l'image
    logo_img = pygame.image.load('assets/images/icons/logo.png').convert_alpha()
    start_img = pygame.image.load('assets/images/icons/start_btn1.png').convert_alpha()
    exit_img = pygame.image.load('assets/images/icons/exit_btn.png').convert_alpha()
    back_img = pygame.image.load('assets/images/icons/back_btn.png').convert_alpha()
    play_img = pygame.image.load('assets/images/icons/play_btn.png').convert_alpha()

elif fond > 20:
    image_fond = pygame.image.load("assets/images/background/menu2.png")
    logo_img = pygame.image.load('assets/images/icons/logo.png').convert_alpha()
    start_img = pygame.image.load('assets/images/icons/start_btn2.png').convert_alpha()
    exit_img = pygame.image.load('assets/images/icons/exit_btn.png').convert_alpha()
    back_img = pygame.image.load('assets/images/icons/back_btn.png').convert_alpha()
    play_img = pygame.image.load('assets/images/icons/play_btn.png').convert_alpha()

else:
    image_fond = pygame.image.load("assets/images/background/menu3.png")
    logo_img = pygame.image.load('assets/images/icons/logo.png').convert_alpha()
    start_img = pygame.image.load('assets/images/icons/start_btn3.png').convert_alpha()
    exit_img = pygame.image.load('assets/images/icons/exit_btn.png').convert_alpha()
    back_img = pygame.image.load('assets/images/icons/back_btn.png').convert_alpha()
    play_img = pygame.image.load('assets/images/icons/play_btn.png').convert_alpha()


# Redimensionner l'image de fond pour qu'elle s'adapte à la taille de la fenêtre
image_fond = pygame.transform.scale(image_fond, (largeur, hauteur))

## MENU PRINCIPAL :

# Afficher l'image de fond
screen.blit(image_fond, (0, 0))

# Définit les boutons

start_button = button.Button(480, 300, start_img, 1)
exit_button = button.Button(580, 575, exit_img, 0.5)
logo_button = button.Button(400, 50, logo_img, 1)
back_button = button.Button(1075, 450, back_img, 0.4)
play_button = button.Button(500, 500, play_img, 0.6)

## CREATION DES MENUS :

    # Creation du menu de selection de personnage
fond_select = pygame.image.load('assets/images/background/fond_select.png').convert_alpha()
fond_select = pygame.transform.scale(fond_select,(largeur,hauteur))
    # Creation du menu de selection
fond_stage = pygame.image.load('assets/images/background/fond_select.png').convert_alpha()
fond_select = pygame.transform.scale(fond_select,(largeur,hauteur))



BLACK = (0,0,0)


## VARIABLE SELECTION PERSONNAGE :

fighter1 = None
fighter2 = None

    #Definition des images de boutons :


selectc1_img = pygame.image.load('assets/images/icons/selectc1.png').convert_alpha()
selectc2_img = pygame.image.load('assets/images/icons/selectc2.png').convert_alpha()
selectc3_img = pygame.image.load('assets/images/icons/selectc3.png').convert_alpha()
selectc4_img = pygame.image.load('assets/images/icons/selectc4.png').convert_alpha()

    #Definition des boutons

p1selectc1_btn = button.Button(300, 250, selectc1_img, 0.5)
p1selectc2_btn = button.Button(450, 250, selectc2_img, 0.5)
p1selectc3_btn = button.Button(600, 250, selectc3_img, 0.5)
p1selectc4_btn = button.Button(750, 250, selectc4_img, 0.5)

p2selectc1_btn = button.Button(300, 450, selectc1_img, 0.5)
p2selectc2_btn = button.Button(450, 450, selectc2_img, 0.5)
p2selectc3_btn = button.Button(600, 450, selectc3_img, 0.5)
p2selectc4_btn = button.Button(750, 450, selectc4_img, 0.5)

## VARIABLE SELECTION PERSONNAGE :

selected_map = None


    #Definition des images de boutons :

alea=random.randint(1,3)
if alea is 1:
    selectm1_source = pygame.image.load('assets/images/background/stage1.1.png').convert_alpha()
if alea is 2:
    selectm1_source = pygame.image.load('assets/images/background/stage1.2.png').convert_alpha()
if alea is 3:
    selectm1_source = pygame.image.load('assets/images/background/stage1.3.png').convert_alpha()
selectm2_img = pygame.image.load('assets/images/background/stage2.png').convert_alpha()
selectm3_img = pygame.image.load('assets/images/background/stage3.png').convert_alpha()

    #Redimensionner

largeur_rectangle = 600
hauteur_rectangle = 400

    # Redimensionner l'image pour s'adapter au rectangle
selectm1_img = pygame.transform.scale(selectm1_source, (largeur_rectangle, hauteur_rectangle))
selectm2_img = pygame.transform.scale(selectm2_img, (largeur_rectangle, hauteur_rectangle))
selectm3_img = pygame.transform.scale(selectm3_img, (largeur_rectangle, hauteur_rectangle))

### secret walter
xp=pygame.image.load('assets/images/background/fond.jpg').convert_alpha()
walter_select = pygame.image.load('assets/images/background/walter_select.png').convert_alpha()
walter1 = pygame.image.load('assets/images/background/walter1.png').convert_alpha()
walter2 = pygame.image.load('assets/images/background/walter2.png').convert_alpha()
walter3 = pygame.image.load('assets/images/background/walter3.png').convert_alpha()
walter4 = pygame.image.load('assets/images/background/walter4.png').convert_alpha()
saul = pygame.image.load('assets/images/background/saul.png').convert_alpha()

    #Definition des boutons

p1selectm1_btn = button.Button(100, 220, selectm1_img, 0.5)
p1selectm2_btn = button.Button(550, 220, selectm2_img, 0.5)
p1selectm3_btn = button.Button(950, 220, selectm3_img, 0.5)


play_pressed = False
key = pygame.key.get_pressed()

run = True
while run:

### IN GAME GAMEPLAY 4K SHADERS LA DINGUERIE

    if play_pressed is True:
          draw_bg()
          draw_health_bar(fighter_1.health, 20, 20)
          draw_health_bar(fighter_2.health, 920, 20)
          draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
          draw_text("P2: " + str(score[1]), score_font, RED, 920, 60)

          #update countdown
          if intro_count <= 0:
            #move fighters
            fighter_1.move(largeur, hauteur, screen, fighter_2, round_over)
            fighter_2.move(largeur, hauteur, screen, fighter_1, round_over)
          else:
            #display count timer
            draw_text(str(intro_count), count_font, RED, largeur / 2, hauteur / 3)
            #update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
              intro_count -= 1
              last_count_update = pygame.time.get_ticks()

          #update fighters
          fighter_1.update()
          fighter_2.update()

          #draw fighters
          fighter_1.draw(screen)
          fighter_2.draw(screen)

          #check for player defeat
          if round_over == False:
            if fighter_1.alive == False:
              score[1] += 1
              round_over = True
              round_over_time = pygame.time.get_ticks()
            elif fighter_2.alive == False:
              score[0] += 1
              round_over = True
              round_over_time = pygame.time.get_ticks()
          else:
            #display victory image
            screen.blit(victory_img, (360, 150))
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
              round_over = False
              intro_count = 3
              fighter_1 = Fighter(1, 00, 410, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
              fighter_2 = Fighter(2, 900, 410, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)


### SELECTION PERSONNAGE MAP ETC ETC ETC ETC

    if game_state is "main":

        if start_button.draw(screen):
            #BOUTON START
            #choose_your_character.play()
            screen.blit(fond_select, (0, 0))
            start_button.hide()
       	    logo_button.hide()
       	    exit_button.rect.x = 1100
            exit_button.rect.y = 575
            game_state = "selection"


        if exit_button.draw(screen):
            #BOUTON QUITTER
            pygame.quit()

        if logo_button.draw(screen):
            pygame.mixer.music.stop()
            pygame.mixer.music.load("assets/audio/saul.mp3")
            pygame.mixer.music.play(-1, 0.0)
            fond_select = pygame.transform.scale(walter_select,(largeur,hauteur))
            fond_select = pygame.transform.scale(walter_select,(largeur,hauteur))
            selectm1_img = pygame.transform.scale(walter1, (largeur_rectangle, hauteur_rectangle))
            selectm2_img = pygame.transform.scale(walter2, (largeur_rectangle, hauteur_rectangle))
            selectm3_img = pygame.transform.scale(walter3, (largeur_rectangle, hauteur_rectangle))
            p1selectm1_btn = button.Button(100, 220, selectm1_img, 0.5)
            p1selectm2_btn = button.Button(550, 220, selectm2_img, 0.5)
            p1selectm3_btn = button.Button(950, 220, selectm3_img, 0.5)

            p1selectc1_btn = button.Button(300, 250, xp, 0.5)
            p1selectc2_btn = button.Button(450, 250, walter1, 0.5)
            p1selectc3_btn = button.Button(600, 250, walter4, 0.5)
            p1selectc4_btn = button.Button(750, 250, walter2, 0.5)

            p2selectc1_btn = button.Button(300, 450, walter3, 0.5)
            p2selectc2_btn = button.Button(450, 450, walter1, 0.5)
            p2selectc3_btn = button.Button(600, 450, xp, 0.5)
            p2selectc4_btn = button.Button(750, 450, walter3, 0.5)
            bg_image = saul


    elif game_state is "selection":
            if exit_button.draw(screen):
            #BOUTON QUITTER
                pygame.quit()
                # PREMIER JOUEUR
            if p1selectc1_btn.draw(screen):
                fighter1 = "C1"
            if p1selectc2_btn.draw(screen):
                fighter1 = "C2"
            if p1selectc3_btn.draw(screen):
                pass
            if p1selectc4_btn.draw(screen):
                pass
                # DEUXIEME JOUEUR
            if p2selectc1_btn.draw(screen):
                fighter2 = "C1"
            if p2selectc2_btn.draw(screen):
                fighter2 = "C2"
            if p2selectc3_btn.draw(screen):
                pass
            if p2selectc4_btn.draw(screen):
                pass


            if fighter1 is not None and fighter2 is not None :
                start_button = button.Button(1050, 250, start_img, 0.8)
                if start_button.draw(screen):
                     screen.blit(fond_select, (0, 0))
                     start_button.hide()
                     p1selectc1_btn.hide()
                     p1selectc2_btn.hide()
                     p1selectc3_btn.hide()
                     p1selectc4_btn.hide()
                     p2selectc1_btn.hide()
                     p2selectc2_btn.hide()
                     p2selectc3_btn.hide()
                     p2selectc4_btn.hide()
                     game_state="stage"


    elif game_state is "stage":

        if exit_button.draw(screen):
            #BOUTON QUITTER
                pygame.quit()
        if p1selectm1_btn.draw(screen):
                selected_map = "M1"
        if p1selectm2_btn.draw(screen):
                selected_map = "M2"
        if p1selectm3_btn.draw(screen):
                selected_map = "M3"

        # Lorsque le bouton "Play" est cliqué
        if play_button.draw(screen):
            if selected_map == "M1":
                bg_image = selectm1_source
            elif selected_map == "M2":
                bg_image = pygame.image.load('assets/images/background/stage2.png').convert_alpha()
            elif selected_map == "M3":
                bg_image = pygame.image.load('assets/images/background/stage3.png').convert_alpha()

            play_button.hide()
            p1selectm1_btn.hide()
            p1selectm2_btn.hide()
            p1selectm3_btn.hide()
            draw_bg()
            play_pressed = True


    	#event handler
    for event in pygame.event.get():
    		#quit game
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()

pygame.quit()