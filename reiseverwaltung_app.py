from datetime import datetime, timedelta
from premium_reise import PremiumReise
from storno_algorithmen import KulanterStornoAlgorithmus


def main():
    reise_datum = datetime.now() + timedelta(days=30)
    premium_reise = PremiumReise(reise_datum, 1000.0)

    premium_reise.set_storno_algorithmus(KulanterStornoAlgorithmus())
    stornogebuehr = premium_reise.execute_storno_berechnen()
    print(f"Die Stornogebühr für die PremiumReise beträgt: {stornogebuehr}")


if __name__ == "__main__":
    main()
