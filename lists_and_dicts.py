def run():
    my_list = [1, "hello", True,4.5]
    my_dic = {"firtsName": 'Andres', "lastName": 'Plaza'}

    super_list = [
        {"firtsName": 'Andres', "lastName": 'Plaza'},
        {"firtsName": 'Camilo', "lastName": 'Jiménez'},
        {"firtsName": 'Isabel', "lastName": 'Jiménez'},
        {"firtsName": 'Juan', "lastName": 'Plaza'}
    ]

    super_dic = {
        "natural_nums" : [1,2,3,4,5],
        "integer_num": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dic.items():
        print(key," ",value)

    for i in super_list:
        for key, value in i.items():
            print(key,":", value)


if __name__ == '__main__':
    run()