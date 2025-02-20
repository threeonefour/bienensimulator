# date: 03.02.2025
# filename: bienensimulator.py
# author: Philipp Burger
# version: 0.4
# An attempt to create a simple simulation of a beehive next to field of flowers.
# Flowers are randomly created and bees fly out to find them and collect nectar. Flowers 
# will expire when all nectar is drained, then new flowers will grow.

import random
import time
import os
clear = lambda: os.system('clear') #terminal - clear befehl spezifisch für linux, windows und mac systeme haben verschiedene andere verfahren

xstock = 52
ystock = 17

class Biene:
    nektar = None
    alter = None
    xpos = None
    ypos = None
    richtung = None
    flapFlag = None
    drin = None
    goHome = None
    saugFlag = None
    move = None
    ladung = None
    wait = None

    def __init__(self):
        self.nektar = 0
        self.alter = 0
        self.xpos = xstock
        self.ypos = ystock
        self.richtung = 1
        self.flapFlag = 1
        self.drin = 0
        self.saugFlag = 1
        self.goHome = 0
        self.move = 1
        self.ladung = 0
        self.wait = 0

    def bienenMove(self):

        richtung = self.richtung # richtung ist hier ein wert der zwischen 1 und 8 liegt, und die Bewegungsrichtugn der Biene vorgibt. Sei die Position der Biene in einem Raster, so entsprechen 1-8 dne umliegenden 8 kästchen um die Biene, mit 1 auf 3 uhr, und danahc aufteigend im Uhrzeigersinn.
        x = self.xpos
        y = self.ypos

        move = random.randrange(1, 26)

        if x == 98 and y != 34 and y != 0:
            richtung = 5
        elif x == 1 and y != 34 and y != 0:
            richtung = 1
        elif y == 0 and x != 1 and x != 98:
            richtung = 3
        elif y == 34 and x != 1 and x != 98:
            richtung = 6
        elif x == 1 and y == 0:
            richtung = 2
        elif x == 98 and y ==0:
            richtung = 4
        elif x == 98 and y == 34:
            richtung = 6
        elif x == 1 and y == 34:
            richtung = 8
        else:  # zufällige bestimmung der richtung in einem 180 grad bereich vor der biene,
               #mit hohem gewicht auf vorwärts, mittlerem gewicht auf diagonal links und rechts,
               #und geringem gewicht auf links oder rechts
             if move <= 2:
                 richtung -=2
             elif move <= 5 and move  >= 3:
                 richtung -= 1
             elif move <= 21 and move >= 6:
                 richtung = richtung
             elif move <= 24 and move >= 22:
                 richtung += 1
             else: 
                 richtung += 2

             if richtung > 8:
                 richtung = richtung - 8
             elif richtung <= 0:
                 richtung = richtung + 8
        
        if richtung == 1:
             x += 1
        elif richtung == 2:
             x += 1
             y += 1
        elif richtung == 3:
             y += 1
        elif richtung == 4:
             x -= 1
             y += 1
        elif richtung == 5:
             x -= 1
        elif richtung == 6:
             x -= 1
             y -= 1
        elif richtung == 7:
             y -= 1
        else: 
             x += 1
             y -= 1
    
        self.xpos = x
        self.ypos = y
        self.richtung = richtung

    def flapflap(self, flapFlag): # noch nicht verwendet, evtl. obsolet, flapFlag wird derzeit im gridComposer verwaltet
        if flapFlag < 1:
            flapFlag = 1
        else:
            flapFlag = 0

    def nektarSaugen(self, blume):   #nektar der blume auf null setzen, marker für rückkehr zum bienenstock wird gesetzt
         self.nektar = blume.nektar
         blume.nektarAbgabe()
         blume.welkFlag = 11
         self.goHome = 1
         self.ladung = 1
         self.wait = 10

    def nektarAbgabe(self): # biene wartet zehn zyklen im bienenstock, ladung wird gelöscht, wabe wird erzeugt
        self.ladung = 0
        self.drin = 1
        self.wait  = 10
        self.goHome = 2
        waben.append(Wabe())



    def feierabend(self):#wegfindung zum bienenstock, abhängig vom gegenwärtigen setor der biene
        if self.xpos > 52:
            if self.ypos < 17:
                self.richtung = 4
            elif self.ypos == 17:
                self.richtung = 5
            else:
                self.richtung = 6

        elif self.xpos < 52:
            if self.ypos < 17:
                self.richtung = 2
            elif self.ypos == 17:
                self.richtung = 1
            else:
                self.richtung = 8

        else:
            if self.ypos < 17:
                self.richtung = 3
            else:
                self.richtung = 7

        if self.richtung == 1:
             self.xpos += 1
        elif self.richtung == 2:
             self.xpos += 1
             self.ypos += 1
        elif self.richtung == 3:
             self.ypos += 1
        elif self.richtung == 4:
             self.xpos -= 1
             self.ypos += 1
        elif self.richtung == 5:
             self.xpos -= 1
        elif self.richtung == 6:
             self.xpos -= 1
             self.ypos -= 1
        elif self.richtung == 7:
             self.ypos -= 1
        else: 
             self.xpos += 1
             self.ypos -= 1
   # def blumeSuchen(self): #geplant, bienen sollen in einem gewissen radius blumen "riechen" können.

    
class Blume:
    nektar = None
    bluete = None
    welkFlag = None
    kompostFlag = None
    retireFlag = None
    xpos = None
    ypos = None
    besetzt = None
    
    def __init__(self):

     
         self.nektar = 8
         self.bluete = 45
         self.welkFlag = 500
         self.kompostFlag = 60
         self.retireFlag = 0
         self.besetzt = 0
         self.xpos = random.randrange(1, 98)
         self.ypos = random.randrange(0, 33)
     
    def nektarAbgabe(self):
         self.nektar = 0
         self.welkFlag = 0

class Wabe:
    honig = None
    nektar = None
    reifegrad = None
    reifeFlag = None

    def __init_(self, vorhonig):
        nektar = 500
        honig = 0
        reifegrad = 0
        reifeFlag = 0
        

    def reifen(self): #momentan werde nnur unendlich waben erzeugt, später sollen diese neue bienen wachsen lassen
        nektar -= 1
        honig += 1
        if nektar == 0: 
            reifeFlag = 1


def drawWiese(theGrid, numberOfTheBees, waben, globalTick, blumenLaden, bienenKader): #funktion löcht das terminal und gibt das grid aus. zusätzlich werden einige statusinformationen angegeben, dazu noc heinige werte zur fehlersuche
    
    clear()
    for i in range(len(theGrid)):
        print(*theGrid[i], sep='') 
    globalTick = int(globalTick) 
    
    print("\n")
    print(f"Aktive Bienen: {numberOfTheBees}, Gefüllte Waben: {len(waben)}, Vergangene Zeit: {globalTick}")
    print(f"Blume expire: {blumenLaden[3].welkFlag} {blumenLaden[3].kompostFlag} Biene pos: x {bienenKader[0].xpos} y {bienenKader[0].ypos} home: {bienenKader[0].goHome} {bienenKader[0].wait} {bienenKader[0].drin} {bienenKader[0].ladung} {bienenKader[0].flapFlag}")

def startup(): # erzeugen aller benötigten listen, festlegen der startbienen
        
    print("Willkommen im Bienensimulator!")
    while True:
        try:        
            startBienen = int(input("Bitte die Anzahl der Startbienen eingeben: "))
            if startBienen <= 0:
                print("Anzahl der Startbienen muss größer Null sein!")
                continue


            break
        except(ValueError, IndexError, TypeError):
            print("Bitte eine positive, ganze Zahl eingeben!")
    print("Generiere Wiese, bitte warten!")
    for i in range(20):
        print(".", end="", flush=True)
    print("\n")
    print("BSS")

    theGrid = []
    for j in range(35):
        theGrid.append([])
        for k in range(100):
            theGrid[j].append(" ")

    bienenKader = []
    waben = []
    for h in range(startBienen):
        bienenKader.append(Biene())

    blumenLaden = []   #aktuell fixer wert für die blumen, geplant ist ein dynamisches system dass blumen- und bienenpopulation balanciert
    for i in range(70):
        blumenLaden.append(Blume())

    print("BSSSS")
    time.sleep(1)
    print("BSSSSSSSSSSS")
    time.sleep(1)
    print("Etwas regt sich im Bienenstock...")
    time.sleep(2)
    
    return theGrid, bienenKader, blumenLaden, waben  

def gridComposer(theGrid, blumenLaden, bienenKader): # hier werden auf basis der vorherig bestimmten positions- und Statusdaten der bienen und blumen die entsprechenden visualisierungen im Grid erzeugt

    theGrid = []
    for j in range(35):
        theGrid.append([])
        for k in range(100):
            theGrid[j].append(" ")

    theGrid[15][50:55] = ['#','#','#','#','#']
    theGrid[16][50] = '#'
    theGrid[16][54] = '#'
    theGrid[17][50:55] = ['#','#','#','#','#']
    theGrid[18][50] = '#'
    theGrid[18][54] = '#'
    theGrid[19][50:55] = ['#','#','#','#','#']

    
    for i in range(len(blumenLaden)):
        x = blumenLaden[i].xpos
        y = blumenLaden[i].ypos
        if blumenLaden[i].welkFlag == 0 and blumenLaden[i].kompostFlag > 0:
            theGrid[y][x] = "o"
            theGrid[y+1][x-1] = "^"
            theGrid[y+1][x+1] = "^"
            theGrid[y+1][x] = "|"
            blumenLaden[i].kompostFlag -= 1
        elif blumenLaden[i].kompostFlag == 0 and blumenLaden[i].welkFlag == 0:
            theGrid[y][x] = " "
            theGrid[y+1][x-1] = " "
            theGrid[y+1][x+1] = " "
            theGrid[y+1][x] = " "
            blumenLaden[i].retireFlag = 1
        else:
            theGrid[y][x] = "@"
            theGrid[y+1][x] = "|"
            theGrid[y+1][x-1] = "\\"
            theGrid[y+1][x+1] = "/"
            blumenLaden[i].welkFlag -= 1
       
    for j in range(len(bienenKader)):
        x = bienenKader[j].xpos    
        y = bienenKader[j].ypos
        flapFlag = bienenKader[j].flapFlag
        saugFlag = bienenKader[j].saugFlag

        if bienenKader[j].drin == 1:
            theGrid[y][x] = "#"
            theGrid[y][x-1] = "#"
            theGrid[y][x+1] = "#"
            continue

        if flapFlag == 1:
            theGrid[y][x] = "o"
            theGrid[y][x-1] = "<"
            theGrid[y][x+1] = ">"
            flapFlag = 0
            if bienenKader[j].ladung == 1:
                   theGrid[y][x] = "O"

        elif flapFlag == 0:
            theGrid[y][x] = "o"
            theGrid[y][x-1] = "-"
            theGrid[y][x+1] = "-"
            flapFlag = 1
            if bienenKader[j].ladung == 1:
                   theGrid[y][x] = "O"
        else:
                if saugFlag == 1:
                    theGrid[y][x] = "O"
                    theGrid[y][x-1] = "("
                    theGrid[y][x+1] = ")"
                    saugFlag = 0
                else:
                    theGrid[y][x] = "o"
                    theGrid[y][x-1] = "("
                    theGrid[y][x+1] = ")"
                    saugFlag = 1
               
              
                



        bienenKader[j].flapFlag = flapFlag
        bienenKader[j].saugFlag = saugFlag

    return theGrid, blumenLaden, bienenKader

def main(theGrid, bienenKader, blumenLaden, waben):
    globalTick = 0
    while True:
        numberOfTheBees = len(bienenKader)
        for j in range(len(blumenLaden)):
           if blumenLaden[j].retireFlag == 1:
             blumenLaden[j] = Blume()

        for i in range(len(bienenKader)):
            if bienenKader[i].goHome == 1:
                if bienenKader[i].wait != 0:
                    bienenKader[i].flapFlag = 3
                    bienenKader[i].wait -= 1
                    if bienenKader[i].wait == 0:
                        bienenKader[i].flapFlag = 1
                else:
                    bienenKader[i].feierabend()
            elif bienenKader[i].goHome == 2:
                if bienenKader[i].wait != 0:
                    bienenKader[i].wait -= 1
                else: 
                    bienenKader[i].drin = 0
                    bienenKader[i].goHome = 0
            else:
                bienenKader[i].bienenMove()
        
        for i in range(len(blumenLaden)):
            for j in range(len(bienenKader)):
                if bienenKader[j].xpos == blumenLaden[i].xpos and bienenKader[j].ypos == blumenLaden[i].ypos and bienenKader[j].ladung == 0 and blumenLaden[i].besetzt != 1:
                    blumenLaden[i].besetzt = 1            
                    bienenKader[j].nektarSaugen(blumenLaden[i])

        for i in range(len(bienenKader)):
            if bienenKader[i].xpos == xstock and bienenKader[i].ypos == ystock and bienenKader[i].ladung == 1 and bienenKader[i].goHome != 0:
                bienenKader[i].nektarAbgabe()
            
                       
        theGrid, blumenLaden, bienenKader = gridComposer(theGrid, blumenLaden, bienenKader)

        drawWiese(theGrid, numberOfTheBees, waben, globalTick, blumenLaden, bienenKader)
        globalTick += 0.1
        time.sleep(0.1)

clear()
theGrid, bienenKader, blumenLaden, waben = startup()
main(theGrid, bienenKader, blumenLaden, waben)
