from uuid import uuid4, UUID


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.id_: UUID = uuid4()
        self.name: str = name
        self.age: int = age
