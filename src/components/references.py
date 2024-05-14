from .ref import Ref
from .author import Author
import toml
import os.path

class References:
    def __init__(self):
        self.references = []
        self.read_toml_file()


    #TODO: Korjaa java-tyyliset funktiokutsut snake_case:ksi ja tämä sisäänrakennettuun __str__-muotoon
    def toString(self):
        s = ""
        if len(self.references) == 0:
            return "Lähteitä ei ole."
        for i, ref in enumerate(self.references):
            if i < len(self.references)-1:
                s += str(ref) +"\n\n"
            else:
                s += str(ref)
        return s
    
    #TODO: vältä toistoa
    def apastr(self):
        s = ""
        if len(self.references) == 0:
            return "Lähteitä ei ole."
        for i, ref in enumerate(self.references):
            if i < len(self.references)-1:
                s += ref.apastr() +"\n\n"
            else:
                s += ref.apastr()
        return s

    #TODO: Käytä hyväsksi is_key_taken metodia ja älä salli saman key:n omaavien lisäystä
    def lisaaLahde(self, ref):
        if not isinstance(ref, Ref):
            return 0
        self.references.append(ref)
        return 1

    #Metodi, joka poistaa references-taulukosta referenssin annetulla bibtexkey:llä
    # *-merkillä saa poistettua kaikki
    # palauttaa 2, jos kaikki poistetaan, 1 jos on poistettu referenssi käyttäjän antamalla bibtexkey:llä
    # palauttaa 0, jos annetulla bibtexkey:llä ei löytynyt referenssiä
    def remove_ref(self, bibtexkey):
        if bibtexkey == "*":
            self.references.clear()
            return 2
        for ref in self.references:
            if ref.bibtexkey == bibtexkey:
                self.references.remove(ref)
                return 1
        return 0

    
    def is_key_taken(self, bibtexkey):
        for r in self.references:
            if bibtexkey == r.bibtexkey:
                return True
        return False

    def generate_toml_str(self):
        if len(self.references) == 0:
            return ""
        toml_string = "Ei tee vielä mitään"
        for i in self.references:
            toml_string += i.bibtexstr()
        return toml_string

    def generate_bib_str(self):
        if len(self.references) == 0:
            return ""
        bib_string = ""
        for i in self.references:
            bib_string += i.ref_generate_bib_str()
        return bib_string
    
    def generate_toml_file(self, toml_string):
        with open("references.toml", "w", encoding="utf-8") as file:
            file.write(toml_string)

    def generate_bibtex_file(self, bibtex_string):
        with open("references.bib", "w", encoding="utf-8") as file:
            file.write(bibtex_string)
    
    def read_toml_file(self):
        #Tarkastaa onko tiedosto olemassa ja luo sellaisen jos ei ole.
        if not os.path.isfile('./references.toml'):
            file = open('references.toml', 'w')
            file.close()
        
        with open("references.toml", "r", encoding="utf-8") as file:
            data = toml.load(file)

        #Viitteitä ei tuoda jos data-dictionary on tyhjä.
        #TODO: Voisi olla omana moduulinaan koodin selkeyttämiseksi.
        if len(data) > 0:
            #Iteroi jokaisen viitteen läpi ja hakee niistä tiedot.    
            for entry_id, entry_info in data.items():
                bibdata = {}
                authorlist = []
                bibtexkey = entry_id
                for key in entry_info:
                    if key == "authors": authlist = entry_info["authors"]
                    elif key == "artype": artype = entry_info["artype"]
                    elif key == "userkeys": userkeys = entry_info["userkeys"]
                    else: bibdata[key] = entry_info[key]
                
                for author in authlist:
                    if ' ' in author: #Tarkastaa, onko välilyönejä ts onko myös etunimi olemassa.
                        lastname, firstname = author.split(' ', 1)
                        authorlist.append(Author(lastname.strip(), firstname.strip())) #Poistetaan leading ja trailing whitespace
                    else: authorlist.append(Author(author))

                self.lisaaLahde(Ref(artype, bibtexkey, authorlist, bibdata, userkeys))