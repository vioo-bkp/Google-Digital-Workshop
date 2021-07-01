class Fractie:
    def __init__(self, numarator: float, numitor: float):
        if numitor == 0:
            raise BaseException('Numitorul nu poate fi 0!')

        self.numarator = numarator
        self.numitor = numitor

    def __str__(self) -> str:
        return f'{self.numarator}/{self.numitor}'

    def __add__(self, other : 'Fractie') -> 'Fractie':
        return Fractie(self.numarator * other.numitor + self.numitor * other.numarator, self.numitor * other.numitor)

    def __sub__(self, other : 'Fractie') -> 'Fractie':
        return Fractie(self.numarator * other.numitor - self.numitor * other.numarator, self.numitor * other.numitor)

    def inverse(self) -> 'Fractie':
        if self.numarator == 0:
            raise BaseException('Fractie invalida (numaratorul e 0)!')
        return Fractie(self.numitor, self.numarator)