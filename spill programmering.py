a = input("Hvilke superkrefter vil du ha? Vil du kunne skyte flammer eller v�re superrask?")
if a == "skyte flammer":
    print("Bra valg!Du vil ikke angre. Gj�rr deg klar for � starte n�!")
    c = input("Du skal pr�ve � bekjempe en fiende som ingen har greid � bekjempe f�r! Vil du angripe med en gang eller vente � se hva fienden din gj�r?")
    if c == "angripe med en gang":
        print("Du skj�t tre flammer, men kun en traff fienden!Den ene flammen traff fienden rett i magen, den ser litt skadet ut!Supert valg!!!")
        g = input("Du har sjansen til � drepe fienden din! Hvoran velger du � gj�re det? Skyte flere flammer eller ta hammeren den har i h�nden og bruke den?")
        if g == "skyte flere flammer":
            print("FANTASTISK! Du drepte den! Gratulerer!")
        elif g == "bruke hammeren":
            print("GRATULERER du drepte fienden din!!!")
    elif c == "vente � se hva fienden min gj�r":
        print("oioi! Det var ikke lurt, fienden din slo deg hardt i den ene armen. Du kan ikke lenger bruke den til � skyte flammer!!!")
        d = input("Fienden har en hammer som den svinger mot deg! Hva gj�r du? Pr�ver du � dukke eller skrike s� h�yt du kan etter hjelp?")
        if d == "dukke":
            print("Du kom deg s� vidt unna hammeren!! Fantastisk!")
            e = input("Fienden er sliten og du har endelig muligheten til � ende dette! Velger du � bruke den andre h�nden for � skyte flammer eller komme deg unna?")
            if e == "skyte flammer":
                print("WOW! Du traff rett i hjertet og drepte den uovervinnelige fienden!!! Gratulerer!")
            elif e == "komme meg unna":
                print("�NEI! Du var ikke rask nok! Fienden drepte deg.GAME OVER!")
        elif d == "skrike s� h�yt jeg kan etter hjelp":
            print("Det var dessverre ingen som h�rte det og du ble drept av fienden!GAME OVER!")
elif a == "superrask":
    print("Supert valg!Du vil ikke angre.Gj�r deg klar til � starte")
    f = input("Du m�ter verdens raskeste mann, Usain Bolt. Dere skal l�pe om kapp! Siden du har superkrefter er det urettferdig, velger du � vinne eller tape med vilje?")
    if f == "vinne":
        print("Du ble tatt for doping! TAPER!!!")
    elif f == "tape med vilje":
        print("Godt valg! Du er en bra person!!")
        

    





    
    
        
        
    