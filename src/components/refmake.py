from .ref import Ref
from .references import References
from .author import Author

#def mkArticle(bibkey, title, journal, year, vol, authlist)

#TODO: Hyödynnä tässä dependency injectionia
def appArticle(references : References, ref_type: str):
    print("Syötä kirjoittajat:")
    authlist = []
    while True:
        print("Sukunimi (jätä tyhjäksi lopettaaksesi):")
        laststr = input("> ")
        if not laststr:
            break
        print("Etunimi tai nimet (valinnainen):")
        firststr = input("> ")
        authlist.append(Author(laststr, firststr))
    print("Syötä otsikko:")
    titlestr = input("> ")
    print("Syötä vuosi:")
    yearstr = input("> ")
    print("Syötä osa (volume):")
    volstr = input("> ")
    print("Syötä sivut viivalla eroteltuna:")
    pagestr = input("> ")
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

    if ref_type == "article":
        print("Syötä julkaisu:")
        jourstr = input("> ")
        return Ref(authlist, titlestr, yearstr, volstr, pagestr, usrkeylist, keystr, journal = jourstr)
    if ref_type == "inproceedings":
        print("Syötä konferenssijulkaisun nimi:")
        conf_name = input("> ")
        print("Syötä sijainti:")
        location = input("> ")
        print("Syötä organisaatio:")
        organization = input("> ")
        print("Syötä julkaisija:")
        publisher = input("> ")
        return Ref(authlist, titlestr, yearstr, volstr, pagestr, usrkeylist, keystr, conf_name=conf_name, location=location, organization=organization, publisher=publisher)
    else:
        print("Virheellinen viitetyyppi.")
        return None