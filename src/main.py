import pygame
import sys
from const import *
from board import Board
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
        dragger = self.game.dragger
        board = self.game.Board

        while True:
            #showing screen using game.py -> Game
            game.show_bg(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                """ CLICK EVENTS """
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    # print(event.pos)

                    clicked_row = dragger.mouseY // SQ_SIZE
                    clicked_col = dragger.mouseX // SQ_SIZE

                    # print(clicked_row, dragger.mouseY)
                    # print(clicked_col, dragger.mouseX)
                    
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)


                # click motion
                if event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                    

                
                # click up
                if event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                """ QUIT CHECK """
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # other methods 

            pygame.display.update()

main = main()
main.mainloop()