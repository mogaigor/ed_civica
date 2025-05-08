parole_sospette = {
    "scioccante": -3,
    "incredibile": -2,
    "rivoluzionario": -2,
    "miracoloso": -3,
    "conspirazione": -3,
    "censurato": -2,
    "scandalo": -2,
    "shock": -2,
    "svelato": -2,
    "segreti": -2,
    "bugia": -3,
    "cover-up": -3,
    "fake": -3,    
    "manipolazione": -3,
    "truffa": -3
}

parole_rassicuranti = {
    "studio": 2,
    "ricerca": 2,
    "dati": 2,
    "ufficiale": 2,
    "verificato": 3,
    "esperto": 2,
    "scienziato": 2,
    "università": 2,
    "peer-reviewed": 3,
    "fonte": 2,
    "attendibile": 3,
    "confermato": 2,
    "evidenza": 2,
    "statistiche": 2,
    "analisi": 2
}

punteggio = 0

while True:
    x = input("Scrivi il tuo messaggio (o 'exit' per uscire): ").lower()
    if x == "exit":
        print(f"Punteggio finale: {punteggio}")
        break
    
    parole = x.split()

    for parola in parole:
        if parola in parole_sospette:
            punteggio += parole_sospette[parola]
        elif parola in parole_rassicuranti:
            punteggio += parole_rassicuranti[parola]

    print(f"Punteggio attuale: {punteggio}")