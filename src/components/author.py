class Author:
    def __init__(self, lastname, firstname = ""):
        self.lastname = lastname
        self.firstname = firstname

    def __str__(self):
        if not self.firstname:
            return self.lastname
        
        return f"{self.lastname}, {self.firstname}"
    
    def apastr(self):
        if not self.firstname:
            return self.lastname
        
        retstr = f"{self.lastname}, "
        namelist = self.firstname.split()
        for n in namelist:
            #n.strip()
            retstr += n[0] + ". "
        
        return retstr.strip()
    
    def list_first_names(self):
        return self.firstname.split()