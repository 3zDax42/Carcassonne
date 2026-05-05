global TileType
TileType = {"Road" : 0, "River" : 1, "Grass" : 2, "City": 3, "Lake" : 4}
class Tile:
    def __init__(self, Side1, Side2, Side3, Side4):
        self.Sides = [Side1, Side2, Side3, Side4]
        self.Placed = False
        #function to turn the pieces
        #function to check all of the surounding pieces
        #Maybe have the 2d list grow as needed and the pieces auto center?
    
    def TurnClockwise(self):
        if not self.Placed:
            self.Sides = [self.Sides[3], self.Sides[0], self.Sides[1], self.Sides[2]]

    def TurnCounterClockwise(self):
        if not self.Placed:
            self.Sides = [self.Sides[1], self.Sides[2], self.Sides[3], self.Sides[0]]

StartPiece = Tile(TileType["City"], TileType["Road"], TileType["Grass"], TileType["Road"])

TileList = []
for i in range(10):
    TileList.append(Tile())
