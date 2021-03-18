---> START


F5 - run all code
F9 - run line of code

Ctrl + 1 - text comment

print("Hello world")


---> ZMIENNE I TYPY


zmienna = 5

int - np. 4 
float - np. 6.5
int + float = float

napis1 = 'witaj'
napis2 = "witaj"
napis 1 == napis2 # zwroci "True"

jeden = 1
dwa = 2
trzy = jeden + dwa
print(trzy)

witaj = "witaj"
swiecie = "swiecie"
witajswiecie = witaj + " " + swiecie


---> TABLICE / LISTY (ARRAY)


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# wypisze kolejno 1, 2, 3
for x in tablica:
    print x


---> PODSTAWOWE OPERATORY


number = 1 + 2 * 3 / 4.0

squared = 7 ** 2 (potegowanie)
cubed = 2 ** 3

helloworld = "hello" + " " + "world"

lotsofhellos = "hello" * 10 - hello written 10 times

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers

print([1,2,3] * 3)
result - [1, 2, 3, 1, 2, 3, 1, 2, 3]


---> FORMATOWANIE NAPISÓW


print("To zdanie pojawi się w pierwszej linii. \nKolejne zdanie w nowej.")


--->  INSTRUKCJE WARUNKOWE


x = 2
print(x == 2) # write True
print(x != 2) # write False
print(x == 3) # write False
print(x < 3)  # write True

imie = "Jan"
wiek = 23
if imie == "Jan" and wiek == 23:
    print("Nazywasz sie Jan i masz 23 lata.")

if imie == "Jan" or imie == "Robert":
    print("Nazywasz sie Jan lub Robert")

imie = "Robert"
if imie in ["Jan", "Robert"]:
    print("Nazywasz sie Jan lub Robert")

x = 2
if x == 2:
    print("x wynosi dwa!")
else:
    print("x jest rozne od dwoch.")


---> PĘTLE


#WHILE

c = 0
while(c < 10): 
    print(c)
    c = c + 1
print('koniec')

owoce = ['banan', 'gruszka', 'kiwi']
for owoc in owoce:
    print(owoc)
    
#FOR
    
for index in range(len(owoce)):
    a = owoce[index]
    print(a, index)
print(f'Tu jest taki owoc jak {a}')


---> FUNKCJE


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


---> SŁOWNIKI


kontakty = {
    "Jan" : 938477566,
    "Jacek" : 938377264,
    "Janusz" : 947662781
}



# FORMATOWANIE DATY

from datetime import datetime

now = datetime.now()
# 2020-01-01 00:00
format1 = now.strftime('%Y-%m-%d %H:%M:%S')
