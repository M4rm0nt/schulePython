from reise import Reise


class PremiumReise(Reise):
    def __init__(self, reise_beginn, grund_preis):
        super().__init__(reise_beginn, grund_preis)

    def preis_berechnen(self):
        pass
