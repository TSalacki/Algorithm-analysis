###############################
Tomasz Sa³acki, 283759
Projekt nr. 11 - Podzia³ zbioru
###############################

Projekt sk³ada siê z jednego programu:
AAL.py, który zajmuje siê rozwi¹zaniem problemu oraz wielokrotnym mierzeniem czasu wykonania i zapisywaniem wyników.

###############################
Sposoby uruchomienia:

usage: AAL.py [-h] -m MODE [-sf SETFILENAME] [-sbf SUBSETFILENAME] [-ss SIZE]
              [-sbc SUBSETCOUNT] [-ms MAXSIZE] -rf RESULTFILE -et MAXEXECTIME
              [-s SAMPLES] [-i ITERATIONS] [-si SIZEINCREASE]
              [-sci SUBSETCOUNTINCREASE]

  -h, --help            wyœwietl pomoc
  -m MODE, --mode MODE  Tryb wykonania programu: 
			1 - dane pobierane s¹ z pliku 
			2 - dane s¹ generowane losowo i wynik wyœwietlany w konsoli
                        3 - dane s¹ generowane losowo i do pliku zapisywany jest pomiar czasu
                        iterations
  -sf SETFILENAME, --setFile SETFILENAME
                        Nazwa pliku, który zawiera g³ówny zbiór
  -sbf SUBSETFILENAME, --subsetFile SUBSETFILENAME
                        Nazwa pliku zawieraj¹cego podzbiory
  -ss SIZE, --setSize SIZE
                        Jak wiele elementów ma zbiór (na potrzeby generacji danych)
  -sbc SUBSETCOUNT, --subsetCount SUBSETCOUNT
                        Jak wiele podzbiorów ma zostaæ wygenerowanyh.
  -ms MAXSIZE, --maxSize MAXSIZE
 			Jak¹ czêœci¹ g³ównego zbioru mog¹ byæ maksymalnie podzbiory.                       
  -rf RESULTFILE, --resultFile RESULTFILE
                        Nzwa pliku, gdzie zostane zapisany wynik dzia³ania programu.
  -et MAXEXECTIME, --execTime MAXEXECTIME
                        Jaki jest maksymalny czas przez jaki program mo¿e siê wykonywaæ.
  -s SAMPLES, --samples SAMPLES
                        Jak wiele pomiarów ma byæ wykonanych w obrêbie jednej iteracji dla danych nastaw.
  -i ITERATIONS, --iterations ITERATIONS
                        Jak wiele iteracji pomiarów ma byæ wykonanych.
  -si SIZEINCREASE, --sizeIncrease SIZEINCREASE
                        O ile rozmiar zbioru powiêksza siê z ka¿d¹ kolejn¹ iteracj¹
  -sci SUBSETCOUNTINCREASE, --subsetCountIncrease SUBSETCOUNTINCREASE
                        O ile powiêksza siê iloœæ podzbiorów z ka¿d¹ kolejn¹ iteracj¹.


###############################
Dane wejœciowe:

Zarówno zbiór jak i jego podzbiory powinny byæ podane w pliku testowym w postaci kolejnych liczb oddzielonych spacjami. W przypadku podzbiorów, ka¿dy kolejny podzbiór powinien znajdowaæ siê w nowej linii.

###############################
Dane wyjœciowe:

W trybie pracy pomiaru czasu, czasy dla jednej iteracji wypisane s¹ w jednej linii i odseparowane od siebie tabulatorami. Ka¿da kolejna iteracja znajduje siê w nowej linii.

w trybie pracy nastawionym na wynik wypisywane s¹: jakie podzbiory by³y wykorzystane (tablica B), podzbiór S1 (tablica E), podzbiór S2 (tablica F), liczba elementów g³ównego zbioru (N) oraz ile pêtli wykona³ algorytm (loops).

###############################
Wykorzystane struktury danych i algorytm:

Ca³y projekt opiera siê na operacjach na listach i zbiorach; wyró¿niamy w nim nastêpuj¹ce struktury:
A - (u¿yte tylko w algorytmie naiwnym) - lista, która zawiera kolejne liczby od 1...N
B - lista, ktora zawiera zbiory C1...Cm
C - lista list - ka¿da z podlist odpowiada kolejnej liczbie tablicy A i zawiera indeksych tych podzbiorów z B, w których ta liczba wystêpuje.
D - lista sk³adaj¹ca siê z 0 lub 1 (jest ich N). Zawiera informacjê czy podzbiór odpowiadaj¹cy danej wartoœci spe³nia za³o¿enia (1) lub nie spe³nia (0).
E - lista zawieraj¹ca elementy trafiaj¹ce do S1.
F - lista zawieraj¹ca elementy trafiaj¹ce do S2.

Wszystkie te elementy s¹ spiête razem w klasie stuff, która zawiera przy tym funkcje generate_variables i check_values odpowiadaj¹ce odpowiednio za generacjê danych losowych do programu oraz za sprawdzenie, które elementy danego podzbioru spe³niaj¹ obecne za³o¿enia, a które nie.

Sam algorytm opiera siê na próbie rozwi¹zania problemu podzia³u zbioru w z³o¿onoœci mniejszej ni¿ 2^n. Zamiast sprawdzaæ wszystkie mo¿liwe kombinacje podzia³u, sprawdzane s¹ te, które w danym kroku s¹ w stanie spe³niæ warunki zadania; jad¹c po kolejnych elementach tablicy E sprawdzamy czy przesuniêcie tej liczby do F spowoduje spe³nienie warunków zadania czy nie. Jeœli tak, to zostawiamy j¹ w F i idziemy dalej. Jeœli nie, to spradzamy czy dla tych podzbiorów, gdzie ona wystêpuje i powoduje niespe³nienie warunków jest ona najwiêkszym elementem. Jeœli nie, to wci¹¿ jest szansa, ¿e to jedynie tymczasowy problem, wiêc przechodzimy do kolejnej liczby. jeœli jest to ostatni element, to znaczy, ¿e obecny uk³ad nie ma szans na bycie poprawnym, wiêc przenosimy liczbê z powrotem do E i cofamy siê do ostatniej przeniesionej. J¹ przenosimy z powrotem do E i przechodzimy do kolejnej liczby, gdzie znów spradzamy cze jest ostatnim elementem. Czynim to tak d³ugo, a¿ lista F stanie siê pusta (i wtedy nie ma rozwi¹zania), albo dana liczba nie bêdzie ostatnim elementem zbiorów niespe³niaj¹cych warunków. Gdy trafimy na tak¹ liczbe, wtedy przechodzimy na pocz¹tek algorytmu. Sam algorytm koñczy dzia³anie, gdy dojdziemy do ostatniego elementu, albo gdy wszystkie podzbiory spe³ni¹ wymagania.

Dziêki takiemu rozwi¹zaniu algorytm jest w stanie znaleŸæ rozwi¹zanie potencjalnie bez ani jednego cofania siê, co znacz¹co redukuje jego z³o¿onoœæ obliczeniow¹. W przpyadku skomplikowanych danych, z³o¿onoœæ mo¿e tymczasowo urosn¹æ do z³o¿onoœæi wyk³adniczej, jednak¿e potêga bêdzie < n oraz zwykle rozwi¹zanie nie wymaga sprawdzenia wszystkich mo¿liwoœci. Tak samo jest w przypadku, gdy rozwi¹zania w ogóle nie ma.

###############################
Ograniczenia i za³o¿enia:

Algorytm pomimo swojej pesymistycznej z³o¿onoœci dzia³a bardzo dobrze dla nawet bardzo du¿ych N (rzêdu tysiêcy). Wynika to z faktu, ¿e o ile nie trafi siê wyj¹tkowo trudny przypadek jego efektywna z³o¿onoœæ jest quasi-liniowa. Jednak na wypadek wyst¹pienia przypadku powoduj¹cego przejœcie na z³o¿onoœæ 2^n wprowadzi³em ograniczenie do maksymalnej d³ugoœci czasu pracy - jeœli algorytm mia³by siê wykonywaæ d³u¿ej, wtedy przera dzia³anie. W takim przypadku istnieje zarówno mo¿liwoœæ, ¿e jest rozwiazanie jak i to, ¿e go nie ma, jednak¿e potencjalny czas pracy (np. w przypadku 2^1000) skutecznie niszczy sens czekania na odpowiedŸ.







