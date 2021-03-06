# komentowanie : Ctrl+1
# run all : F5
# run line : F9
# run : Ctrl + Enter

print('Hello world!')


# DODAWANIE

def dodawanie(l1, l2):
    wynik = l1 + l2
    return wynik

w1 = dodawanie(10, 9)

print(w1)


# ODEJMOWANIE

def odejmowanie(l1, l2):
    wynik = l1 - l2
    return wynik

w2 = odejmowanie(10, 9)

print(w2)


# PETLA WHILE 

c = 0
while(c < 10): 
    print(c)
    c = c + 1
print('koniec')


# PETLA FOR

owoce = ['banan', 'gruszka', 'kiwi']

for owoc in owoce:
    print(owoc)
    
for index in range(len(owoce)):
    a = owoce[index]
    print(a, index)
    
print(f'Tu jest taki owoc jak {a}')


# FORMATOWANIE TEKSTU

print('To zdanie pojawi się w pierwszej linii. \nKolejne zdanie w nowej. \n\tNastępne będzie przesunięte.')


# FORMATOWANIE DATY

from datetime import datetime

now = datetime.now()
# 2020-01-01 00:00
format1 = now.strftime('%Y-%m-%d %H:%M:%S')


# FUNKCJA INPUT

def przedstaw_sie():
    imie = input('Podaj imie: ')
    nazwisko = input('Podaj nazwisko: ')
    print(f'Nazywasz sie {nazwisko} {imie}')

przedstaw_sie()


# WIZYTOWKA

def wizytowka():
    imie = input('Podaj imie: ')
    wiek = input('Podaj wiek: ')
    miasto = input('Podaj miasto: ')
    print(f'Imie: {imie} \nWiek: {wiek} \nMiasto: {miasto}')

wizytowka()