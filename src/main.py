import pygame
import sys
from const import *
from game import Game



class main:
    def __init__(self):
        print("initialized main => pygame\n")
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen

        while True:
            #showing screen using game.py -> Game
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():
                """ CLICK EVENTS """
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                # click motion
                if event.type == pygame.MOUSEMOTION:
                    pass
                
                # click up
                if event.type == pygame.MOUSEMOTIONUP:
                    pass

                """ QUIT CHECK """
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # other methods 

            pygame.display.update()

main = main()
main.mainloop()