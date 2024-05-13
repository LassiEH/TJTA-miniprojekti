class Ref:
    def __init__(self, author, title, year, volume, pages, userkeys, bibtexkey, **kwargs):
        self.bibtexkey = bibtexkey
        self.author = author
        self.title = title
        self.year = year
        self.userkeys: list = userkeys
        self.volume = volume
        self.pages = pages
        # Käsitellään lisäparametreja, jotka voivat vaihdella eri viitetyypeille
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        s = ""
        for i, name in enumerate(self.author):
            s += str(name)
            if (i < len(self.author) - 1):
                s += ", "
            else:
                s += ". "
        # Muodostetaan vuosi osa
        year_str = f"({self.year}). "

        # Muodostetaan otsikko osa
        title_str = f"{self.title}. "

        # Käsitellään eri viitetyypit
        if hasattr(self, 'journal'):
            # Artikkeli
            journal_str = f"{self.journal}, {self.volume}: {self.pages}."
            return s + year_str + title_str + journal_str
        elif hasattr(self, 'conf_name'):
            # inproceedigns
            conf_str = f"{self.conf_name}, volume {self.volume}, pages {self.pages}, {self.location}, {self.organization}, {self.publisher}."
            return s + year_str + title_str + conf_str
        else:
            return "Unsupported reference type"
