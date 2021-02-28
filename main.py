# Zad1.
# Napisz pierwszy skrypt,
# w którym zadeklarujesz po dwie zmienne każdego typu
# a następnie wyświetl te zmienne

# a = 'Pierwsze zadanie'
# b = 1
# print(a)
# print(b)
###########################################################################
# Zad2.
# Stwórz skrypt kalkulator,
# w którym wykorzystać wszystkie podstawowe działania arytmetyczne

# num1 = float(input("Wprowadź pierwszą liczbę: "))
# op = input("Wprowadź operator: ")
# num2 = float(input("Wprowadź drugą liczbę: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Podano zły operator")
###########################################################################
# Zad3.
# Napisz skrypt,
# w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

# suma = 5
# odejmowanie = 2
# mnożenie = 5
# dzielenie = 100
# potęgowanie = 3
# modulo = 35
# suma += 3
# odejmowanie -= 10
# mnożenie *= 3
# dzielenie /= 4
# potęgowanie **=2
# modulo %= 2
# print(suma)
# print(odejmowanie)
# print(mnożenie)
# print(dzielenie)
# print (potęgowanie)
# print (modulo)
###########################################################################
# Zad4.
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia:

# e = int(input("Podaj niewiadomą e: "))
# wynik = e**2
# print(wynik)
###########################################################################
# Zad.5
# Zapisz swoje imie i nazwisko w oddzielnych zmiennych
# wszystkie wielkimi literami. Użyj odpowiedniej metody
# by wyświetlić je pisane tak,
# że pierwsza litera jest wielka a poszostałe małe.
# (trzeba użyć metody capitalize)

# string = "WOJCIECH"
# string1 = "ORLOWSKI"
#
# zmieniona_zmienna = string.capitalize()
# zmieniona_zmienna1 = string1.capitalize()
# print(zmieniona_zmienna)
# print(zmieniona_zmienna1)
###########################################################################
# Zad.6
# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki
# z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.
# (trzeba użyć metody count)

# string = "The future is bulletproof The aftermath is secondary It's time to do it now and do it loud Killjoys, make some noise Na, na-na, na-na, na-na, na-na Na, na-na, na-na, na-na Na, na-na, na-na, na-na Na-na, na-na, na-na Drugs, gimme drugs, gimme drugs I don't need it, but I'll sell what you got Take the cash and I'll keep it Eight legs to the wall Hit the gas, kill 'em all And we crawl, and we crawl, and we crawl You be my detonator Love, gimme love, gimme love I don't need it, but I'll take what I want from your heart And I'll keep it in a bag, in a box Put an X on the floor Gimme more, gimme more, gimme more Shut up and sing it with me From mall security (Na, na-na, na-na, na-na) To every enemy (Na, na-na, na-na, na-na) We're on your property Standing in V formation Let's blow an artery (Na, na-na, na-na, na-na) Eat plastic surgery (Na, na-na, na-na, na-na) Keep your apology Give us more detonation More, gimme more, gimme more Oh, let me tell you 'bout the sad man Shut up and let me see your jazz hands Remember when you were a madman Thought you was Batman And hit the party with a gas can Kiss me. you animal You run the company (Na, na-na, na-na, na-na) Fuck like a Kennedy (Na, na-na, na-na, na-na) I think we'd rather be Burning your information Let's blow an artery (Na, na-na, na-na, na-na) Eat plastic surgery (Na, na-na, na-na, na-na) Keep your apology Give us more detonation And right here Right now All the way in Battery City The little children Raise their open filthy palms Like tiny daggers up to heaven And all the juvie halls And the Ritalin rats Ask angels made from neon And fucking garbage Scream out, What will save us? And the sky opened up Everybody wants to change the world Everybody wants to change the world But no one, no one wants to die Wanna try, wanna try, wanna try Wanna try, wanna try, now I'll be your detonator Make no apology (Na, na-na, na-na, na-na) It's death or victory (Na, na-na, na-na, na-na) On my authority Crash and burn, young and loaded Drop like a bullet shell (Na, na-na, na-na, na-na) Dress like a sleeper cell (Na, na-na, na-na, na-na) I'd rather go to hell Than be in purgatory Cut my hair Gag and bore me Pull this pin Let this world explode"
# substring = "na"
# count = string.count(substring)
# print("Słów 'NA' w tej piosence jest: ", count)
###########################################################################
# Zad.7
# Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie
# indeksu. Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę,
# wykorzystując indeksy.

###########################################################################
# Zad.8
#Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i
#spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)

# string = "The future is bulletproof The aftermath is secondary It's time to do it now and do it loud Killjoys, make some noise Na, na-na, na-na, na-na, na-na Na, na-na, na-na, na-na Na, na-na, na-na, na-na Na-na, na-na, na-na Drugs, gimme drugs, gimme drugs I don't need it, but I'll sell what you got Take the cash and I'll keep it Eight legs to the wall Hit the gas, kill 'em all And we crawl, and we crawl, and we crawl You be my detonator Love, gimme love, gimme love I don't need it, but I'll take what I want from your heart And I'll keep it in a bag, in a box Put an X on the floor Gimme more, gimme more, gimme more Shut up and sing it with me From mall security (Na, na-na, na-na, na-na) To every enemy (Na, na-na, na-na, na-na) We're on your property Standing in V formation Let's blow an artery (Na, na-na, na-na, na-na) Eat plastic surgery (Na, na-na, na-na, na-na) Keep your apology Give us more detonation More, gimme more, gimme more Oh, let me tell you 'bout the sad man Shut up and let me see your jazz hands Remember when you were a madman Thought you was Batman And hit the party with a gas can Kiss me. you animal You run the company (Na, na-na, na-na, na-na) Fuck like a Kennedy (Na, na-na, na-na, na-na) I think we'd rather be Burning your information Let's blow an artery (Na, na-na, na-na, na-na) Eat plastic surgery (Na, na-na, na-na, na-na) Keep your apology Give us more detonation And right here Right now All the way in Battery City The little children Raise their open filthy palms Like tiny daggers up to heaven And all the juvie halls And the Ritalin rats Ask angels made from neon And fucking garbage Scream out, What will save us? And the sky opened up Everybody wants to change the world Everybody wants to change the world But no one, no one wants to die Wanna try, wanna try, wanna try Wanna try, wanna try, now I'll be your detonator Make no apology (Na, na-na, na-na, na-na) It's death or victory (Na, na-na, na-na, na-na) On my authority Crash and burn, young and loaded Drop like a bullet shell (Na, na-na, na-na, na-na) Dress like a sleeper cell (Na, na-na, na-na, na-na) I'd rather go to hell Than be in purgatory Cut my hair Gag and bore me Pull this pin Let this world explode"
# x = string.split(", ")
# print(x)
###########################################################################
# Zad.9
# Napisz skrypt, w którym zadeklarujesz zmienne typu:
# string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.

# string = "Zmienna typu string"
# print(string)
# print(float(25.16))
# print(0x14c)
###########################################################################