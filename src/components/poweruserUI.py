class PoweruserUI:
    
    def __init__(self, lahteet, args : list):
        self.ohjeet = """
        Käynnistä sovellus antamatta mitään argumentteja tai anna yksi seuraavista argumenteista:\n
        --h   Näytä ohjeet sovelluksen käyttöön\n
        --l   Lisää lähde\n
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
                self.naytaOhjeet()
                return
            case "--l":
                self.lisaaLahde()
                return
            case _:
                print(self.ohjeet)
                return

    def lisaaLahde(self):
        print("Ei ole toteutettu") 

    def naytaOhjeet(self):
        print(self.ohjeet)
        #TODO paremmat ohjeet sovelluksen käytölle