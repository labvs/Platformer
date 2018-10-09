import arcade
import random
import os

def on_render_boom():
        """ Заставка """
        # Дальше пишем все что будем рисовать
        x = 300; y = 300; radius = 100
        arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

        # Левый глаз
        x = 350; y = 320; radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

        # Правый глаз
        x = 250; y = 320; radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

        # Улыбка
        x = 300; y = 300; width = 80; height = 70
        start_angle = 190; end_angle = 350
        arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

        # Текст
        start_x = 100
        start_y = 500
        arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
        arcade.draw_text("Идет Взрыв", start_x, start_y, arcade.color.BLACK, 40)
        arcade.draw_text("Михаил Куприенко", start_x, start_y, arcade.color.BLACK, 40)