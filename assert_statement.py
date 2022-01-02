def run():
        num = int(input("Ingresa un numero: "))
        assert num.isnumeric(), "Deebes ingresar un número"
        divisors = lambda num: [i for i in range(1,num+1) if(num % i == 0)]
        esPrimo = False

        if(len(divisors(num)) == 2):
            esPrimo = True

        print(divisors(num),"Es primo: ", esPrimo)

        print('Finalizo el programa')


if __name__ == '__main__':
    run()