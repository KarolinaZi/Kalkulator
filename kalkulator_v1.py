import sys
import logging


def kalkulator(calculation_type, first_number, second_number, third_number):
    text = ""
    result = float(0)
    if calculation_type == 1:
        result += float(first_number+second_number+third_number)
        text += "Dodaję liczby: %s , %s, %s\n" %(first_number,second_number, third_number)
    elif calculation_type == 2:
        result = float(first_number-second_number)
        text += "Odejmuję %s od %s\n" %(second_number, first_number)
    elif calculation_type == 3:
        result = float(first_number*second_number*third_number)
        text += "Mnożę liczby: %s , %s, %s\n" %(first_number,second_number, third_number)
    elif calculation_type == 4:
        result = float(first_number/second_number)
        if second_number == 0:
            print("Druga liczba musi być różna od zera!")
            exit(2)
        text += "Dzielę %s przez %s\n" %(first_number,second_number)

    text += "Wynik to: %s" %result
    print(text)


if __name__ == "__main__":
    calculation_type = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

    if calculation_type >= 5:
        print("Podaj liczbę całkowitą z zakresu od 1 do 4.")
        exit(4)
    
    first_number = float(input("Podaj pierwszą liczbę działania: "))
    second_number = float(input("Podaj drugą liczbę działania: "))
    third_number = None
    
    if calculation_type == 1:
        third_number = float(input("Podaj trzecią liczbę działania: "))
    elif calculation_type == 3:
        third_number = float(input("Podaj trzecią liczbę działania: "))
    else:
        pass

    kalkulator(calculation_type, first_number, second_number, third_number)
    



