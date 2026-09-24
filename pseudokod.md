```
### Grovplanering

Jag tänkte göra ett spel med en slot machine. Man har lite pengar i början och man kan välja hur mycket man bettar. När man trycker på spin blir det tre symboler/bilder och om de är lika får man en vinst, annars om alla är olika förlorar man det man bettade. Jag tänkte använda pygame.

### Pseudokod

START

SKAPA spelare med startsaldo

SKAPA slot machine

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
        Dra av insatsen från saldot

        SLUMPA tre symboler

        VISA symbolerna

        KONTROLLERA resultatet


        OM tre lika:
            BERÄKNA vinst
            Lägg til vinsten på saldot
            VISA "Du vann!"

        




```