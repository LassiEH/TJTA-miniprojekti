class Ref:
    def __init__(self, author, title, journal, year, volume, pages, userkeys):
        self.author: list = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.pages = pages
        self.userkeys: list = userkeys

    def __str__(self):
        s = ""
        for i, name in enumerate(self.author):
            s += name
            if (i < len(self.author) - 1):
                s += ", "
            else:
                s += ". "
        return s + self.title + ": " + self.journal + ", " +  str(self.volume) + ". " + str(self.pages) + ", " + str(self.year)
