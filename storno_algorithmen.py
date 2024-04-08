class StornoAlgorithmus:
    def storno_berechnen(self, reise):
        raise NotImplementedError


class KulanterStornoAlgorithmus(StornoAlgorithmus):
    def storno_berechnen(self, reise):
        from premium_reise import PremiumReise
        from standard_reise import StandardReise

        if isinstance(reise, StandardReise):
            return reise.grund_preis * 0.25
        elif isinstance(reise, PremiumReise):
            return reise.grund_preis * 0.10
        else:
            return reise.grund_preis


class StrengerStornoAlgorithmus(StornoAlgorithmus):
    def storno_berechnen(self, reise):
        return reise.grund_preis * 0.50
