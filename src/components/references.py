class References:
    def __init__(self):
        self.references = []

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

    def lisaaLahde(self, ref):
        self.references.append(ref)