from components.cli import Cli

class PoweruserUI:

    def __init__(self, lahteet, args : list):
        self.ui = Cli(lahteet)
        self.ohjeet = """
        Käynnistä sovellus antamatta mitään argumentteja tai anna yksi seuraavista argumenteista:\n
        --h   Näytä ohjeet sovelluksen käyttöön\n
        --l   Lisää lähde\n
        --p   Tulostaa lähteet (bibtex tai apa)
        --g   Generoi bibtex tiedosto
        """


        self.references = lahteet
        if len(args) == 2:
            self.actions(args[1])
        else:
            print("\nVirhe: Liian monta argumenttia\n")
            print(self.ohjeet)

    def actions(self, argumentti):
        match argumentti:
            case "--h":
                print(self.ohjeet)
                return
            case "--l":
                self.ui.lisaa_lahde()
                return
            case "--p":
                self.ui.tulosta_lahde()
            case "--b":
                self.ui.generoi_tiedosto()
            case _:
                print(self.ohjeet)
                return
