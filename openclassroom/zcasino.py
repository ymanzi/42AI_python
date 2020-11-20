#!/usr/bin/python2.7

from random import randrange
from math import ceil


def check_int(value):
    try:
        value = int(value)
        assert (value > 0)
    except TypeError:
        print("La saisie n'est pas un nombre: ", value)
    except AssertionError:
        print("La valeur est inferieur ou egale a zero:", value)
    return (value)


def tour_roulette(nbr):
    value = randrange(0, 50)
    if (nbr == value):
        return (1)
    elif ((value % 2) == (nbr % 2)):
        return (2)
    else:
        return (0)

def roulette(money):
    on = True
    while (on):
        print("Nous voila parti pour un nouveau tour de roulette\n")
        bet = input("Quelle est votre mise? :")
        bet = check_int(bet)
        print("Bet=", bet, "money=", money)
        try:
            assert (bet < money)
        except AssertionError:
            print("Vous ne pouvez parier plus que ce que vous possedez.")
        nbr = input("Sur quelle numero (0 - 49) ? :")
        nbr = check_int(nbr)
        ret = tour_roulette(nbr)
        if (ret == 0):
            print("Vous avez perdu votre mise de ", bet, "$");
            money -= bet
        elif (ret == 1):
            print("OUUURRAAAHHH Nous avons la un chanceux. Vous remportez ", 3 * bet, "$")
            money += (3 * bet)
        else:
            print("Ce n'etait pas loin. Vous etes tombes sur la meme couleur. Vous gagnez ", ceil(bet/2), "$")
            money += ceil(bet / 2)
        if (money == 0):
            print("Vous n'avez plus d'argent. C'est termine.")
            on = False
        else:
            on = bool(input("Voulez-vous continuer (True - False)? :"))
            
def zcasino():
    money = input("Combien voulez-vous amener sur la table ?: ")
    try:
        money = int(money)
        assert (money > 0)
    except ValueError:
        print("La saisie n'est pas un nombre.")
    except AssertionError:
        print("La valeur est inferieur ou egale a zero.")
    roulette(money)

zcasino()



