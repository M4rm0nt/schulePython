from reise import Reise
from storno_algorithmen import KulanterStornoAlgorithmus


class StandardReise(Reise):
    def __init__(self, reise_beginn, grund_preis):
        super().__init__(reise_beginn, grund_preis)
        self.set_storno_algorithmus(KulanterStornoAlgorithmus())

    def preis_berechnen(self):
        pass
