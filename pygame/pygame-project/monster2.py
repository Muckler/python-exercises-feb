import pygame

def main():
    width = 520
    height = 520
    monster_x = 0
    monster_y = 0
    
    monster_dir_x = 5
    monster_dir_y = 5
    change_dir_countdown = 120
    gob_dir_x = 500
    gob_dir_y = 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/background.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    monster = pygame.image.load('images/monster.png').convert_alpha()
    goblin = pygame.image.load('images/goblin.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_x += monster_dir_x
        monster_y += monster_dir_y

        change_dir_countdown -= 1
        # Draw background
        screen.blit(background_image, (0, 0))
        screen.blit(monster, (monster_x, monster_y))
        screen.blit(hero, (260, 200))
        



        # Game display

        pygame.display.update()
        clock.tick(60)
        if monster_x >= (width - 75):
            monster_dir_x = -monster_dir_x
            monster_x = 500 - 75
        if monster_y >= (height - 75):
           monster_dir_y = -monster_dir_y
           monster_y = 500 - 75
        if monster_x <= 0:
            monster_dir_x = -monster_dir_x
            monster_x = 0
        if monster_y <= 0:
            monster_dir_y = -monster_dir_y
            monster_y = 0
    
       
        

    pygame.quit()

if __name__ == '__main__':
    main()
