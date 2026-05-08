import pygame as py
import random

#function to turn the pieces
#function to check all of the surounding pieces
#Maybe have the 2d list grow as needed and the pieces auto center?

class Main():
    def __init__(self):
        global TileType, Game_Screen, TileList
        TileType = {"Road" : 0, "River" : 1, "Grass" : 2, "City": 3, "Lake" : 4}
        self.ScreenWidth = 1200; self.ScreenHight = 800
        Game_Screen = py.display.set_mode((self.ScreenWidth, self.ScreenHight))
        self.Running = True
        self.Clock = py.time.Clock()
        self.GameGrid = [[0 for _ in range(20)] for _ in range(20)]
        self.StartPiece = self.Tile(TileType["City"], TileType["Road"], TileType["Grass"], TileType["Road"], py.image.load('Starting Tile.png').convert_alpha())
        self.GameGrid[10][10] = self.StartPiece
        TileList = []
        for i in range(8):
            TileList.append(self.Tile(TileType["Grass"], TileType["Road"], TileType["Road"], TileType["Grass"], py.image.load('Road Turn.png').convert_alpha()))
            TileList.append(self.Tile(TileType["Grass"], TileType["Road"], TileType["Grass"], TileType["Road"], py.image.load('Road Straight.png').convert_alpha()))
            TileList.append(self.Tile(TileType["City"], TileType["Road"], TileType["Grass"], TileType["Road"], py.image.load('Starting Tile.png').convert_alpha()))
            TileList.append(self.Tile(TileType["City"], TileType["Road"], TileType["Road"], TileType["Grass"], py.image.load('C Ro Ro G.png').convert_alpha()))
            TileList.append(self.Tile(TileType["City"], TileType["Grass"], TileType["Grass"], TileType["Grass"], py.image.load('C G G G.png').convert_alpha()))
            TileList.append(self.Tile(TileType["City"], TileType["Grass"], TileType["Road"], TileType["Road"], py.image.load('C G Ro Ro.png').convert_alpha()))
            if i % 2 == 0: # Make four copies
                TileList.append(self.Tile(TileType["City"], TileType["Grass"], TileType["Road"], TileType["Grass"], py.image.load('C G Ro G.png').convert_alpha()))
                TileList.append(self.Tile(TileType["City"], TileType["Road"], TileType["City"], TileType["Road"], py.image.load('Ro C Ro C.png').convert_alpha()))
                TileList.append(self.Tile(TileType["Grass"], TileType["Grass"], TileType["Grass"], TileType["Grass"], py.image.load('Full Grass.png').convert_alpha()))
            elif i % 4 == 0:# Make two copies
                TileList.append(self.Tile(TileType["City"], TileType["City"], TileType["Road"], TileType["City"], py.image.load('C C Ro C.png').convert_alpha()))
                TileList.append(self.Tile(TileType["City"], TileType["City"], TileType["Grass"], TileType["City"], py.image.load('C C G C.png').convert_alpha()))
                TileList.append(self.Tile(TileType["City"], TileType["City"], TileType["City"], TileType["City"], py.image.load('C C C C.png').convert_alpha()))
                TileList.append(self.Tile(TileType["Grass"], TileType["Grass"], TileType["Road"], TileType["Grass"], py.image.load('G G Ro G.png').convert_alpha()))
                TileList.append(self.Tile(TileType["City"], TileType["Road"], TileType["Road"], TileType["Road"], py.image.load('C Ro Ro Ro.png').convert_alpha()))
                TileList.append(self.Tile(TileType["Road"], TileType["Road"], TileType["Road"], TileType["Road"], py.image.load('Ro Ro Ro Ro.png').convert_alpha()))

    def Input(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.Running = False

    def Main(self):
        while self.Running:
            self.Input()

            self.Draw()

    def Draw(self):
        Game_Screen.fill((0, 0, 0))
        for X in range(len(self.GameGrid)):
            for Y in range(len(self.GameGrid)):
                if self.GameGrid[X][Y]:
                    self.StartPiece.Draw(X * 40, Y * 40)
        py.display.flip()

    class Tile:
        def __init__(self, Side1, Side2, Side3, Side4, Img):
            self.Sides = [Side1, Side2, Side3, Side4]
            self.Placed = False
            self.Img = Img
        
        def TurnClockwise(self):
            if not self.Placed:
                self.Sides = [self.Sides[3], self.Sides[0], self.Sides[1], self.Sides[2]]

        def TurnCounterClockwise(self):
            if not self.Placed:
                self.Sides = [self.Sides[1], self.Sides[2], self.Sides[3], self.Sides[0]]
        
        def Draw(self, X_Pos, Y_Pos):
            Game_Screen.blit(self.Img, (X_Pos, Y_Pos))


Game = Main()
Game.Main()
