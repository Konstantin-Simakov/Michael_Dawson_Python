# exercise2.py
# 'Space invaders' game simulator.

import math, random
from superwires import games, color

games.init(screen_width=640, screen_height=480, fps=50)

class Wrapper(games.Sprite):
    """ The sprite moves around the graphic screen. """
    def update(self):
        """ Move the object only horizontally. """
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

    def die(self):
        """ Destroy the object. """
        self.destroy()


class Collider(Wrapper):
    """ The sprite that could move around the graphic screen and be destroyed. """
    def update(self):
        """ Check if there are sprites visaully overlapping the given one. """
        super().update()
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """ Destroy the object with explosion. """
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Invader(Wrapper):
    """ Space invader. It needs >=1 missiles to destroy it. """
    IMAGE = games.load_image("space_invader.bmp")
    SPEED = 2
    MIN_SPEED = SPEED / 10
    POINTS = 20
    lives = 1
    total = 0

    def __init__(self, game, x, y):
        """ Initialize a sprite with the invader picture. """
        Invader.total += 1
        
        # Set the random speed for an invader but
        # not less than Invader.MIN_SPEED value.
        dy = Invader.SPEED * random.random()
        if dy < Invader.MIN_SPEED:
            dy = Invader.MIN_SPEED
        
        super().__init__(
                image=Invader.IMAGE,
                x=x,
                y=y,
                dy=dy)
        self.game = game
        # How many missiles does it need to destroy the invader.
        self.lives = Invader.lives

    def die(self):
        """ Destroy the invader with counting its lives. """
        self.lives -= 1
        if 0 == self.lives:
            super().die()
            Invader.total -= 1

            self.game.score.value += Invader.POINTS
            self.game.score.right = games.screen.width - 10

            # If there are no more invaders, go to the next level.
            if 0 == Invader.total:
                # And if there is a max level end the game with winning.
                if Game.MAX_LEVEL == self.game.level:
                    self.game.win()
                else:
                    self.game.advance()

    def update(self):
        """ 
        Check to see if the invader's bottom has reached the side of the screen. 
        """
        if self.bottom > games.screen.height:
            self.game.lose()

        # For safe operation of the update() method.
        super().update()


class Cannon(Wrapper):
    """ Player's cannon. """
    IMAGE = games.load_image("space_cannon.bmp")
    # It could be launched 3 missile per second.
    MISSILE_DELAY = games.screen.fps / 3;
    SPEED = 7

    def __init__(self, game, x):
        """ Initialize the sprite with spaceship picture. """
        super().__init__(
            image=Cannon.IMAGE,
            x=x,
            y=games.screen.height-40,
            is_collideable=False)
        self.missile_wait = 0
        self.game = game

    def update(self):
        """ 
        Move the cannon left and right when the corresponding arrow key is pressed. 
        """
        # The cannon doesn't move in normal condition.
        self.dx = 0
        # When the cannon can move.
        if games.keyboard.is_pressed(games.K_LEFT):
            self.dx = -Cannon.SPEED
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.dx = Cannon.SPEED

        # Check graphics screen bounds.
        super().update()
        
        # Missile launch;
        # if the 'Space' is pressed and waiting interval is ended, launch a missile.
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait <= 0:
            new_missile = Missile(self.x)
            games.screen.add(new_missile)
            self.missile_wait = Cannon.MISSILE_DELAY

        # If the next missile is not yet authorized to launch, 
        # subtract 1 from the length of the remaining waiting interval. 
        if self.missile_wait > 0:
            self.missile_wait -= 1


class Missile(Collider):
    """ Missile that the player's cannon could launch.  """
    IMAGE = games.load_image("missile.bmp")
    SOUND = games.load_sound("missile.wav")
    BUFFER = 50
    VELOCITY = 7
    LIFETIME = games.screen.fps * 1.1

    def __init__(self, cannon_x):
        """ Initialize a sprite with image of a missile. """
        Missile.SOUND.set_volume(0.3)
        Missile.SOUND.play()
        
        x = cannon_x
        y = games.screen.height - Missile.BUFFER

        # Calculate vertical velocity of the missile (horizontal dx = 0).
        dy = -Missile.VELOCITY

        # Create the missile.
        super().__init__(
                image=Missile.IMAGE,
                x=x,
                y=y,
                dy=dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Move the missile. """
        # If the missile has "expired", it is destroyed.
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.destroy()

        # The rocket will go through bounds of the graphics screen.
        # Check if the sprite overlaps with another ones.
        super().update()


class Explosion(games.Animation):
    """ Animation explosion. """
    SOUND = games.load_sound("explosion.wav")
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
        Explosion.SOUND.set_volume(0.3)
        Explosion.SOUND.play()


class Game(object):
    """ The actual game. """
    MAX_LEVEL = 10
    def __init__(self):
        """ Initialize a Game object. """
        # Choose the initial level.
        self.level = 0
        # Load music to accompany the transition to the next level.
        self.sound = games.load_sound("level.wav")
        # Create an object where the current score will be saved.
        self.score = games.Text(
                value=0,
                size=30,
                color=color.white,
                top=5,
                right=games.screen.width-10,
                is_collideable=False)
        games.screen.add(self.score)
        # Create a cannon that the user will control.
        self.cannon = Cannon(
                game=self,
                x=games.screen.width/2)
        games.screen.add(self.cannon)

    def play(self):
        """ Start the game. """
        # Start the music theme.
        games.music.load("space_battle.mp3")
        games.music.play(-1)
        # Load and set a background.
        NEBULA_IMAGE = games.load_image("nebula.jpg")
        games.screen.background = NEBULA_IMAGE
        # Go to level 1.
        self.advance()
        # Start the game.
        games.screen.mainloop()

    def advance(self):
        """ Takes the game to the next level. """
        self.level += 1
        # Increase the number of lives for each invader, speed of the cannon and
        # decrease missile delay before the next missile launch.
        # if the level is even, starting at level 2.
        if self.level % 2 == 0:
            Invader.lives += 1
            Cannon.SPEED += 1
            Cannon.MISSILE_DELAY -= 1
        
        # Add a new space invader.
        for i in range(self.level):
            # Calculate initial x and y coordinates of the invader.
            x = random.randrange(10, games.screen.width - 10)
            y = 10
            # Create a new invader.
            new_invader = Invader(
                    game=self,
                    x=x,
                    y=y)
            games.screen.add(new_invader)

        # Display the level number in 3 seconds.
        level_message = games.Message(
                value="Level "+str(self.level),
                size=40,
                color=color.yellow,
                x=games.screen.width/2,
                y=games.screen.height/10,
                lifetime=3*games.screen.fps,
                is_collideable=False)
        games.screen.add(level_message)
        # Sound effect of going (besides the 1st level).
        if self.level > 1:
            self.sound.set_volume(0.3)
            self.sound.play()

    def lose(self):
        """ End the game with losing. """
        # Display in 3 seconds the message.
        end_message = games.Message(
                value="You lose.",
                size=90,
                color=color.red,
                x=games.screen.width/2,
                y=games.screen.height/2,
                lifetime=3*games.screen.fps,
                after_death=games.screen.quit,
                is_collideable=False)
        games.screen.add(end_message)

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


def main():
    space_invaders = Game()
    space_invaders.play()


# Go!
if "__main__" == __name__:
    main()

