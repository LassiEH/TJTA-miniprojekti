class Cli:
    """
        komentorivi pohjainen käyttöliittymä ohjelmalle
    """

    def __init__(self):
        pass

        
    def aloitus(self):
        """
            ui aloitus ruutu
        """
        print("\n")
        print("OHTU ohjelma")
        print("Valitse:")
        print("Lisää lähde [1]")
        print("Tulosta lähteet [2]")
        print("Lopeta [3]")
        while True:
            i = input()
            match i:
                case "1":
                    return 1
                case "2":
                    return 2
                case "3":
                    return 3
                case _:  
                    continue

    def lisaa_lahde(self):
        """
            Funktio, joka huolehtii lähteen lisäämisestä
            esim. kysyy inputteja 
            toteutetaan oliona lähteen lisäys tiedostoon
        """
        print("\n")
        print("Ei ole toteutettu")

    def tulosta_lahde(self):
        """
            Funktio, jolla tulostetaan lähteet terminaaliin
        """
        print("\n")
        print("Ei ole toteutettu")
       
    def kaynnista(self):
        """
            Funktio, jolla käynnistetään ohjelma
        """
        while True:
            vastaus = self.aloitus()
            if vastaus == 1:
                self.lisaa_lahde()
            if vastaus == 2:
                self.tulosta_lahde()
            if vastaus == 3:
                break