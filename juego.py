import random

def jugarVariasVeces(n):
    vecesGanaJuan = 0
    vecesGanaMaria = 0
    vecesEmpatan = 0
    for i in range(n):
        ganador = simularJuego()
        if ganador == "Juan":
            vecesGanaJuan += 1
        elif ganador == "Maria":
            vecesGanaMaria += 1
        elif ganador == "Empate":
            vecesEmpatan += 1
    
    return f"Al jugar {n} veces: \nJuan ganó {vecesGanaJuan} veces \nMaria ganó {vecesGanaMaria} veces \n{vecesEmpatan} veces empataron"      

def simularJuego():
    puntajeJuan = juegaJuan()
    puntajeMaria = juegaMaria(puntajeJuan)
    if puntajeJuan > puntajeMaria:
        return "Juan"
    elif puntajeJuan < puntajeMaria:
        return "Maria"
    else:
        return "Empate"
    
def juegaJuan():
    puntaje = tirarDados()
    if puntaje == 0:
        return tirarDados()
    elif puntaje <= 3:
        return  tirarUnDado()
    return puntaje

def juegaMaria(puntajeJuan):
    puntaje = tirarDados()
    if puntaje == 0:
        return tirarDados()
    elif puntaje < puntajeJuan and puntaje > 0:
        return tirarUnDado()
    return puntaje

def tirarDados():
    dados = [random.randint(1, 6), random.randint(1,6)]
    if dados[0] == 4:
        return dados[1]
    elif dados[1] == 4:
        return dados[0]
    else:
        return 0
    
def tirarUnDado():
    return random.randint(1, 6)