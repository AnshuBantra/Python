class Valut:
    def __init__(self, galleons=0, sickels=0, knuts=0) -> None:
        self.galleons = galleons
        self.sickels = sickels
        self.knuts = knuts

    def __str__(self) -> str:
        return f'galleons={self.galleons}, sickels={self.sickels}, knuts={self.knuts}'

    def __add__(self, other) -> tuple:
        return Valut(   self.galleons+other.galleons,
                        self.sickels+other.sickels,
                        self.knuts+other.knuts
                )

potters = Valut(100,50,25)
print(potters)

weasley = Valut(25,50,100)
print(weasley)

print(potters+weasley)