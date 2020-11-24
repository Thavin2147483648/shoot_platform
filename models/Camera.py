from constants import Screen, MainCharacter


class Camera:
    def __init__(self, obj, outer_size=(Screen.WIDTH, Screen.HEIGHT)):
        self.x = 0
        self.y = 0
        self.outer_size = outer_size
        self.obj = obj
        self.width = self.outer_size[0]
        self.height = self.outer_size[1]

    # TODO: Write code...
    def update(self):
        rect = self.obj.get_rect()
        self.x = rect.x - (self.outer_size[0] - rect.width) // 2
        self.y = rect.y - (self.outer_size[1] - rect.height) // 2
        self.x = sorted([0, self.x, self.obj.scene.width - self.width])[1]
        self.y = sorted([0, self.y, self.obj.scene.height - self.height])[1]
