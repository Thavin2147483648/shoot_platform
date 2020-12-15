from models.LevelObject import StaticLevelObject
from constants import Turret as Properties
from enums import DirectionX
from objects.Bullet import Bullet
from constants import Bullet as BulletProperties


class Turret(StaticLevelObject):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    EXTRA_WIDTH = 52
    ANIMATION = Properties.ANIMATION
    CAN_COLLIDE = True
    GROUP_NAME = 'turret'
    SHOOT_PERIOD = 50
    OFFSET_Y = 18

    def __init__(self, scene, cell_x, cell_y, *groups, shoot_period=SHOOT_PERIOD):
        super().__init__(scene, cell_x, cell_y, *groups)
        self.extra_width = self.EXTRA_WIDTH
        self.direction_x = DirectionX.LEFT
        self.shoot_period = shoot_period

    def process_logic(self, events):
        player = self.scene.get_object('main_character')
        if player.get_middle_x() <= self.get_middle_x():
            self.direction_x = DirectionX.LEFT
        else:
            self.direction_x = DirectionX.RIGHT
        d = ('left' if self.direction_x == DirectionX.LEFT else 'right')
        if self.scene.game.get_frames() % self.get_shoot_period() == 0:
            self.shoot()
        self.animation.set_animation('none_' + d)

    def get_extra_width(self):
        return self.extra_width

    def get_shoot_period(self):
        return self.shoot_period

    def get_direction_x(self):
        return self.direction_x

    def get_render_rect(self):
        rect = super(Turret, self).get_render_rect()
        rect.width += self.get_extra_width()
        if self.direction_x == DirectionX.LEFT:
            rect.x -= self.get_extra_width()
        return rect

    def shoot(self):
        d = self.get_direction_x()
        if d == DirectionX.LEFT:
            bullet = Bullet(self.scene, self.get_x1() - self.get_extra_width() - BulletProperties.WIDTH,
                            self.get_y1() + self.OFFSET_Y, d)
        else:
            bullet = Bullet(self.scene, self.get_x2() + self.get_extra_width(),
                            self.get_y1() + self.OFFSET_Y, d)
        self.scene.add_object(bullet)
