from core.model.token import Token


class EmotionalToken:
    def __init__(self, token: Token, emotion, association: float = 1):
        self._token = token
        self._emotion = emotion
        self._association = association

    @property
    def token(self):
        return self._token

    @property
    def emotion(self):
        return self._emotion

    @property
    def association(self):
        return self._association

    def __repr__(self):
        return str(self.as_dict())

    def __str__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {'token': self.token.as_dict(), 'emotion': self.emotion, 'association': self.association};

    def __eq__(self, other):
        if not isinstance(other, EmotionalToken):
            return False
        return (self.token == other.token) & (self.emotion == other.emotion) & (self.association == other.association)
