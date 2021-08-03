from __future__ import annotations

from uuid import UUID

from ShapeEngine.entity.base.shape import Shape


class Cuboid(Shape):
    def __init__(self, x: float, y: float, z: float, _id: UUID = None):
        super(Cuboid, self).__init__(_id)
        self._x = x
        self._y = y
        self._z = z
        self._id = id

    def validate(self) -> bool:
        return self._x > 0 and self._y > 0 and self._z > 0

    def get_volume(self) -> float:
        return self._x * self._y * self._z
        

    def to_dict(self) -> dict:
        return {
            'id': self._id,
            'x': self._x,
            'y': self._y,
            'z': self._z
        }
        

    def update(self, cuboid: Cuboid):
        self._x = cuboid._x
        self._y = cuboid._y
        self._z = cuboid._z
        

    @classmethod
    def from_dict(cls, cuboid_dict: dict) -> Cuboid:
        return cls(cuboid_dict.get('x'), cuboid_dict.get('y'), cuboid_dict.get('z'), cuboid_dict.get('id'))
