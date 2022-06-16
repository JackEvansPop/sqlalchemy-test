from typing import TypedDict


class A(TypedDict):
    x: int


assert A.__required_fields__ == frozenset({"x"})
