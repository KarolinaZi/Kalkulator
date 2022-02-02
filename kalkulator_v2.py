import logging
import math
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')



def addition(first_number,second_number, *args):
    result = float(first_number + second_number + sum(args))
    logger.info(f'Dodaję liczby:{first_number} {second_number} {args}')
    return result

def deduction(first_number,second_number, *args):
    result = float(first_number-second_number)
    logger.info(f'Odejmuję {second_number} od {first_number}')
    if args:
        return NotImplemented
    return result

def multiplication(first_number,second_number, *args):

    result = float(first_number*second_number*math.prod(args))
    logger.info(f'Mnożę liczby:{first_number} {second_number} {args}')
    return result


def division(first_number,second_number, *args):
    result = float(first_number/second_number)
    if second_number == 0:
        print("Druga liczba musi być różna od zera!")
        exit(2)
    logger.info(f'Dzielę {first_number} przez {second_number}')
    if args:
        return NotImplemented
    return result


def get_arguments(operation):
    first_number = float(input("Podaj pierwszą liczbę działania "))
    second_number = float(input("Podaj drugą liczbę działania "))
    args = []
    if operation in [1,3]:
        next_arguments = None
        while True:
            next_arguments = input("Podaj kolejną liczbę działania lub End by zakonczyc: ")
            if next_arguments == "End":
                break
            args.append(float(next_arguments))

    return float(first_number), float(second_number),args


operations = {
1: addition,
2: deduction,
3: multiplication,
4: division
}


def main():
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    first_number,second_number,args = get_arguments(operation)
    result = operations[operation](first_number, second_number, *args)
    
    logger.info(f'Wynik to:{result}')
    return result


if __name__ == "__main__":
    main()