imie = input("jak masz na imię?")
print(f"cześć {imie}!")

pytania = [
    ("jak jest stolica Polski?", 
     {'a': 'Warszawa', 'b': 'Gdańsk', 'c': 'Poznań','d': 'Katowice'}, 'a'),
    ("jak ma imię Lewandowski?",
     {'a': 'Kamil', 'b': 'Janusz', 'c': 'Robert','d': 'Jakub'}, 'c'),
    ("jak język programowania kojarzy się z wężem?",
     {'a': 'C++', 'b': 'Java', 'c': 'Python','d':'TypeScript'}, 'c')
]
wynik = 0

for pytanie, mozliwe_odpowiedzi, prawidlowa_odpowiedz in pytania:
    print(pytanie)
    for klucz, wartosc in mozliwe_odpowiedzi.items():
        print(f"{klucz}: {wartosc}")
    odpowiedz_uzytkonika = input('Odpowiedź:')

    if odpowiedz_uzytkonika == prawidlowa_odpowiedz:
        print('To dobra odpowiedź!')
        wynik += 1
    else:
        print('To zła odpowiedź')
print(f'Twój wynik to {wynik}/{len(pytania)}')