# -*- coding: utf-8 -*-
"""

@author: H Persévérance
"""

import pyglet, random 
from pyglet.image import load 
from pyglet.window import key
import pyglet.gui 

win = pyglet.window.Window(700, 600, caption='Pierre-Papier-Ciseau') 
batch = pyglet.graphics.Batch()
group = pyglet.graphics.OrderedGroup
frame = pyglet.gui.Frame(win)
pyglet.gl.glClearColor(0.8, 0.8, 0.8, 1.0)

@win.event
def on_draw():
    win.clear()
    batch.draw()
    
@win.event
def on_key_press(symbol, modifiers):
    if symbol==key.ENTER and play.enabled:
        on_play(True)
        play.value = True
    
icon1 = load('16_16.png')
icon2 = load('32px.png')
win.set_icon(icon1, icon2)
play_img = load('play.png')
play_h_img = load('play_h.png')
play_p_img = load('play_p.png')
ci_p = load('ci_p.png')
ci_h = load('ci_h.png')
ci = load('ci.png')
pa_p = load('pa_p.png')
pa_h = load('pa_h.png')
pa = load('pa.png')
pi_p = load('pi_p.png')
pi_h = load('pi_h.png')
pi = load('pi.png') 

def enabled(a):
    global pierre, papier, ciseau
    pierre.enabled = a
    papier.enabled = a 
    ciseau.enabled = a

def on_pierre():
    global player_score, random_score
    enabled(False)
    random_player = random.choice(['pierre', 'papier', 'ciseau']) 
    if random_player=='pierre' :
        label.text = "    Match nul\n Appuyez sur 'Play'"
    elif random_player=='ciseau':
        label.text = " Vous avez gagné\n Appuyez sur 'Play'"
        player_score += 1
    else:
        label.text = "    J'ai gagné\n Appuyez sur 'Play'"
        random_score += 1 
    player_label.text = f'Votre Choix : "pierre" \nScore : {player_score}'
    random_label.text = f'Ordinateur : "{random_player}" \nScore : {random_score}'
    play.enabled = True
    play.value = False

def on_papier():
    global player_score, random_score
    enabled(False)
    random_player = random.choice(['pierre', 'papier', 'ciseau']) 
    if random_player=='papier' :
        label.text = "    Match nul\n Appuyez sur 'Play'"
    elif random_player=='pierre':
        label.text = " Vous avez gagné\n Appuyez sur 'Play'"
        player_score += 1
    else:
        label.text = "    J'ai gagné\n Appuyez sur 'Play'"
        random_score += 1 
    player_label.text = f'Votre Choix : "papier" \nScore : {player_score}'
    random_label.text = f'Ordinateur : "{random_player}" \nScore : {random_score}'
    play.enabled = True
    play.value = False

def on_ciseau():
    global player_score, random_score
    enabled(False)
    random_player = random.choice(['pierre', 'papier', 'ciseau']) 
    if random_player=='ciseau' :
        label.text = "    Match nul\n Appuyez sur 'Play'"
    elif random_player=='papier':
        label.text = " Vous avez gagné\n Appuyez sur 'Play'"
        player_score += 1
    else:
        label.text = "    J'ai gagné\n Appuyez sur 'Play'"
        random_score += 1 
    player_label.text = f'Votre Choix : "ciseau" \nScore : {player_score}'
    random_label.text = f'Ordinateur : "{random_player}" \nScore : {random_score}'
    play.enabled = True
    play.value = False

def on_play(value):
    enabled(True)
    if not value :
        label.text = 'Appuyer sur play'
    else:
        play.enabled = False
        label.text = 'Cliquer sur votre choix entre le papier, la pierre, et le ciseau' 
        # random_label.text = f'Ordinateur :  \nScore : {random_score}'
        # player_label.text = f'Votre Choix :  \nScore : {player_score}'

x = ( win.width - (ci.width + pi.width + pa.width +20) )/2
y = win.height - 10 - ci.height 
random_score = 0 
player_score = 0 

pierre = pyglet.gui.PushButton(x, y, pi_p, pi, hover=pi_h, batch=batch, group=group(1))
pierre.set_handler('on_release', on_pierre)
frame.add_widget(pierre)

x += pi.width+10
papier = pyglet.gui.PushButton(x, y, pa_p, pa, hover=pa_h, batch=batch, group=group(1))
papier.set_handler('on_release', on_papier)
frame.add_widget(papier)

x += pa.width+10
ciseau = pyglet.gui.PushButton(x, y, ci_p, ci, hover=ci_h, batch=batch, group=group(1))
ciseau.set_handler('on_release', on_ciseau)
frame.add_widget(ciseau)

x = (win.width-play_img.width)//2
play = pyglet.gui.ToggleButton(x, 80, play_p_img, play_img, hover=play_h_img, batch=batch, group=group(1) )
play.set_handler('on_toggle', on_play)
frame.add_widget(play)

enabled(False)

player_label = pyglet.text.Label('Votre Choix :  \nScore : 0', font_name='Times New Roman', font_size=14, bold=True, color=(0, 0, 0, 255),
                                 x=20, y=250, anchor_x='left', multiline=True, width=win.width//2-20, batch=batch) 
random_label = pyglet.text.Label('Ordinateur :  \nScore : 0', font_name='Times New Roman', font_size=14, bold=True, color=(0, 0, 0, 255),
                                 x=win.width-10, y=250, anchor_x='right', multiline=True, width=win.width//2-10, batch=batch)
label = pyglet.text.Label('\tAppuyez sur "Play"', font_name='Times New Roman', font_size=14, color=(0, 0, 0, 255),
                                 x=win.width//2, y=y-10, anchor_x='center', anchor_y='top', multiline=True, width=300, batch=batch)


pyglet.app.run()
        
    
        
        
    
     
    