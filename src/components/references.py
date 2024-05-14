from .ref import Ref
import toml

class References:
    def __init__(self):
        self.references = []
        #TODO lisaa read_toml_file methodi

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

    def is_key_taken(self, bibtexkey):
        for r in self.references:
            if bibtexkey == r.bibtexkey:
                return True
        return False

    def generate_toml_str(self):
        if len(self.references) == 0:
            return ""
        toml_string = ""
        for i in self.references:
            toml_string += i.ref_generate_toml_str()
        return toml_string

    def generate_toml_file(self, toml_string):
        with open("references.toml", "w", encoding="utf-8") as file:
            file.write(toml_string)

    def read_toml_file(self):
        with open("references.toml", "r", encoding="utf-8") as file:
            data = toml.load(file)

        #TODO luo ref olioita datasta 