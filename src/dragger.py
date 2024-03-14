import pygame
from const import *
from piece import Piece
from board import Board

class Dragger:
    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None
        self.dragging  = False
        self.board = Board()

    #other methodds

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # pos => tupple\

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQ_SIZE
        self.initial_col = pos[0] // SQ_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
        self.board.squares[self.initial_row][self.initial_col] = None

    def undrag_piece(self):
        self.piece._setloc()
        self.piece = None
        self.dragging = False

            


    # blit methods

    def update_blit(self, surface):
        # texture chanege => making the dragging gg piece bigger
        self.piece._setloc(size=128)

        location = self.piece.loc
        img = pygame.image.load(location)

        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)

        #blit
        surface.blit(img, self.piece.texture_rect)

        
    


