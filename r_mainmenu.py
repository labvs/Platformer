""" Игра показывает главное меню """

import arcade
import random
import os

def on_render_mainmenu():
    """ Главное меню """
    # Дальше пишем все что будем рисовать
    # пример рисования смайлика: http://arcade.academy/examples/happy_face.html#happy-face
    # функции рисования: http://arcade.academy/quick_index.html#drawing-module
    # сайт фреймворка arcade: http://arcade.academy

    # Текст
    start_x = 50
    start_y = 450
    arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
    arcade.draw_text("Главное меню", start_x, start_y, arcade.color.BLACK, 40)

