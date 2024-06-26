from datetime import datetime


class Reise:
    def __init__(self, reise_beginn, grund_preis):
        self.grund_preis = grund_preis
        self.reise_beginn = reise_beginn
        self.storno_algorithmus = None

    def preis_berechnen(self):
        pass

    def tage_bestimmen(self):
        pass

    def set_storno_algorithmus(self, alg):
        self.storno_algorithmus = alg

    def execute_storno_berechnen(self):
        if not self.storno_algorithmus:
            raise Exception("StornoAlgorithmus ist nicht gesetzt")
        return self.storno_algorithmus.storno_berechnen(self)
