
### Grovplanering

```

Jag tänkte göra ett spel med en slot machine. Man har lite pengar i början och man kan välja hur mycket man bettar. När man trycker på spin blir det tre symboler/bilder och om de är lika får man en vinst, annars om alla är olika förlorar man det man bettade. Jag tänkte använda pygame.

```

### Pseudokod

```

--Hur klasserna funkar--

KLASS Spelare:
    privat attribut __balance

    MEDTOD show_balance:
        returnera __balance
    
    METOD increase_balance:
        ÖKA __balance med belopp

    METOD reduce_balance:
        MINSKA __balance med belopp
    
    METOD check_balance:
        KONTROLLERAR om man har tillräckligt med pengar
    

KLASS SlotMachine:
    lista med tre "slots"

    METOD spin:
        SLUMPA tre symboler
    
    METOD get_result:
        returnera resultatet

    METOD show_result:
        VISA resultatet


KLASS Symbol:

    METOD get_value:
        returna value


(kommer vara andra namn på symbolerna)

KLASS Symbol1(Symbol):

    METOD get_value:
        returnera value

KLASS Symbol2(Symbol):

    METOD get_value:
        returnera value

KLASS Symbol3(Symbol):

    METOD get_value:
        returnera value



KLASS Spel:
    skapa spelare med startsaldo
    skapa slot machine

    METOD run:
        VISAR saldo
        VISAR "SPIN" knapp
        VISAR skrivfält
        update() och draw() allt

    



--hur spelet funkar--

SKAPA Spel

SÅ LÄNGE spelet körs:

    VISA spelarens saldo

    VISA knappen "SPIN"

    VISA ett fält där man kan skriva det man vill betta


    VÄNTA på att spelaren ska skriva det man vill betta

    VÄNTA på att spelaren ska trycka på "SPIN"


    KONTROLLERA om spelaren har tillräckligt med pengar

    OM spelaren inte har tillräckligt med pengar:
        VISA "Du har inte tillräckligt med pengar"
        
        Spelaren får skriva in ett nytt värde

    ANNARS:

        SLUMPA tre symboler

        VISA symbolerna

        KONTROLLERA resultatet


        OM tre lika:
            BERÄKNA vinst
            Lägg till vinsten på saldot
            VISA "Du vann!"

        ANNARS OM 2 lika:
            BERÄKNA vinst
            Lägg till vinsten på saldot
            VISA "Du vann lite!"

        ANNARS:
            Dra av insatsen från saldot
            VISA "Du förlorade!"
    
    
    OM pengarna är slut:
        VISA "du har inga pengar kvar!"
        Kan inte spela längre
        





```