# Project Euler #
[Project Euler hovedside](https://projecteuler.net/)

## Problem 6 ##
[Problem 6 hos Project Euler ](https://projecteuler.net/problem=6)

### Problembeskrivelse ###
*Fritt oversatt fra Project Euler*

Summen av kvadratet av de første ti naturlige tallene er,
$$1^2 + 2^2 + 3^2 + \ldots{} + 10^2 = 385$$

Kvadratet av summen av de første ti naturlige tallene er,

$$(1 + 2 + 3 + \ldots{} + 10)^{2} = 55^{2} = 3025$$

Differansen mellom kvadratet av summen, og summen av kvadratene, er da
$3025 - 385 = 2640$

Finn differansen mellom kvadratet av summen av de hundre første naturlige tallene, og summen av kvadratene. I.e,

$$(1 + 2 + 3 + \ldots{} + \text{n})^{2} - (1^2 + 2^2 + 3^2 + \ldots{} + \text{n}^2)$$

der $n = 100$



### Løsning ###
Koden til løsningen på dette problemet vil være bygget opp med funksjoner.

#### Steg 1: Sum av kvadrater ####
Først lager vi funksjonen `SumOfSquares()` som tar inn et heltall (naturlig tall) `n`,
og regner ut summen av kvadratet av alle tall opp *til og med* `n`.


```python
def SumOfSquares(n):
	res = 0
	for i in range(n + 1):
		res += i**2

	return res
```

- I funksjonen lager vi variabelen `res`. Denne variabelen oppdateres ved at vi hele tiden legger til kvadratet av et tall.
- Vi kontrollerer hvilke tall vi legger til i `res` ved å bruke en `for`-løkke som itererer gjennom alle tallene fra 0 til `n`.
- Vi bruker `range(n + 1)` for å få med endepunktet (`range(100)` inkluderer ikke 100).
- `res += i**2` legger til kvadratet av gjeldende iterasjon (tall) til variabelen `res`
- Til sist returnerer vi `res` slik at når vi kaller funksjonen vil vi få summen av kvadratene.


#### Steg 2: Kvadratet av summen ####
For å finne kvadratet av summen av de første n naturlige tallene lager vi funksjonen `SquareOfSum`.
Denne er litt enklere enn den første funksjonen, fordi vi kan utnytte relasjonen mellom summen av
de første n naturlige tallene og det n-te [trekanttallet](https://en.wikipedia.org/wiki/Triangular_number).

Mer bestemt, så er det n-te trekanttallet, $T_n$
$$T_{n} = \sum_{i=1}^{n} i = 1 + 2 + 3 + \ldots{} + n = \frac{n(n+1)}{2}$$
og dette utnytter vi i funksjonen vår.
Funksjonen `SquareOfSum` tar inn et heltall `n` og regner ut kvadratet av summen tallene opp *til og med* `n`.


```python
def SquareOfSum(n):
	res = ((n * (n + 1)) / 2)**2
    
	return res
```

- Variabelen `res` holder resultatet, altså kvadratet av summen.
- Vi definerer `res` ved formelen for det n-te trekanttalletm, og husker å kvadrere alt.
- Vi returnerer `res` slik at når vi kaller funksjonen vil vi få summen av kvadratene.

#### Steg 3: Finne differansen ####
Det som gjenstår nå er simpelthen å finne differansen.
For å gjøre det kaller vi begge funksjonene vi har laget tidligere, og regner ut differansen.


```python
target = 100

diff = SquareOfSum(target) - SumOfSquares(target)

print(diff)
```

    25164150.0
    

- Vi definerer variabelen `target` og tildeler den verdien 100, siden problembeskrivelsen gjelder de naturlige tallene opp til og med 100.
- Vi definerer variabelen `diff` ved å kalle funksjonene våre. Mer bestemt, differansen mellom disse.
- Til slutt bruker vi `print(diff)` for å skrive resultatet til konsoll.

#### Komplett kode ####
Den fullstendige koden vil da se slik ut


```python
# Sum av kvadrater
def SumOfSquares(n):
	res = 0
	for i in range(n + 1):
		res += i**2

	return res

# Kvadrat av summen
def SquareOfSum(n):
	res = ((n * (n + 1)) / 2)**2
    
	return res


# De 100 første naturlige tallene
target = 100 # we want to work with the first 100 natural numbers

# Regner differansen
diff = SquareOfSum(target) - SumOfSquares(target)

# Printer resultatet
print(diff)
```

    25164150.0
    


```python

```
