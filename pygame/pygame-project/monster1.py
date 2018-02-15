import pygame

def main():
    width = 500
    height = 500
    monster_dir_x = 5
    monster_dir_y = 5
    gob_dir_x = 500
    gob_dir_y = 500
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/background.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    monster_x = pygame.image.load('images/monster.png').convert_alpha()
    monster_y = pygame.image.load('images/goblin.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_dir_x += 5
        monster_dir_y += 5
        gob_dir_x -= 5
        gob_dir_y -= 5
        # Draw background
        screen.blit(background_image, (0, 0))
        screen.blit(monster_x, (monster_dir_x, monster_dir_y))
        screen.blit(hero, (260, 200))
        #screen.blit(monster_y, (v, w))



        # Game display

        pygame.display.update()
        clock.tick(60)
        if monster_dir_x > 460 and monster_dir_y > 460:
            monster_dir_x = 5
            monster_dir_y = 5

    pygame.quit()

if __name__ == '__main__':
    main()
