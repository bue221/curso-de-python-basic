def run():
    # dic = {i: (i**2) for i in range(0,100)}
    # print(dic)
    dic = {i: (round(i**0.5,4)) for i in range(0,1000)}
    print(dic)

if __name__ == '__main__':
    run()