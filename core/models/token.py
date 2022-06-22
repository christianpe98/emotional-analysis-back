class Token:
    def __init__(self, text: str, pos_tag: str = "Unknown"):
        self._text = text
        self._pos_tag = pos_tag

    @property
    def text(self) -> str:
        return self._text

    @property
    def pos_tag(self) -> str:
        return self._pos_tag

    def __repr__(self):
        return str(self.as_dict())

    def __str__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {"text": self.text, "pos_tag": self.pos_tag}

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return (self.text == other.text) & (self.pos_tag == other.pos_tag)
