# Oppgave 12A
class Person:
    def __init__(self, navn):
        self.navn = navn
        self.status = False
        self.ektefelle = ""

    # Oppgave 12B
    def visStatus(self):
        if self.status == False:
            print("Jeg er singel.")
        if self.status == True:
            print(f"Jeg er gift med {self.ektefelle}.")
    
    # Oppgave 12C
    def gifteMeg(self, person):
        # Oppgave 12D; Forklaring på hvorfor det ikke fungerer optimalt
        """
        Grunnen til at denne koden ikke fyngerer som den burde er fordi vi ikke skjekker statusen til personen vi vil gifte oss med. Vi skjekker kun om vi er singel eller ikke. For å fikse dette burde koden se sånn her ut:

        def gifteMeg(self, person):
            if self.status == True and person.navn != self.ektefelle:
                print(f"Beklager {person.navn}. Jeg er allerede gift med {self.ektefelle}.")
            if self.status == False and person.status == False:
                self.ektefelle = person.navn
                person.ektefelle = self.navn
                self.status = True
                person.status = True

        Her skjekker vi først om vi er gift og at personen vi gifter oss med ikke er vår ektefelle allerede. Hvis vi er gift og personen vi prøver gifte seg med oss ikke er vår ektefelle printes det ut en beklager melding om at vi allerede er gift.

        Hvis vi er singel og personen vi prøver å gifte oss med er singel så vil den nederste if-setningen aktiveres og vi vil da bli gift.

        """
        if self.status == True:
            print(f"Beklager {person.navn}. Jeg er allerede gift med {self.ektefelle}.")
        else:
            self.ektefelle = person.navn 
            person.ektefelle = self.navn
            self.status = True
            person.status = True

def hovedprogram():
    brad = Person("Brad Pitt")
    brad.visStatus()

    angie = Person("Angelina Jolie")
    brad.gifteMeg(angie)
    brad.visStatus()

    jo = Person("Jo By")
    brad.gifteMeg(jo)
    jo.gifteMeg(brad)
    jo.visStatus()

hovedprogram()