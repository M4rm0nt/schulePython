from datetime import datetime, timedelta
from premium_reise import PremiumReise
from standard_reise import StandardReise
from storno_algorithmen import KulanterStornoAlgorithmus
from storno_algorithmen import StrengerStornoAlgorithmus


def main():

    reise_datum = (datetime.now() + timedelta(days=30)).strftime('%d.%m.%Y')

    # KulanterStornoAlgorithmus
    premium_reiseKA = PremiumReise(reise_datum, 1000.0)
    premium_reiseKA.set_storno_algorithmus(KulanterStornoAlgorithmus())
    stornogebuehrPRSA = premium_reiseKA.execute_storno_berechnen()
    print(f"Die Stornogebühr für die PremiumReise am {reise_datum} mit KA beträgt: {stornogebuehrPRSA}")

    standart_reiseKA = StandardReise(reise_datum, 1000.0)
    standart_reiseKA.set_storno_algorithmus(KulanterStornoAlgorithmus())
    stornogebuehrSRKA = standart_reiseKA.execute_storno_berechnen()
    print(f"Die Stornogebühr für die StandartReise am {reise_datum} mit KA beträgt: {stornogebuehrSRKA}")

    # StrengerStornoAlgorithmus
    premium_reiseSA = PremiumReise(reise_datum, 1000.0)
    premium_reiseSA.set_storno_algorithmus(StrengerStornoAlgorithmus())
    stornogebuehrPRSA = premium_reiseSA.execute_storno_berechnen()
    print(f"Die Stornogebühr für die PremiumReise am {reise_datum} mit SA beträgt: {stornogebuehrPRSA}")

    standart_reiseSA = StandardReise(reise_datum, 1000.0)
    standart_reiseSA.set_storno_algorithmus(StrengerStornoAlgorithmus())
    stornogebuehrSRKA = standart_reiseSA.execute_storno_berechnen()
    print(f"Die Stornogebühr für die StandartReise am {reise_datum} mit SA beträgt: {stornogebuehrSRKA}")


if __name__ == "__main__":
    main()
