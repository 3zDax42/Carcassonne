import pygame as py
import random

#function to turn the pieces
#function to check all of the surounding pieces
#Maybe have the 2d list grow as needed and the pieces auto center?

class Main():
    def __init__(self):
        global TileType, Game_Screen, GameGrid, TileList
        TileType = {"Road" : 0, "River" : 1, "Grass" : 2, "City": 3, "Lake" : 4}
        self.ScreenWidth = 1240; self.ScreenHight = 840
        Game_Screen = py.display.set_mode((self.ScreenWidth, self.ScreenHight))
        self.Running = True
        self.Clock = py.time.Clock()
        GameGrid = [[0 for _ in range(20)] for _ in range(20)]
        self.Boarder = py.image.load('Carcassonne Boarder.png').convert_alpha()
        self.StartPiece = self.Tile(TileType["City"], TileType["Road"], TileType["Grass"], TileType["Road"], py.image.load('Starting Tile.png').convert_alpha())
        GameGrid[10][10] = self.StartPiece
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
        self.Players = []
        for i in range(4):
            self.Players.append(self.Player())
        self.PlayerTurn = 0

    def Input(self):
        for Event in py.event.get():
            if Event.type == py.QUIT:
                self.Running = False
            self.Players[self.PlayerTurn].Input(Event)

    def Main(self):
        while self.Running:
            self.Input()

            if self.Players[self.PlayerTurn].Tile == None:
                self.PlayerTurn = (self.PlayerTurn + 1) % 4
                self.Players[self.PlayerTurn].Turn_Start()

            self.Draw()
        py.quit()

    def Draw(self):
        Game_Screen.fill((0, 0, 0))
        py.draw.rect(Game_Screen, (100, 100, 100), (840, 0, 400, 840))
        py.draw.rect(Game_Screen, (200, 200, 200), (1020, 700, 40, 40))
        for X in range(42):
            for Y in range(42):
                if (X== 0 or X == 41) or (Y == 0 or Y == 41):
                    Game_Screen.blit(self.Boarder, (X * 20, Y * 20))
        for X in range(len(GameGrid)):
            for Y in range(len(GameGrid)):
                if GameGrid[X][Y] != 0:
                    GameGrid[X][Y].Draw(X * 40 + 20, Y * 40 + 20)
        self.Players[self.PlayerTurn].Draw()
        py.display.flip()

    class Tile:
        def __init__(self, Side1, Side2, Side3, Side4, Img):
            self.Sides = [Side1, Side2, Side3, Side4] # N, W, S, E
            self.Placed = False
            self.Img = Img
        
        def TurnClockwise(self):
            if not self.Placed:
                self.Sides = [self.Sides[3], self.Sides[0], self.Sides[1], self.Sides[2]]
                self.Img = py.transform.rotate(self.Img, -90)

        def TurnCounterClockwise(self):
            if not self.Placed:
                self.Sides = [self.Sides[1], self.Sides[2], self.Sides[3], self.Sides[0]]
                self.Img = py.transform.rotate(self.Img, 90)
        
        def Draw(self, X_Pos, Y_Pos):
            Game_Screen.blit(self.Img, (X_Pos, Y_Pos))

    class Player:
        def __init__(self):
            self.Mouse_X = 0
            self.Mouse_Y = 0
            self.Mouse_Pos = [self.Mouse_X, self.Mouse_Y]
            self.Shift = None
            self.Points = 0
            self.Turn = False
            self.Tile = None

        def Input(self, Event):
            if self.Turn:
                if Event.type == py.MOUSEMOTION:
                    self.Mouse_X, self.Mouse_Y = py.mouse.get_pos()
                    self.Mouse_Pos = [(self.Mouse_X - 20) // 40, (self.Mouse_Y - 20) // 40]
                if Event.type == py.MOUSEBUTTONDOWN:
                    if self.Mouse_Pos[0] < 20 and self.Mouse_Pos[1] < 20:
                        self.Place_Tile()
                if Event.type == py.KEYDOWN:
                    if Event.key == py.K_LSHIFT:
                        self.Shift = True
                    if Event.key == py.K_r:
                        if self.Shift == True:
                            self.Tile.TurnCounterClockwise()
                        else:
                            self.Tile.TurnClockwise()
                if Event.type == py.KEYUP:
                    if Event.key == py.K_LSHIFT:
                        self.Shift = False
            else: return

        def Place_Tile(self):
            if GameGrid[self.Mouse_Pos[0]][self.Mouse_Pos[1]] == 0:
                self.Tile.Placed = True
                GameGrid[self.Mouse_Pos[0]][self.Mouse_Pos[1]] = self.Tile
                self.Turn = False
                self.Tile = None

        def Turn_Start(self):
            self.Tile = random.choice(TileList)
            for _ in range(len(TileList)):
                if TileList[_] == self.Tile:
                    TileList.pop(_)
                    break
            self.Turn = True
        
        def Draw(self):
            if self.Turn:
                self.Tile.Draw(1020, 700)
        
Game = Main()
Game.Main()
