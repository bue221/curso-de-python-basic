def read():
    numbers = []
    with open("./archivos/number.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))

def write():
    names = ['Andres','Camilo', 'Plaza', 'Jimenez']
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    pass

if __name__ == '__main__':
    run()