class Ref:
    def __init__(self, author, title, journal, year, volume, pages):
        self.author: list = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.pages = pages

    def __str__(self):
        s = ""
        for i, name in enumerate(self.author):
            s += name
            if (i < len(self.author) - 1):
                s += ", "
            else:
                s += ". "
        return s + self.title + ": " + self.journal + ", " +  self.volume + ". " + self.pages + ", " + str(self.year)
