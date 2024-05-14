from .author import Author
import toml

class Ref:
    def __init__(self, artype, bibtexkey, author: list, bibdata: dict, userkeys: list):
        self.artype = artype
        self.bibtexkey = bibtexkey
        self.author = author
        self.bibdata = bibdata
        self.userkeys = userkeys
    
    #Saattaa olla hyödyllinen
    def get_field(self, field_name):
        return self.bibdata.get(field_name, "")

    def __str__(self):
        s = f"{self.artype} ({self.bibtexkey})\n"
        for i, auth in enumerate(self.author):
            s += str(auth)
            if (i < len(self.author) - 1):
                s += ", "
            else:
                s += ". "
        
        for i, (key, value) in enumerate(self.bibdata.items()):
            s += f"\n{key}: {value}"
        s += "\n"
        
        return s
    
    def apastr(self):
        s = ""
        for i, auth in enumerate(self.author):
            s += auth.apastr()
            if (i < len(self.author) - 1):
                s += ", & "
            else:
                s += " "
        # Muodostetaan vuosi osa
        s += f"({self.bibdata.get("year", "n.d.")}). "

        # Muodostetaan otsikko osa
        s += f"{self.bibdata.get("title", "")}, "
        
        s += f"{self.bibdata.get("booktitle", "")}, "
        
        s += f"{self.bibdata.get("volume", "")}, "
        
        s += f"{self.bibdata.get("pages", "")}."
        
        return s
    
    # BibTex tynkä
    def bibtexstr(self):
        pass
        

        # Käsitellään eri viitetyypit
        #if hasattr(self, 'journal'):
            # Artikkeli
        #    journal_str = f"{self.journal}, {self.volume}: {self.pages}."
        #    return s + year_str + title_str + journal_str
        #elif hasattr(self, 'conf_name'):
            # inproceedigns
        #    conf_str = f"{self.conf_name}, volume {self.volume}, pages {self.pages}, {self.location}, {self.organization}, {self.publisher}."
        #    return s + year_str + title_str + conf_str
        #else:
        #    return "Unsupported reference type"

    def ref_generate_toml_str(self):
        toml_str = ""
        toml_str += "[" + str(self.bibtexkey) + "]\n"
        toml_str += "artype = \"" + str(self.artype) + "\"\n"
        author_str = []
        for i in self.author:
            author_str.append(str(i))
        toml_str += toml.dumps({"authors" : author_str})
        toml_str += toml.dumps({"userkeys" : self.userkeys})
        toml_str += toml.dumps(self.bibdata)
        toml_str += "\n"
        return toml_str
