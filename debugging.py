

def run():
    try:
        num = int(input("Ingresa un numero: "))
        
        divisors = lambda num: [i for i in range(1,num+1) if(num % i == 0)]
        esPrimo = False

        if(len(divisors(num)) == 2):
            esPrimo = True

        print(divisors(num),"Es primo: ", esPrimo)

        print('Finalizo el programa')
    except ValueError:
        print('Debes ingresar un numero para que funcione')


if __name__ == '__main__':
    run()