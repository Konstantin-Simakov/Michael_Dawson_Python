# exercise3.py
# 'Pacman' game simulator.

import random
from superwires import games, color

games.init(screen_width=640, screen_height=480, fps=50)

class Pacman(games.Animation):
    """ An actual pacman. """
    IMAGES = [
        "pacman1.bmp",
        "pacman2.bmp"
    ]
    # The speed will be increased with level up.
    # Pacman's eat sound.
    sound = games.load_sound("eat.wav")
    sound.set_volume(0.35)
    speed = 5

    def __init__(self, game, x, y):
        """ Create a pacman. """
        super().__init__(
                images=Pacman.IMAGES,
                x=x,
                y=y,
                repeat_interval=6)
        self.game = game


    def eat(self):
        """ Kill sprites that overlapping with the pacman. Pacman "eats". """
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            Pacman.sound.play()


    def move(self):
        """ How the pacman can move and rotate. """
        if games.keyboard.is_pressed(games.K_UP):
            self.dx = 0
            self.dy = -Pacman.speed
            self.angle = -90
        elif games.keyboard.is_pressed(games.K_DOWN):
            self.dx = 0
            self.dy = Pacman.speed
            self.angle = 90
        elif games.keyboard.is_pressed(games.K_LEFT):
            self.dx = -Pacman.speed
            self.dy = 0
            self.angle = 180
        elif games.keyboard.is_pressed(games.K_RIGHT):
            self.dx = Pacman.speed
            self.dy = 0
            self.angle = 0
    
    def die(self):
        """ Pacman dies with explosion. """
        self.destroy()
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def disappear(self):
        """ Pacman desappears. """
        self.destroy()

    def stop(self):
        """ 
        If the pacman achieves graphics screen bounds, it stops 
        without changing its angle. 
        """
        self.dx = 0
        self.dy = 0

    def update(self):
        """ 
        Check if there are sprites visaully overlapping the given one; 
        if it is, eat it. 
        Check the bounds of the graphics screen; 
        if the pacman collides it, the game is ended.
        Set the capable to move for the pacman.
        """
        # Pacman must move if it's alive.
        self.move()
        # Eat the 'item'.
        self.eat()

        # Check bounds of the graphics screen.
        if (self.right > games.screen.width or
                self.left < 0 or 
                self.top < 0 or
                self.bottom > games.screen.height):
            self.game.lose()


class Explosion(games.Animation):
    """ Animation explosion. """
    sound = games.load_sound("explosion.wav")
    IMAGES = [
            "explosion1.bmp",
            "explosion2.bmp",
            "explosion3.bmp",
            "explosion4.bmp",
            "explosion5.bmp",
            "explosion6.bmp",
            "explosion7.bmp",
            "explosion8.bmp",
    ]

    def __init__(self, x, y):
        super().__init__(
                images=Explosion.IMAGES,
                x=x,
                y=y,
                repeat_interval=4,
                n_repeats=1,
                is_collideable=False)
        Explosion.sound.set_volume(0.3)
        Explosion.sound.play()


class Item(games.Sprite):
    """ "Item" that the pacman eats. """
    IMAGE = games.load_image("item.bmp")
    POINTS = 10
    total = 0

    def __init__(self, game, x, y):
        """ Initialize a sprite with the 'item' picture. """
        Item.total += 1
        super().__init__(
                image=Item.IMAGE,
                x=x,
                y=y)
        self.game = game

    def die(self):
        """ Item dies and disappears when the pacman eats it.  """
        Item.total -= 1
        self.destroy()

        # Increase the number of scores in the game.
        self.game.score.value += Item.POINTS
        self.game.score.right = games.screen.width - 10

        # If there are no items, go to the next level.
        if 0 == Item.total:
            # And if there is a max level end the game with winning.
            if Game.MAX_LEVEL == self.game.level:
                self.game.win()
            else:
                self.game.advance()


class Game(object):
    """ The actual game. """
    MAX_LEVEL = 10
    # Minimum indentation of all objects from the bounds grpaphics screen.
    INDENT = 20

    def __init__(self):
        """ Initialize a Game object. """
        # Choose the initial level.
        self.level = 0
        # Load music to accompany the transition to the next level.
        self.sound = games.load_sound("level.wav")
        self.sound.set_volume(0.5)
        # Create an object where the current score will be saved.
        self.score = games.Text(
                value=0,
                size=30,
                color=color.white,
                top=5,
                right=games.screen.width-10,
                is_collideable=False)
        games.screen.add(self.score)
        # Create a pacman that the user will control
        # in the left lower corner of the graphics screen.
        self.pacman = Pacman(
                game=self,
                x=Game.INDENT,
                y=games.screen.height-Game.INDENT)
        games.screen.add(self.pacman)

    def play(self):
        """ Start the game. """
        # Start the music theme.
        games.music.load("pacman_theme.mp3")
        games.music.play(-1)
        # Load and set background.
        NEBULA_IMAGE = games.load_image("nebula.jpg")
        games.screen.background = NEBULA_IMAGE
        # Go to level 1.
        self.advance()
        # Start the game.
        games.screen.mainloop()

    def advance(self):
        """ Take the game to the next level. """
        self.level += 1
        # Increase Pacman's speed if the level is even.
        if self.level % 2 == 0:
            Pacman.speed += 1

        # Reverse minimum space around the pacman through horizontal and vertical.
        BUFFER_X = games.screen.width // 5
        BUFFER_Y = games.screen.height // 5
        # Add new items.
        # The factor of new items compared to a current level.
        FACTOR = 2
        for i in range(self.level * FACTOR):
            # First, choose indents through horizontal and vertical from the pacman.
            x_distance = random.randrange(BUFFER_X, games.screen.width - Game.INDENT)
            y_distance = random.randrange(BUFFER_Y, games.screen.height - Game.INDENT)
            # Based on these distances, calculate screen coordinates.
            x = self.pacman.x + x_distance
            y = self.pacman.y + y_distance

            # If it is needed, return the object inside the window.
            x %= games.screen.width
            y %= games.screen.height

            # Move it from bounds a bit, else this game will be too difficult.
            if x < Game.INDENT:
                x = Game.INDENT
            elif x > games.screen.width - Game.INDENT:
                x = games.screen.width - Game.INDENT
            if y < Game.INDENT:
                y = Game.INDENT
            elif y > games.screen.height - Game.INDENT:
                y = games.screen.height - Game.INDENT

            # Create a new item with x and y values calculated above.
            new_item = Item(
                    game=self,
                    x=x,
                    y=y)
            games.screen.add(new_item)

        # Display the level number.
        level_message = games.Message(
                value="Level"+str(self.level),
                size=40,
                color=color.yellow,
                x=games.screen.width/2,
                y=games.screen.height/10,
                lifetime=3*games.screen.fps,
                is_collideable=False)
        games.screen.add(level_message)
        # Sound effect of going (besides the 1st level)
        if self.level > 1:
            self.sound.play()

    def lose(self):
        """ End the game with losing. """
        # Display in 3 seconds the message.
        end_message = games.Message(
                value="You lose",
                size=90,
                color=color.red,
                x=games.screen.width/2,
                y=games.screen.height/2,
                lifetime=3*games.screen.fps,
                after_death=games.screen.quit,
                is_collideable=False)
        games.screen.add(end_message)
        # Pacman dies here.
        self.pacman.die()
        
        # Play losing music after base music stops.
        sound = games.load_sound("lose.wav")
        games.music.stop()
        sound.play()

    def win(self):
        """ End the game with winning. """
        # Display in 3 seconds the message.
        end_message = games.Message(
                value="You win!",
                size=90,
                color=color.yellow,
                x=games.screen.width/2,
                y=games.screen.height/2,
                lifetime=3*games.screen.fps,
                after_death=games.screen.quit,
                is_collideable=False)
        games.screen.add(end_message)
        # Pacman disappears here.
        self.pacman.disappear()

        # Play losing music after base music stops.
        sound = games.load_sound("win.wav")
        games.music.stop()
        sound.play()


def main():
    pacman = Game()
    pacman.play()


# Go!
if "__main__" == __name__:
    main()
