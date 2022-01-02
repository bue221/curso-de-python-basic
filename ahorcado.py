import random
import os

DATA = []
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

def readData():
    with open('./archivos/data.txt','r',encoding='utf-8') as f:
        for line in f:
            DATA.append(line)

def replace_at(cadena, idx, char):
  return cadena[:idx] + char + cadena[idx+1:]

def run():
    readData()

    word = ''
    wordAdv = ''
    errors = 0
    randomNumber = random.randint(0, len(DATA))

    for count, value in enumerate(DATA):
        if(count == randomNumber):
            word = value

    totalError = 7
    for i in range(0,len(word)-1):
        wordAdv += '_'

    def printInfo():
        os.system('cls')
        print('---------------Ahorcados Curso de python------------')
        print('Advina la palabra: ')
        print(wordAdv)
        if(errors > 0 ):
            print(AHORCADO[errors])


    while(len(list(filter(lambda i: i == '_',wordAdv))) != 0 and errors < totalError):
        print(errors)
        printInfo();
        letra = input('Ingresa una letra: ')
        notFound = True
        for count, char in enumerate(word):
            if(letra == char):
                wordAdv = replace_at(wordAdv,count,char)
                notFound = False
        if(notFound):
            errors += 1

    if(errors >= totalError):
        print('La palabra era '+word)
    else:
        print('La palabra es '+word+' GANASTE SUPER!!!!')

if __name__ == '__main__':
    run()
