from enum import Flag
import imp
from sys import byteorder
from tkinter import Scale
from turtle import position
from ursina import * 

app = Ursina()


line_1 = Entity(model = 'cube', color = rgb(79, 70, 70), position = (-5,0), scale = (0.05, 8, 0), )

window.color = rgb(47, 45, 45)
window.fps_counter.enabled = False
window.exit_button.visible = False
window.exit_button.ignore = True
window.title = 'Game Launcher'
window.windowed_position = True
window.borderless = False
window.cog_menu = False
window.cog_button = False
window.icon = 'game_icon2.ico'


app.run()