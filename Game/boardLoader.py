import json
import importlib
import sys
sys.path.append('../Players')
import Buff
from wall import Wall
from player import Player

class defaultTile():
    colour = [255,255,255]

class Board:
    gameBoard = []
    playerMap = None

    def __init__(self, boardName,playerName):
        with open(('../Boards/'+boardName+'.json'),'r') as f:
            data = json.load(f)
            w = data['width']
            h = data['height']
            buffs = data['buffs']
            walls = data['walls']
            rPlayers = data['rPlayers']
            bPlayers = data['bPlayers']
        self.playerList = []
        self.gameBoard = [ [defaultTile() for i in range(w)] for j in range(h)]
        #initialize all buffs
        for i in range(0,len(buffs)):
            if len(buffs[i]) == 6:
                buffs[i] = Buff.Heal(buffs[i][0],buffs[i][1],buffs[i][2],buffs[i][3],buffs[i][4],buffs[i][5])
            elif len(buffs[i]) == 4:
                buffs[i] = Buff.Heal(buffs[i][0],buffs[i][1],buffs[i][2],buffs[i][3])
            else:
                buffs[i] = Buff.Heal(buffs[i][0],buffs[i][1])

        #adding everything to the gameBoard
        for y in range(0,h):
            for x in range(0,w):
                for wall in walls:
                    if wall[0] == x and wall[1] == y:
                        self.gameBoard[y][x] = Wall(wall[0],wall[1])
                        break
                if isinstance(self.gameBoard[y][x],defaultTile):
                    for b in buffs:
                        if b.x == x and b.y == y:
                            self.gameBoard[y][x] = b
                            break

        customPlayerMod = importlib.import_module(playerName)
        #adding all players to the playerMap
        for p in bPlayers:
            self.playerList.append(customPlayerMod.CustomPlayer(p[0],p[1],'blue'))
        for p in rPlayers:
            self.playerList.append(customPlayerMod.CustomPlayer(p[0],p[1],'red'))

        ###testing
        # for v in self.gameBoard:
        #     print(' ')
        #     for r in v:
        #         if isinstance(r,defaultTile):
        #             print(0,end=' ')
        #         elif isinstance(r,Buff.Heal):
        #             print(2,end=' ')
        #         else:
        #             print(1,end=' ')
        #
        # print("\n\n")
        # for p in self.playerMap:
        #     print(p)
