COSTI = {
    "corsa_semplice": 11.20,  # una corsa è 5.60 €
    "settimanale": 32.20,
    "mensile":113.50,
    "trimestrale": 308.00,
}

def decisore(viaggi): 
    stati = [0]
    abbonamenti = []

    for i, c in enumerate(viaggi, start=1):
        if c == '.' or not c:
            stati.append(stati[-1])
            continue    
        
        opzioni = []
        scelte  = ["biglietto", "settimanale", "mensile", "trimestrale"]
        
        opzioni.append(stati[i - 1] + COSTI["corsa_semplice"])

        if i >= 7:
            opzioni.append(stati[i - 7] + COSTI["settimanale"])
        else:
            opzioni.append(COSTI["settimanale"])
        
        if i >= 30:
            opzioni.append(stati[i - 30] + COSTI["mensile"])
        else:
            opzioni.append(COSTI["mensile"])

        if i >= 90:
            opzioni.append(stati[i - 90] + COSTI["trimestrale"])
        else:
            opzioni.append(COSTI["trimestrale"])

        minimo = min(opzioni)
        scelta = str(f"giorno {i} ") + scelte[opzioni.index(minimo)]

        stati.append(minimo)
        abbonamenti.append(scelta)


    print(f"La spesa minima è di {round(stati[-1], 2)} €")
    print(f"Gli abbonamenti da comprare sono: ")
    for a in abbonamenti:
        print(a)


if __name__ == "__main__":
    viaggio = input(". per i giorni in cui non si viaggia e 1 per il viaggio: ")
    decisore(viaggio)
