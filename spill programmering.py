a = input("Hvilke superkrefter vil du ha? Vil du kunne skyte flammer eller være superrask?")
if a == "skyte flammer":
    print("Bra valg!Du vil ikke angre. Gjørr deg klar for å starte nå!")
    c = input("Du skal prøve å bekjempe en fiende som ingen har greid å bekjempe før! Vil du angripe med en gang eller vente å se hva fienden din gjør?")
    if c == "angripe med en gang":
        print("Du skjøt tre flammer, men kun en traff fienden!Den ene flammen traff fienden rett i magen, den ser litt skadet ut!Supert valg!!!")
        g = input("Du har sjansen til å drepe fienden din! Hvoran velger du å gjøre det? Skyte flere flammer eller ta hammeren den har i hånden og bruke den?")
        if g == "skyte flere flammer":
            print("FANTASTISK! Du drepte den! Gratulerer!")
        elif g == "bruke hammeren":
            print("GRATULERER du drepte fienden din!!!")
    elif c == "vente å se hva fienden min gjør":
        print("oioi! Det var ikke lurt, fienden din slo deg hardt i den ene armen. Du kan ikke lenger bruke den til å skyte flammer!!!")
        d = input("Fienden har en hammer som den svinger mot deg! Hva gjør du? Prøver du å dukke eller skrike så høyt du kan etter hjelp?")
        if d == "dukke":
            print("Du kom deg så vidt unna hammeren!! Fantastisk!")
            e = input("Fienden er sliten og du har endelig muligheten til å ende dette! Velger du å bruke den andre hånden for å skyte flammer eller komme deg unna?")
            if e == "skyte flammer":
                print("WOW! Du traff rett i hjertet og drepte den uovervinnelige fienden!!! Gratulerer!")
            elif e == "komme meg unna":
                print("ÅNEI! Du var ikke rask nok! Fienden drepte deg.GAME OVER!")
        elif d == "skrike så høyt jeg kan etter hjelp":
            print("Det var dessverre ingen som hørte det og du ble drept av fienden!GAME OVER!")
elif a == "superrask":
    print("Supert valg!Du vil ikke angre.Gjør deg klar til å starte")
    f = input("Du møter verdens raskeste mann, Usain Bolt. Dere skal løpe om kapp! Siden du har superkrefter er det urettferdig, velger du å vinne eller tape med vilje?")
    if f == "vinne":
        print("Du ble tatt for doping! TAPER!!!")
    elif f == "tape med vilje":
        print("Godt valg! Du er en bra person!!")
        

    





    
    
        
        
    