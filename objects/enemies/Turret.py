from models.BarIndicator import BarIndicatorColor, BarIndicator
from models.Float import Float
from models.LevelObject import StaticLevelObject
from constants import Turret as Properties
from enums import DirectionX
from models.ObjectWithHealth import ObjectWithHealth
from objects.Bullet import Bullet
from constants import Bullet as BulletProperties, HealthIndicator
from models.ObjectHealthIndicator import ObjectHealthIndicator


class Turret(StaticLevelObject, ObjectWithHealth):
    WIDTH = Properties.WIDTH
    HEIGHT = Properties.HEIGHT
    EXTRA_WIDTH = 52
    ANIMATION = Properties.ANIMATION
    CAN_COLLIDE = True
    GROUP_NAME = 'turret'
    SHOOT_PERIOD = 30
    OFFSET_Y = 18
    DAMAGEABLE = True
    HEALTH = Properties.HEALTH
    SCORE = 300

    def __init__(self, scene, cell_x, cell_y, *groups, shoot_period=SHOOT_PERIOD):
        super().__init__(scene, cell_x, cell_y, *groups)
        ObjectWithHealth.__init__(self)
        self.extra_width = self.EXTRA_WIDTH
        self.direction_x = DirectionX.LEFT
        self.shoot_period = shoot_period
        self.health_indicator = ObjectHealthIndicator(scene, self)
        self.scene.add_object(self.health_indicator)

    def process_logic(self, events):
        if self.is_dead():
            self.scene.get_object('score').add(self.SCORE)
            self.kill()
        player = self.scene.get_object('player')
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
        
    def kill(self) -> None:
        self.health_indicator.kill()
        super(Turret, self).kill()
