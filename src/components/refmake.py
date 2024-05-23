from .ref import Ref
from .references import References
from .author import Author

#TODO: Harkitse templatejen siirtämistä toisaalle
#Template -luokan avulla templateihin voisi lisätä kentille erilliset suomenkieliset nimet,
#helposti laajennettavia regex-tarkistuksia ja erityisiä tulostusformatoijia
templates = dict({
"article": ["title", "journal", "year", "volume", "pages"],
"inproceedings": ["title", "booktitle", "year", "volume", "pages", "publisher"]
})

def ref_query(references : References, ref_type: str):
    if not templates.get(ref_type, ""):
        print("Virheellinen viitetyyppi.")
        return None

    bibdata = {}

    print("Syötä kirjoittajat:")
    authlist = []
    while True:
        print("Sukunimi \033[96m(jätä tyhjäksi lopettaaksesi)\033[0m:")
        laststr = input("> ")
        if not laststr:
            break
        print("Etunimi tai nimet (valinnainen):")
        firststr = input("> ")
        authlist.append(Author(laststr, firststr))
    
    for i, field in enumerate(templates.get(ref_type)):
        print(f"Syötä {field}:")
        bibdata[field] = input("> ").strip()
    
    keystr = ""
    while True:
        print("Syötä tunniste:")
        keystr = input("> ").strip()
        if not keystr or references.is_key_taken(keystr):
            print("Lähde, jolla on sama tunniste on jo lisätty tai syöttämäsi tunniste oli tyhjä!")
            continue
        break
    print("Syötä omat avainsanat pilkulla eroteltuna:")
    usrkeystr = input("> ")
    # Testataan, että käyttäjän syöte ei ole tyhjä tai ettei se sisällä vain whitespacea.
    if not (len(usrkeystr) == 0 or usrkeystr.isspace()):
        usrkeylist = usrkeystr.split(',')
    # Jos käyttäjä ei anna sopivaa syötettä, usrkeylistin arvoksi tulee tyhjä.
    else:
        usrkeylist = ""

    return Ref(ref_type, keystr, authlist, bibdata, usrkeylist)