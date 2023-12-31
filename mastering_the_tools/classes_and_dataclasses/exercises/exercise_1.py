from dataclasses import dataclass, field


@dataclass
class A:
    _length: int = field(init=False, default=0)


@dataclass
class B:
    x: int
    y: str = "hello"
    l: list[int] = field(default_factory=lambda: [])
    # l: list[int] = field(default_factory=list) # does the same thing as above


@dataclass
class C:
    a: int = 3
    b: int = field(init=False)

    def __post_init__(self):
        self.b = self.a + 3
