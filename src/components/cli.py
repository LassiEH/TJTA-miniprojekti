from .refmake import *

class Cli:
    """
        komentorivi pohjainen käyttöliittymä ohjelmalle
    """

    def __init__(self, lahteet):
        self.references = lahteet


    def aloitus(self):
        """
            ui aloitus ruutu
        """
        print("OHTU ohjelma")
        print("Valitse:")
        print("Lisää lähde [1]")
        print("Tulosta lähteet [2]")
        print("Generoi BibTeX-tiedosto [3]")
        print("Ohje [4]")
        print("Lopeta [5]")
        while True:
            i = input()
            match i:
                case "1":
                    return 1
                case "2":
                    return 2
                case "3":
                    return 3
                case "4":
                    return 4
                case "5":
                    return 5
                case _:
                    continue

    def lisaa_lahde(self):
        """
            Funktio, joka huolehtii lähteen lisäämisestä
            esim. kysyy inputteja 
            toteutetaan oliona lähteen lisäys tiedostoon
        """
        
        print("Syötä viitteen tyyppi (article tai inproceedings)")
        reftype = input("> ")
        ref = ref_query(self.references, reftype)
        if not ref is None:
            self.references.lisaaLahde(ref)

    def tulosta_lahde(self):
        """
            Funktio, jolla tulostetaan lähteet terminaaliin
        """
        print("Valitse tulostusmuoto:")
        print("Näytä lähteet ja BibTex-tietueet [1]")
        print("Näytä lähteet APA-formaatissa [2]")
        i = input()
        match i:
            case "1":
                print("\n"+ self.references.toString() + "\n") #TODO: paranneltu tulostaminen
            case "2":
                print("\n"+ self.references.apastr() + "\n")
            case _:
                print("\n")

    def tulosta_ohje(self):
        """
            Tulostaa ohjelman käyttöön 
        """
        print("\n")
        print("Ohje")
        print()
        s = "Ohjelman avulla käyttäjä pystyy lisäämään lähteitä järjestälmään ja käyttäjä pystyy genoroimaan BibTeX-tiedoston. Järjestelmä myös listaa tallennetut lähteet."
        print(s + "\n")
        s = "Syöttämällä \"1\" käyttäjä pystyy lisäämään uuden lähteen järjestälmään."
        print(s + "\n")
        s = "Syöttämällä \"2\" käyttäjä pystyy tulostamaan lähteet."
        print(s + "\n")
        s = "Syöttämällä \"3\" käyttäjä pystyy generoimaan BibTeX-tiedoston."
        print(s + "\n")
        s = "Syöttämällä \"4\" käyttäjä pystyy tulostamaan ohjeet."
        print(s + "\n")
        s = "Syöttämällä \"5\" käyttäjä pystyy lopettamaan ohjelman."
        print(s + "\n")

    def generoi_tiedosto(self):
        """
            Funktio, joka generoi tiedoston
        """
        print("Ei ole toteutettu" + "\n")
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
                self.generoi_tiedosto()
            if vastaus == 4:
                self.tulosta_ohje()
            if vastaus == 5:
                print("Kiitos ohjelman käytöstä")
                return
