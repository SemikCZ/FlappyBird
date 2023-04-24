import pyglet
from pyglet import gl
from pyglet.window import key
from pyglet import shapes
import random

"""Naprogramuj hru Flappy Bird

Hra Flappy Bird spočívá v tom že pták prolétává skrze překážky 

Ovladani:

klavesa mezernik 

Konec: Esc

"""
#Atributy

SIRKA = 1200
VYSKA = 600
RYCHLOST = 200
RYCHLOST_PTAKA = RYCHLOST * 2


VELIKOST_PTAKA = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXTU = 30
TLOUSTKA_PTAKA = 10
SIRKA_PREKAZKY = 20
VYSKA_PREKAZKY = 50
VYSKA_PTAKA = 30
dt = 0.0


stisknute_klavesy = set()
pozice_prekazky = [0,0]
pozice_ptaka = [0,0]
rychlost_ptaka = [0,0]
score= [0]


def nakresli_ptaka(x1,y1,x2,y2): # Definice jednotlivých proměnných

    ptak = shapes.Circle(x1, y1, x2, y2, color=(255, 255, 0))
    ptak.draw()

def nakresli_oko(x1,y1,x2,y2) :

    oko = shapes.Circle(x1,y1,x2,y2, color=(0,0,0))
    oko.draw()

def nakresli_oko2(x1,y1,x2,y2) :

    oko2 = shapes.Circle(x1,y1,x2,y2, color=(255,255,255))
    oko2.draw()   

def nakresli_zobak(x1,y1,x2,y2) :

    zobak = shapes.Rectangle(x1,y1,x2,y2, color=(250,128,114))
    zobak.draw()

def nakresli_prekazku(x1,y1,x2,y2):

    prekazka = shapes.Rectangle(x1, y1, x2, y2, color = (124,252,0))
    prekazka.draw()

def reset() :
    # Nastaveni pozice ptaka - x-ova rychlost 
    if random.random() > 0.5:

        pozice_ptaka[0] = RYCHLOST
    else:
        pozice_ptaka[0] = -RYCHLOST
    # y-ova rychlost - uplne nahodna
    pozice_ptaka[1] = random.uniform(-1, 1) 
    score[0] = 0


def nakresli_text(text, x, y, pozice_x) :
    napis = pyglet.text.Label(
        text,
        font_name=None,
        font_size=VELIKOST_FONTU,
        x=y, y=x, anchor_x=pozice_x
    )
    napis.draw()



def vykresli ():

    window.clear()

    
    nakresli_ptaka(
        100,     #X-ova pozice ptaka
        250,     #Y-ova pozice ptaka
        35,    #Velikost ptaka horizontalne
        60)     #Velikost ptaka vertikalně

    nakresli_oko(
        112,
        265,
        10,
        60)    
    
    nakresli_oko2(
        112,
        265,
        5,
        5)
    
    nakresli_zobak(
        100,
        230,
        30,
        9
    )

    nakresli_prekazku(
        1000,
        500,
        100,
        700
    )

    nakresli_prekazku(
        1000,
        250,
        -100,
        -700
    )
    nakresli_prekazku(
        600,
        250,
        100,
        400
    )
    nakresli_text(str(score[0]),
              x=VYSKA - ODSAZENI_TEXTU,
              y=SIRKA - ODSAZENI_TEXTU,
              pozice_x='left')
   
    
def obnov_stav(dt): #Aktualizuje ptáka na základě vstupů z klávesnice
    global pozice_prekazky, pozice_ptaka, rychlost_ptaka, score, hra_aktivni

    # Aktualizace pozice ptaka
    if ('nahoru', 1) in stisknute_klavesy:
        rychlost_ptaka[1] = RYCHLOST_PTAKA
    else:
        rychlost_ptaka[1] -= RYCHLOST * dt
    pozice_ptaka[1] += rychlost_ptaka[1] * dt
    # Detekce srážky
    if pozice_ptaka[0] + TLOUSTKA_PTAKA > pozice_prekazky[0] and \
       pozice_ptaka[0] < pozice_prekazky[0] + SIRKA_PREKAZKY and \
       (pozice_ptaka[1] + VYSKA_PTAKA > pozice_prekazky[1] + VYSKA_PREKAZKY or \
        pozice_ptaka[1] < pozice_prekazky[1]):
        print("Kolize!")
        hra_aktivni = False

    score[0] += 1

def stisk_klavesy(symbol, modifikatory,): # Přiřazení klávesy SPACE požadovanou funkci
    global pozice_ptaka
    if symbol == key.SPACE:
        stisknute_klavesy.add(('nahoru', 1))
        pozice_ptaka[1] += RYCHLOST_PTAKA * dt

def pusteni_klavesy(symbol, modifikatory,): # Vynulování klávesy SPACE
    global pozice_ptaka
    if symbol == key.SPACE:
        stisknute_klavesy.discard(('nahoru', 1))
        pozice_ptaka[1] -= RYCHLOST_PTAKA *dt
        pozice_ptaka[1] = max(pozice_ptaka[1], 0)


reset()      


window = pyglet.window.Window(width=SIRKA, height=VYSKA) # Velikost okna

window.push_handlers(
    on_draw = vykresli,
    on_key_press = stisk_klavesy,
    on_key_release = pusteni_klavesy 
)

pyglet.clock.schedule(obnov_stav)
pyglet.app.run()



