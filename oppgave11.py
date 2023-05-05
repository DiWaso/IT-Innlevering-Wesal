import csv
import matplotlib.pyplot as plt

filnavn = "oppgave11.csv" # Importerer filen

def Oversikt(filnavn):
    with open(filnavn, encoding = "utf-8-sig") as fil: # Åpner filen med utf-8 tegnsetting. Gir oss tilgang til alle bokstaver, inkludert æøå

        filinnhold = csv.reader(fil, delimiter = ";") # Splitter linjene mellom vært semikolon i filen
        overskrifter = next(filinnhold) # Lar oss hoppe over overskriftene, men lagrer dem også inne i denne variabelen

        # En tom ordbok for å holde oversikt på hvor mye som har blitt brukt på hva de tre månedene
        oversikt_mnd = {}
        total_mat = []    # En tom liste for å legge til alle prisene for mat
        total_strøm = []  # En tom liste for å legge til alle prisene for strøm

        for i in filinnhold:   # Leser gjennom filene. Vær linje i filen vil nå være en liste siden vi splittet dem mellom vært semikolon
            dato = i[0].split(".")    # Splitter datoen opp i en liste mellom vært punktum så vi får tre verdier i listen: dag, måned, år
            if str(dato[1]) not in oversikt_mnd.keys():    # Skjekker om måneden ikke er en nøkkel i ordboken
                oversikt_mnd[str(dato[1])] = {}    # Hvis ja, legger den til måneden som en nøkkel med en tom ordbok som sinn verdi
            if str(dato[1]) in oversikt_mnd.keys():    # Skjekker om måneden er en nøkkel i ordboken
                if str(i[1]) in oversikt_mnd[str(dato[1])].keys():   # Hvis ja, skjekkes det her om "mat" eller "strøm" er en nøkkel i den ordboken som er verdien til måneden
                    oversikt_mnd[str(dato[1])][str(i[1])].append(float(i[2]))   # Hvis ja, legges det til en verdi inn i listen som er verdien til enten "mat" eller "strøm"
                if str(i[1]) not in oversikt_mnd[str(dato[1])].keys():    # Hvis nei, lages det en ny nøkkel som heter "mat" eller "strøm" som inneholder en liste med tall som sinn verdi
                    oversikt_mnd[str(dato[1])][str(i[1])] = [float(i[2])]

        for i in oversikt_mnd.values():   # Går gjennom verdiene til de forskjellige måneds nøkkelene i ordboken
            for key, value in i.items():  # Går gjennom de forskjellige nøkkelene i ordboken som er verdiene til de forskjellige måneds nøkkelene
                if key == "mat":    # Skjekker om nøkkelen er "mat"
                    for j in value: # Hvis ja, går den gjennom alle tallene i listen som er verdien til nøkkelen "mat" og legger dem inn i listen total_mat
                        total_mat.append(j)
                if key == "strøm":  # Skjekker om nøkkelen er "strøm"
                    for j in value: # Hvis ja, går den gjennom alle tallene i listen som er verdien til nøkkelen "strøm" og legger dem inn i listen total_strøm
                        total_strøm.append(j)
        
        return (oversikt_mnd, total_mat, total_strøm)

# Oppgave 11A            
# Bruker formaterte strings til å printe ut melding for mat, strøm, og hvor mye de brukte på alt.
print(f"De har brukt totalt {sum(Oversikt(filnavn)[1])}kr på mat.")
print(f"De har brukt totalt {sum(Oversikt(filnavn)[2])}kr på strøm.")
print(f"De har brukt totalt {sum(Oversikt(filnavn)[1]) + sum(Oversikt(filnavn)[2])}kr på alt.")

# Oppgave 11B
summer = 0

for key_1, value_1 in Oversikt(filnavn)[0].items(): # Henter måned nøkkelen og ordboken som tilhører til den nøkkelen (verdien til nøkkelen)
    for value_2 in value_1.values():   # Går gjennom ordboken som er verdien til måned nøkkelen og henter ut alle betalingene fra den måneden
        summer += sum(value_2)    # Summerer alt sammen for den måneden den er på
    print(f"Måned {key_1}: {summer}kr")   # Printer ut hvor mye som ble brukt den måneden
    summer = 0    # Setter summen tilbake til 0 og går til neste måned

# Oppgave 11C
måned_nmr = []
summert_pris = []
summer = 0

# Samme løkke som løkken ovenfor
for key_1, value_1 in Oversikt(filnavn)[0].items():
    for value_2 in value_1.values():
        summer += sum(value_2)
    summert_pris.append(summer) # Legger til summerte prisen i en liste
    måned_nmr.append(key_1)     # Legger til måneds nummeret i en liste
    summer = 0
    
måned_nmr.reverse()   # Snur listen om så vi får måned 1 til 3 og ikke 3 til 1
summert_pris.reverse()   # Snur listen om så summene er riktig med månedene
plt.bar(måned_nmr, summert_pris, zorder=2)    # Lager stolpe diagremmet
plt.title("Oversikt over hva familien Rosendal bruker på mat og strøm (totalt)")    # Setter tittel
plt.xlabel("Måned nummer")   # Setter navn på x-aksen
plt.ylabel("Totalt mat og strøm beløp i Kr")    # Setter navn på y-aksen
plt.grid(axis = "y", zorder=1)    # Tegner linjer bak stolpene

# Oppgave 11D
def leggTilPost(filnavn):
    with open(filnavn, "a") as fil:
        tekst_liste = []
        tekst_string = ""
        
        dato = tekst_liste.append(input("Skriv datoen i formen dd.mm.åååå: "))
        gruppe = tekst_liste.append(input("Skriv om det er mat eller strøm: "))
        beløp = tekst_liste.append(input("Skriv beløpet: "))
        betalt_til = tekst_liste.append(input("Skriv hvem beløpet har blitt betalt til: "))
        
        for i in tekst_liste: # Går gjennom listen hvor alle inputtene har blitt lagt til
            if i == tekst_liste[-1]: # Skjekker om i er lik den siste inputten
                tekst_string += f"{i}" # Hvis ja, så skriver den den siste inputten uten semikolon (;) på slutten
                break # Går ut av løkken
            tekst_string += f"{i};" # Legger til de andre inputtene med semikolon på slutten
        
        fil.write(f"{tekst_string}\n") # Legger til teksten nederst på filen med ett linjeskifte på slutten

leggTilPost(filnavn)