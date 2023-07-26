"""
classmethod()
@classmethod
factory
"""


class A:
    x = 5
    y = 2

    def __init__(self, a: float) -> None:
        self.a = a


    def add(self, a: int, b: int) -> int:
        return a + b

    @classmethod
    def sub(cls):
        return cls(13)


print(A.sub().__dict__)


