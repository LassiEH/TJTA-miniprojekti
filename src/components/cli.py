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
        while True:
            print()
            print("OHTU ohjelma")
            print("Valitse:")
            print("Lisää lähde [1]")
            print("Poista lähde [2]")
            print("Tulosta lähteet [3]")
            print("Generoi BibTeX-tiedosto [4]")
            print("Ohje [5]")
            print("Tallenna [6]")
            print("Lopeta [7]")
            print()
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
                case "6":
                    return 6
                case "7":
                    return 7
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
        s = "Syöttämällä \"2\" käyttäjä pystyy poistamaan lähteitä."
        print(s + "\n")
        s = "Syöttämällä \"3\" käyttäjä pystyy tulostamaan lähteet."
        print(s + "\n")
        s = "Syöttämällä \"4\" käyttäjä pystyy generoimaan BibTeX-tiedoston."
        print(s + "\n")
        s = "Syöttämällä \"5\" käyttäjä pystyy tulostamaan ohjeet."
        print(s + "\n")
        s = "Syöttämällä \"6\" käyttäjäjä pystyy tallentamaan lähteet."
        print(s + "\n")
        s = "Syöttämällä \"7\" käyttäjä pystyy lopettamaan ohjelman."
        print(s + "\n")

    def generoi_tiedosto(self):
        """
            Funktio, joka generoi tiedoston
        """
        toml_string = self.references.generate_toml_str()
        self.references.generate_toml_file(toml_string)

    def generoi_bib_tiedosto(self):
        """
            Funktio, joka generoi bib-tiedoston
        """
        bib_string = self.references.generate_bib_str()
        self.references.generate_bib_file(bib_string)

    def poista_lahde(self):
        index = 0
        while True:
            print()
            print()
            print("Valitse lähde, jonka haluat poistaa.")
            print()
            ids = self.references.get_references_ids()
            if (len(ids) == 0):
                print("Ei lähteitä")
            for i, ref in enumerate(ids):
                if i == index:
                    print(">   ", ref)
                else:
                    print("    ", ref)

            print()
            print()
            print(" liiku alas [j]   liiku ylös [k]   poista lähde [d]  poistu [q]")
            user_input = input()
            if (user_input == "q"):

                return
            if (user_input == "k"):
                index -= 1
                index = max(index, 0)
                continue

            if (user_input == "j"):
                index += 1
                index = min(index, len(ids)-1)
                continue

            if (user_input == "d"):
                print()
                print("Halutatko poistaa ", ids[index] , "?")
                print("[k]yllä [e]i")
                user_input = input()
                if (user_input == "k"):
                    self.references.remove_ref(ids[index])
                if (user_input == "e"):
                    continue

                
            

    def kaynnista(self):
        """
            Funktio, jolla käynnistetään ohjelma
        """
        while True:
            vastaus = self.aloitus()
            if vastaus == 1:
                self.lisaa_lahde()
            if vastaus == 2:
                self.poista_lahde()
            if vastaus == 3:
                self.tulosta_lahde()
            if vastaus == 4:
                self.generoi_tiedosto()
            if vastaus == 5:
                self.tulosta_ohje()
            if vastaus == 6:
                self.generoi_tiedosto()
            if vastaus == 7:
                print("Kiitos ohjelman käytöstä")
                return
