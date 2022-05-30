# Lambda functions
from typing import Tuple


printStri = lambda str, num: f'{str}{" "*(num-len(str))}'
printLine = lambda num: print(f'{"-"*(num)}')
lenStrArray = lambda arr: len(max(arr, key=len))
capitString = lambda str: ' '.join([s.capitalize() for s in str.split()])
isEven = lambda num: num % 2 == 0
isOdd = lambda num: num % 2 != 0
# ------------------------------------------------------------------------------------
# Main Variables
N = 60
# ------------------------------------------------------------------------------------
printLine(N)
x, y, lun = 2, 11, 30
print(f'{printStri("Divisione intera",lun)} {y // x}')    # divisione intera
print(f'{printStri("Divisione float",lun)} {y / x}')      # divisione float
print(f'{printStri("Resto",lun)} {y % x}')                # resto
print(f'{printStri("Potenza",lun)} {y ** x}')             # potenza
# ------------------------------------------------------------------------------------
printLine(N)
str = 'ciao sono \"giovanni\"'
print(str.lower())
print(str.upper())
print(str.strip())
print(str.replace('giovanni', 'celeste'.upper()))
# ------------------------------------------------------------------------------------
printLine(N)
print(bool(False))      # False
print(bool(None))       # False
print(bool(0))          # False
print(bool(""))         # False
print(bool(True))       # True
print(bool(2))          # True
print(bool("ciao"))     # True
# ------------------------------------------------------------------------------------
printLine(N)
print(isEven(x))
print(isOdd(x))
# ------------------------------------------------------------------------------------
#### LIST ####
printLine(N)
citta = ['san donato milanese', 'udine', 'venezia', 'firenze']
citta.append('milano')
citta.insert(1, 'brescia')
citta.sort()
# LIST COMPREHENSION
printCitta = lambda a: [
    print(f'{printStri(capitString(w),lenStrArray(a))}|') for w in a]
printCitta(citta)
# ------------------------------------------------------------------------------------
#### TUPLE ####
printLine(N)
citta = ('san donato milanese', 'udine', 'venezia', 'firenze')
(x, y, *z) = citta
print(citta)
print(x)
print(y)
print(z)
print(citta.count('venezia'))
print(citta.index('venezia'))
# ------------------------------------------------------------------------------------
#### SET ####
printLine(N)
citta = {'san donato milanese', 'udine', 'venezia', 'firenze'}
citta.add('milano')
citta.update({'brescia', 'roma', 'venezia'})

citta.remove('udine')  # se non esiste l'elemento, errore
citta.discard('roma')
[print(city) for city in citta]
