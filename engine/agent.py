from typeguard import typechecked


class Agent:
    @typechecked
    def __init__(self, name: str) -> None:
        self.name = name
