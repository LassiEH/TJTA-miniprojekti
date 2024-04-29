from .ref import Ref

#def mkArticle(bibkey, title, journal, year, vol, authlist)

#TODO: Hyödynnä tässä dependency injectionia
def appArticle():
    print("Syötä kirjoittajat pilkulla eroteltuna:\n> ")
    authstr = input()
    authlist = authstr.split(',')
    print("Syötä otsikko:\n> ")
    titlestr = input()
    print("Syötä julkaisu:\n> ")
    jourstr = input()
    print("Syötä vuosi:\n> ")
    yearstr = input()
    print("Syötä osa (volume):\n> ")
    volstr = input()
    print("Syötä sivut viivalla eroteltuna:\n> ")
    pagestr = input()
    print("Syötä tunniste:\n> ")
    keystr = input() #Älä tee mitään? Tietotyypistä puuttuu tunniste!
    return Ref(authlist, titlestr, jourstr, yearstr, volstr, pagestr)
