def run():
    # list = []
    # #100 primeros números cuadrados
    # # for i in range(0,100):
    # #     list.append(i**2);
    # # print(list)
    # #NUMEROS CUADRADOS NO DIVISIBLES POR 3
    # for i in range(0,100):
    #     if(i**2 % 3 != 0):
    #         list.append(i**2)
    # print(list)

    squares = [i**2 for i in range(0,100)]
    notdivisible3squares = [i**2 for i in range(0,100) if i % 3 != 0]

    print(squares)
    print(notdivisible3squares)

    number = [i for i in range(1,100000) if (i % 36 == 0 and len(str(i)) < 6)]
    print(number)


if __name__ == '__main__':
    run()