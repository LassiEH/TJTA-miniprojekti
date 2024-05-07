from .ref import Ref

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
        if not isinstance(ref, Ref):
                return 0
        self.references.append(ref)
        return 1