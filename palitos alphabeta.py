import math

INF = 1000000
DEPTH_MAX = 10
MIN_NUM_palitos = 1
MAX_NUM_palitos = 3
num_palitos = 13

def minimax(player, depth, num_palitos, alpha, beta):
    if depth == DEPTH_MAX or num_palitos == 0:
        return 0
    val = -INF
    for i in range(MIN_NUM_palitos, min(MAX_NUM_palitos+1, num_palitos+1)):
        num_palitos -= i
        # Se realiza la recursión con la poda alfa-beta
        tempval = -minimax(1-player, depth+1, num_palitos, -beta, -alpha)
        num_palitos += i
        val = max(val, tempval)
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    return val + 2*player - 1

def tras_juega():
    global num_palitos
    val = -INF
    n = 0
    alpha = -INF
    beta = INF
    for i in range(MIN_NUM_palitos, min(MAX_NUM_palitos+1, num_palitos+1)):
        num_palitos -= i
        # Se realiza la recursión con la poda alfa-beta
        tempval = -minimax(1, 1, num_palitos, -beta, -alpha)
        num_palitos += i
        if tempval > val:
            val = tempval
            n = i
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    num_palitos -= n
    palitos_str = "|" * num_palitos
    print(f"La computadora tomó {n} palitos. Quedan {palitos_str}")

def jugar():
    global num_palitos
    num_palitos = int(input("Ingrese el número inicial de palitos: "))
    palitos_str = "|" * num_palitos
    print(f"Quedan {palitos_str}")
    while num_palitos > 0:
        player_choice = int(input("¿Cuántos palitos quieres tomar? "))
        while player_choice < MIN_NUM_palitos or player_choice > min(MAX_NUM_palitos, num_palitos):
            player_choice = int(input("Esa no es una cantidad válida. ¿Cuántos palitos quieres tomar? "))
        num_palitos -= player_choice
        if num_palitos == 0:
            print("¡Has ganado!")
            break
        tras_juega()
        if num_palitos == 0:
            print("¡La computadora ha ganado!")
            break
        palitos_str = "|" * num_palitos
        print(f"Quedan {palitos_str}")

while True:
    jugar()
    respuesta = input("¿Quieres seguir jugando? (S/N)").lower()
    if respuesta != "s":
        break
