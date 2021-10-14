# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring


class Band:
    list = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.list.append(self)

    def __str__(self):
        return "The band {}".format(self.name)

    def __repr__(self):
        return "Band instance. name={}, members={}".format(self.name, self.members)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.list


class Musician:
    def __init__(self, name, instrument, job, solo):
        self.name = name
        self.instrument = instrument
        self.job = job
        self.solo = solo

    def __str__(self):
        return "My name is {} and I play {}".format(self.name, self.instrument)

    def __repr__(self):
        return "{} instance. Name = {}".format(self.job, self.name)

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar", "Guitarist", "face melting guitar solo")


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass", "Bassist", "bom bom buh bom")


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums", "Drummer", "rattle boom crash")
