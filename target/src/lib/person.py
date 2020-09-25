from uuid import uuid4


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.id_ = uuid4()
        self.name = name
        self.age = age

    def __show__(self) -> str:
        return {
            "id": self.id_,
            "name": self.name,
            "age": self.age,
        }
