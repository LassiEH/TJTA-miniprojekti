import os.path
import toml
from .ref import Ref
from .author import Author

class References:
    def __init__(self):
        self.references = []
        self.read_toml_file()


    def get_references_ids(self) -> list:
        ids = []
        for ref in self.references:
            ids.append(ref.bibtexkey)
        return ids

    def stringify(self, fnc):
        s = ""
        if len(self.references) == 0:
            return "Lähteitä ei ole."
        for i, ref in enumerate(self.references):
            if i < len(self.references)-1:
                s += fnc(ref) +"\n\n"
            else:
                s += fnc(ref)
        return s

    def __str__(self):
        return self.stringify(str)
    
    def apastr(self):
        return self.stringify(lambda Ref: Ref.apastr())
    
    def bibtexstr(self):
        return self.stringify(lambda Ref: Ref.bibtexstr())

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
        toml_string = ""
        if len(self.references) == 0:
            return toml_string
        for i in self.references:
            toml_string += i.ref_generate_toml_str()
        return toml_string

    def generate_bib_str(self):
        bib_string = ""
        if len(self.references) == 0:
            return bib_string
        for i in self.references:
            bib_string += i.bibtexstr() +"\n\n"
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
            file = open('references.toml', 'w', encoding="utf-8")
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