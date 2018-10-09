#-*- coding: utf-8 -*-
''' Простой платформер
'''
### Импорт необходимых модулей
import arcade
import random
import os

### Константы
SPRITE_SCALING = 0.5
# Ширина и высота экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

### Импорт модуйле, который реализуют различные состояния игры
from r_title import on_render_title
from r_game import on_render_game
from r_pause import on_render_pause
from r_mainmenu import on_render_mainmenu
from r_gameover import on_render_gameover

### Основной класс игры
class MyGame(arcade.Window):
    """ Основной игровой класс """

    def __init__(self, width, height):
        # Вызываем родительский класс и создаем окно
        super().__init__(width, height)
        # Перекрашиваем фон окна
        arcade.set_background_color(arcade.color.AMAZON)        

    def setup(self):
        # Всякие начальные установки
        self.is_full_screen = False
        self.set_fullscreen(self.is_full_screen)
        # Переменные, который будут переключать состояние игры
        self.isTitle = 1
        self.isGame = 2
        self.isPause = 3
        self.isMainMenu = 4
        self.isGameOver = 5
        # При старте игры переводим ее в состояние "Заставка"
        self.GameState = self.isTitle
        # Подключаем функции, которые будут отрисовывать соовтетствующие состояния игры
        self.on_render_title = on_render_title
        self.on_render_game = on_render_game
        self.on_render_pause = on_render_pause
        self.on_render_mainmenu = on_render_mainmenu
        self.on_render_gameover = on_render_gameover       

    def on_draw(self):
        """ Рендерить это окно """
        arcade.start_render()
        if self.GameState == self.isTitle:
            self.on_render_title()
        if self.GameState == self.isGame:
            self.on_render_game()
        if self.GameState == self.isPause:
            self.on_render_pause()            
        if self.GameState == self.isMainMenu:
            self.on_render_mainmenu()
        if self.GameState == self.isGameOver:
            self.on_render_gameover()                                
        
    def on_key_press(self, key, modifiers):
        """ Нажатия на кнопки """
        if key == arcade.key.ESCAPE:
            arcade.window_commands.close_window()
        # Переключение в полноэкранный режим и обратно
        # http://arcade.academy/examples/full_screen_example.html
        if key == arcade.key.F12:            
            self.is_full_screen = not self.is_full_screen
            self.set_fullscreen(self.is_full_screen)

        if key == arcade.key.KEY_1:
            self.GameState = self.isTitle
        if key == arcade.key.KEY_2:
            self.GameState = self.isGame
        if key == arcade.key.KEY_3:
            self.GameState = self.isPause
        if key == arcade.key.KEY_4:
            self.GameState = self.isMainMenu
        if key == arcade.key.KEY_5:
            self.GameState = self.isGameOver
                               
    def update(self, delta_time):
        """ Вся логика, перемещение и т.п должна быть тут"""
        pass


def main():    
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
    

if __name__ == "__main__":
    main()
