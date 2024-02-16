# exercise1.py
# 
# Asteroids move across the screen and
# the ship can rotates.
# When the player turns on the ship's engine, 
# the speed changes appropriately based on the angle of the ship, 
# and a characteristic sound is heard.
# Missiles were added.
# Add Fire density control was added.
# Colision processing was added.
# Wrapper was added.
# Explosions was added.
# Levels, music theme, game statistics are added.
# Space debris added. It needs 2 missiles to be destroyed.
# 

import math, random
from superwires import games, color

games.init(screen_width=640, screen_height=480, fps=50)

class Wrapper(games.Sprite):
    """ The sprite moves around the graphic screen. """
    def update(self):
        """ Moves the sprite to the opposite side of the window. """
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

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


class Asteroid(Wrapper):
    """ An asteroid moving in a straight line across the screen. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    IMAGES = {SMALL: games.load_image("asteroid_small.bmp"),
              MEDIUM: games.load_image("asteroid_medium.bmp"),
              LARGE: games.load_image("asteroid_large.bmp")}
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self, game, x, y, size):
        """ Initialize a sprite with the asteroid picture. """
        Asteroid.total += 1
        super().__init__(
                image=Asteroid.IMAGES[size],
                x=x,
                y=y,
                dx=random.choice([-1, 1]) * Asteroid.SPEED * random.random()/size,
                dy=random.choice([-1, 1]) * Asteroid.SPEED * random.random()/size)
        self.size = size
        self.game = game

    def die(self):
        """ Destroy the asteroid. """
        Asteroid.total -= 1

        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        # If the size of asteroid is large or middle, 
        # replace it with SPAWN=2 smaller ones.
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(
                        game=self.game,
                        x=self.x,
                        y=self.y,
                        size=self.size-1)
                games.screen.add(new_asteroid)
        # If there are no more asteroids, go to the next level.
        if 0 == Asteroid.total and 0 == Debris.total:
            self.game.advance()
        super().die()


class Debris(Wrapper):
    """ Space debris. It needs 2 missiles to destroy it. """
    IMAGE = games.load_image("space_debris.bmp")
    SPEED = 3
    POINTS = 40
    total = 0

    def __init__(self, game, x, y, size=Asteroid.LARGE):
        """ Initialize a sprite with the asteroid picture. """
        Debris.total += 1
        super().__init__(
                image=Debris.IMAGE,
                x=x,
                y=y,
                dx=random.choice([-1, 1]) * Debris.SPEED * random.random()/size,
                dy=random.choice([-1, 1]) * Debris.SPEED * random.random()/size)
        self.size = size
        self.game = game
        self.lives = 2

    def die(self):
        """ Destroy the Debris with counting its lives. """
        self.lives -= 1
        if 0 == self.lives:
            Debris.total -= 1

            self.game.score.value += Debris.POINTS
            self.game.score.right = games.screen.width - 10

            # If there are no more Debriss, go to the next level.
            if 0 == Asteroid.total and 0 == Debris.total:
                self.game.advance()
            super().die()


class Ship(Collider):
    """ Player's ship. """
    IMAGE = games.load_image("ship.bmp")
    SOUND = games.load_sound("thrust.wav")
    ROTATION_STEP = 3
    VELOCITY_STEP = 0.03
    # It could be launched 2 missile per second.
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        """ Initialize the sprite with spaceship picture. """
        super().__init__(
            image=Ship.IMAGE,
            x=x,
            y=y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        """ Rotate the ship when arrow keys is pressed. """
        # Limit horizontal and vertical velocities.
        self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        
        # The ship makes a jerk.
        if games.keyboard.is_pressed(games.K_UP):
            Ship.SOUND.play()
            # Convert degrees to radians.
            angle = self.angle * math.pi / 180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        # The ship stops.
        if games.keyboard.is_pressed(games.K_DOWN):
            self.dx = 0
            self.dy = 0

        # If the Space is pressed and waiting interval is ended, launch a missile.
        if games.keyboard.is_pressed(games.K_SPACE) and 0 == self.missile_wait:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

        # If the next missile is not yet authorized to launch, 
        # subtract 1 from the length of the remaining waiting interval. 
        if self.missile_wait > 0:
            self.missile_wait -= 1

        # The ship will go around the screen.
        # Check if the sprite overlaps with another ones.
        super().update()

    def die(self):
        """ Destroy the ship and end the game. """
        self.game.end()
        super().die()


class Missile(Collider):
    """ Missile that the player's spaceship could launch.  """
    IMAGE = games.load_image("missile.bmp")
    SOUND = games.load_sound("missile.wav")
    BUFFER = 70
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """ Initialize a sprite with image of a missile. """
        Missile.SOUND.play()
        
        # Convert degrees to radians.
        angle = ship_angle * math.pi / 180
        # Calculate the start position of the missile.
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # Calculate horizontal and vertical velocity of the missile.
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # Create the missile.
        super().__init__(
                image=Missile.IMAGE,
                x=x,
                y=y,
                dx=dx,
                dy=dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Move the missile. """
        # If the missile has "expired", it is destroyed.
        self.lifetime -= 1
        if 0 == self.lifetime:
            self.destroy()

        # The rocket will go around the screen.
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
        Explosion.SOUND.play()


class Game(object):
    """ The actual game. """
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
        # Create a ship that the user will control.
        self.ship = Ship(
                game=self,
                x=games.screen.width/2,
                y=games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        """ Start the game. """
        # Start the music theme.
        games.music.load("theme.mid")
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

        # Reversed space around the ship.
        BUFFER = 150
        # Create new asteroids.
        for i in range(self.level):
            # Calculate x and y so that they are at least 150 pixels away from the ship.
            # First, choose minimum indents through horizontal and vertical.
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            # Based on these indentations, we will generate 
            # horizontal and vertical distances from the ship.
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)
            # Based on these distances, calculate screen coordinates.
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            # If it is needed, return the object inside the window.
            x %= games.screen.width
            y %= games.screen.height

            # Create an asteroid.
            new_asteroid = Asteroid(
                    game=self,
                    x=x,
                    y=y,
                    size=Asteroid.LARGE)
            games.screen.add(new_asteroid)

        # Create new space debris.
        for i in range(self.level):
            # Calculate x and y so that they are at least 150 pixels away from the ship.
            # First, choose minimum indents through horizontal and vertical.
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            # Based on these indentations, we will generate 
            # horizontal and vertical distances from the ship.
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)
            # Based on these distances, calculate screen coordinates.
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            # If it is needed, return the object inside the window.
            x %= games.screen.width
            y %= games.screen.height

            # Create a new derbis.
            new_debris = Debris(
                    game=self,
                    x=x,
                    y=y)
            games.screen.add(new_debris)

        # Display the level number.
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
            self.sound.play()

    def end(self):
        """ End the game. """
        # Display in 5 seconds the message 'Game Over'.
        end_message = games.Message(
                value="Game Over",
                size=90,
                color=color.red,
                x=games.screen.width/2,
                y=games.screen.height/2,
                lifetime=5*games.screen.fps,
                after_death=games.screen.quit,
                is_collideable=False)
        games.screen.add(end_message)


def main():
    astrocrash = Game()
    astrocrash.play()


# Go!
if "__main__" == __name__:
    main()
