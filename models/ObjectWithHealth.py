from models.Float import Float


class ObjectWithHealth:
    HEALTH = 0

    def __init__(self, current=None):
        if current is None:
            current = self.HEALTH
        self._max_health = Float(self.HEALTH)
        self._health = 0
        self.set_health(current)

    def get_max_health(self):
        return Float(self._max_health)

    def get_health(self):
        return Float(self._health)

    def set_health(self, value):
        if Float(0) <= Float(value) <= self.get_max_health():
            self._health = Float(value)
            self.on_health_updated()

    def damage(self, value):
        value = max(Float(0), Float(self.get_health() - value))
        self.set_health(value)

    def on_health_updated(self):
        pass

    def heal(self, value):
        value = min(self.get_max_health(), Float(self.get_health() + value))
        self.set_health(value)

    def is_dead(self):
        return self.get_health() == Float(0)
