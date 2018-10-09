import arcade
import random
import os

def on_render_game():
    # Текст
    start_x = 50
    start_y = 450
    arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
    arcade.draw_text("Идет Игра", start_x, start_y, arcade.color.BLACK, 40)
