import toml
from .author import Author

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
        for i, auth in sorted(enumerate(self.author), key=str):
            s += auth.apastr()
            if i < len(self.author) - 1:
                s += ", & "
            else:
                s += " "
        # Muodostetaan vuosi osa
        s += f"({self.bibdata.get("year", "n.d.")}). "

        # Muodostetaan otsikko osa
        s += f"{self.bibdata.get("title", "")}"

        tempstr = f"{self.bibdata.get("booktitle", "")}"
        if tempstr:
            s += ", "
        s += tempstr

        tempstr = f"{self.bibdata.get("volume", "")}"
        if tempstr:
            s += ", "
        s += tempstr

        tempstr = f"{self.bibdata.get("pages", "")}"
        if tempstr:
            s += ", "
        s += tempstr + f"."

        return s

    def bibtexstr(self):
        s = f"@{self.artype}{{{self.bibtexkey},\n  author={{"
        for i, auth in enumerate(self.author):
            s += auth.bibtexstr()
            if (i < len(self.author) - 1):
                s += " and "
        s += "}"
        for i, (key, value) in enumerate(self.bibdata.items()):
            s += f",\n  {key}={{{value}}}"
        s += "\n}"

        return s

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
