import pygame
from const import *
from board import Board
from dragger import Dragger


class Game:
    def __init__ (self):
        self.Board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col)%2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (110, 154, 80)
                
                rect = (col*SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                #
                # cannot understand why d i need to revert the order
                #
                if self.Board.squares[col][row].has_piece():

                    # blit all pieces accept dragger
                    piece = self.Board.squares[col][row].piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.loc)
                        img_center = row * SQ_SIZE + SQ_SIZE // 2, col * SQ_SIZE + SQ_SIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)