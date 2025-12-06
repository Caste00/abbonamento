COSTI = {
    "biglietto": 11.20,  # una corsa è 5.60 €
    "settimanale": 32.20,
    "mensile":113.50,
    "trimestrale": 308.00,
}

DURATA = {
    "biglietto": 1,
    "settimanale": 7,
    "mensile": 30,
    "trimestrale": 90,
}

# potrebbe avere senso una funzione get_next_day, così da gestire in un altra funzione il formato di viaggi
def decisore(viaggi): 
    n = len(viaggi)
    stati = [0] * (n + 1)   
    scelta = [None] * (n + 1)
    
    for i, c in enumerate(viaggi, 1): 
        if (c == '.' or not c):
            stati[i] = stati[i - 1]
            scelta[i] = "Nessuno"
            continue
        
        opzioni = []        
        for tipo in COSTI.keys():
            durata = DURATA[tipo]
            costo = COSTI[tipo]
            if i >= durata:
                totale = stati[i - durata] + costo
            else:
                totale = costo
            opzioni.append((totale, tipo))
            
        costo_minimo, tipo_minimo = min(opzioni, key=lambda x: x[0])
        stati[i] = costo_minimo
        scelta[i] = tipo_minimo
        
    print(f"La spesa minima è di {round(stati[-1],2)} €")
    
    # Ricostruzione degli abbonamenti
    abbonamenti = []
    i = n
    while i > 0:
        tipo = scelta[i]
        if tipo and tipo != "Nessuno":
            abbonamenti.append((i - DURATA[tipo] + 1, i, tipo))
            i -= DURATA[tipo]
        else:
            i -= 1
            
    return stati[-1], abbonamenti