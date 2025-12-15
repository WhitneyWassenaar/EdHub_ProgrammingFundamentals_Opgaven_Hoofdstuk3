# Deze opdracht komt uit de EdHub Hoofdstuk 3 > opgaven
# ==========================================
# Voorbeeld Opdracht
# Gegeven is een variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn leeftijd is 25'
# ==========================================

leeftijd = 25
print('Mijn leeftijd is', leeftijd)  # Het resultaat is: Mijn leeftijd is 25

# ==========================================
# Opgave 1.
# Gegeven is een variabele 'naam' met de waarde 'Jan' en de variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn naam is Jan en ik ben 25 jaar oud'. Verander daarna de leeftijd naar 30 en print de zin opnieuw.
#
# Verwachte uitkomst is: 'Mijn naam is Jan en ik ben 25 jaar oud' en 'Mijn naam is Jan en ik ben 30 jaar oud'
# ==========================================

naam = 'Jan'
leeftijd = 25

print(f'Mijn naam is {naam} en ik ben {leeftijd} jaar oud')

leeftijd = 30
print(f'Mijn naam is {naam} en ik ben {leeftijd} jaar oud')


# ==========================================
# Opgave 2.
# Gegeven zijn een aantal variabelen. Wat zijn de datatypes van de variabelen als je ze print met de type() method? Bedenk vooraf wat het datatype is en controleer daarna met de print functie of je het goed hebt.
# ==========================================

a = 5 / 5 # float

b = '12' # string

c = 5 * 5 # int

d = 'Python' * 4 #string

print(type(a), type(b), type(c), type(d))


# ==========================================
# Opgave 3.
# Variabele namen mag je zelf verzinnen, maar niet alle namen zijn toegestaan omdat ze al gebruikt worden door Python (keywords). Welke van de volgende variabele namen zijn toegestaan en welke niet?
# ==========================================


And = 'something'
# while = 'something' # Deze zal een error geven
Break = 'something'
awaiting = 'something'

# === JUISTE ANTWOORDEN ===
# a.     And = 'something'    | Kan wel, want in python is 'and' wel een keyword. Python is hoofdletter gevoelig dus 'And' kan weer wel
# b.     while = 'something'  | Kan niet, want while is een keyword en wordt dus gebruikt voor while loops in Python
# c.     Break = 'something'  | Kan wel, want in Python is 'break' (dus met een kleine b) wel een keyword in Python, dus met een hoofdletter kan het wel
# d.     awaiting = 'something'   | Kan wel, want in Python is 'await' een keyword, dus awaiting kan wel gebruikt worden

# ==========================================
# Opgave 4.
# Schrijf een goede variabele naam voor onderstaande onderdelen. Denk aan de conventies voor Python variabelen.
#
# a. Het totale aantal van het product bananen in een winkelmand
#
# b. De minimale toegestane lengte voor een attractie in een pretpark
#
# c. Het grootste getal in een rij met getallen
# ==========================================
# In python gebruik je liever snake_case
# === MIJN ANTWOORDEN ===
# A. total_bananas
# B. min_length
# C. highest_number_in_row

# === UITWERKING ===
# a.
totale_aantal_bananen = 0
sum_bananas = 0
# b.
min_lengte_voor_achtbaan = 120
min_length_for_rollercoaster = 120
# c.
max_getal_uit_rij = 1000
highest_number_of_row = 1000

# Natuurlijk zijn er meerdere goede antwoorden mogelijk. Zorg wel dat je in ieder geval snake_case gebruikt. Liefst heb je zo kort mogelijke variabele namen, maar ze mogen zeker wat langer zijn als het daardoor duidelijker wordt waar de variabele voor staat. De lesstof en oefeningen zijn in het Nederlands geschreven, maar in de praktijk wordt meestal Engels gebruikt. Het is goed om daar alvast aan te wennen.




# ==========================================
# Opgave 5.
# Gegeven is de variabele 'teller' met de waarde 10. Verhoog de waarde van de teller met 1. Gebruik de samengevoegde toekenning operator. Print de waarde van de teller. Herhaal dit proces maar verlaag de teller met 2. Print opnieuw de waarde van de teller.
#
# Verwachte uitkomst is: 11 en 9
# ==========================================

teller = 10
teller += 1

print(teller)  # Het resultaat is: 11

teller -= 2
print(teller) # Het resultaat is: 9



# ==========================================
# Opgave 6.
# Gegeven zijn de onderstaande statements. Welke van de print statements zullen een foutmelding geven en waarom?
#
# a. print(int(‘1490.99’) | kan niet want het getal is een float dat kan niet gelijk omgezet worden naar een int
#
# b. print(float(12))     | kan wel, een int kan naar een float
#
# c. print(int('1plus1')) | kan niet, er zit een string tussen de getallen en die kan niet naar een int gemaakt worden
#
# d. print(str(25E10))    | kan wel, want 25E10 is een geheel getal en dus is het een int, die kan wel naar een string gemaakt worden
# ==========================================



# ==========================================
# Opgave 7.
# Gegeven is de variabele getal_1 met waarde 3 en getal_2 met waarde 5. Schrijf de zin 'Het product van 3 en 5 is 15' door de variabelen te gebruiken in de zin. Pas een f-string toe.
# ==========================================

getal_1 = 3
getal_2 = 5
som = getal_1 * getal_2
print(f'Het product van {getal_1} en {getal_2} is {som}')