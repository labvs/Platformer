""" Заставка игры """

import arcade
import random
import os

def on_render_title():
    """ Заставка """
    # Дальше пишем все что будем рисовать
    # пример рисования смайлика: http://arcade.academy/examples/happy_face.html#happy-face
    # функции рисования: http://arcade.academy/quick_index.html#drawing-module
    # сайт фреймворка arcade: http://arcade.academy

    # Текст
    start_x = 50
    start_y = 450
    arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
    arcade.draw_text("Идет Заставка", start_x, start_y, arcade.color.BLACK, 40)
