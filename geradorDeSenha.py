import random
import string

def gerandoLetra():

    aleatorio = []
    contador = 0
    while contador < 12:
        aleatorio += random.choices(string.ascii_lowercase)
        contador += 1
    return aleatorio


def gerandoNumeros():

    aleatorio = []
    contador = 0

    while contador < 5:
        aleatorio.append(random.randrange(1, 10))
        contador += 1

    return aleatorio

def geradoCaracteres():

    caracteres = ['.', ',', '/', '?', '|', '!', '^', '%', '$']
    aleatorio = []
    contador = 0

    while contador < 10:
        aleatorio += random.choices(caracteres)
        contador += 1

    return aleatorio


def finalizandoSenha():

    senhajundando = gerandoLetra() + gerandoNumeros() + geradoCaracteres()

    for senha in senhajundando:
        print(f'{senha}', end='')

    return senhajundando


finalizandoSenha()