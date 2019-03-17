###############################
Tomasz Sa�acki, 283759
Projekt nr. 11 - Podzia� zbioru
###############################

Projekt sk�ada si� z jednego programu:
AAL.py, kt�ry zajmuje si� rozwi�zaniem problemu oraz wielokrotnym mierzeniem czasu wykonania i zapisywaniem wynik�w.

###############################
Sposoby uruchomienia:

usage: AAL.py [-h] -m MODE [-sf SETFILENAME] [-sbf SUBSETFILENAME] [-ss SIZE]
              [-sbc SUBSETCOUNT] [-ms MAXSIZE] -rf RESULTFILE -et MAXEXECTIME
              [-s SAMPLES] [-i ITERATIONS] [-si SIZEINCREASE]
              [-sci SUBSETCOUNTINCREASE]

  -h, --help            wy�wietl pomoc
  -m MODE, --mode MODE  Tryb wykonania programu: 
			1 - dane pobierane s� z pliku 
			2 - dane s� generowane losowo i wynik wy�wietlany w konsoli
                        3 - dane s� generowane losowo i do pliku zapisywany jest pomiar czasu
                        iterations
  -sf SETFILENAME, --setFile SETFILENAME
                        Nazwa pliku, kt�ry zawiera g��wny zbi�r
  -sbf SUBSETFILENAME, --subsetFile SUBSETFILENAME
                        Nazwa pliku zawieraj�cego podzbiory
  -ss SIZE, --setSize SIZE
                        Jak wiele element�w ma zbi�r (na potrzeby generacji danych)
  -sbc SUBSETCOUNT, --subsetCount SUBSETCOUNT
                        Jak wiele podzbior�w ma zosta� wygenerowanyh.
  -ms MAXSIZE, --maxSize MAXSIZE
 			Jak� cz�ci� g��wnego zbioru mog� by� maksymalnie podzbiory.                       
  -rf RESULTFILE, --resultFile RESULTFILE
                        Nzwa pliku, gdzie zostane zapisany wynik dzia�ania programu.
  -et MAXEXECTIME, --execTime MAXEXECTIME
                        Jaki jest maksymalny czas przez jaki program mo�e si� wykonywa�.
  -s SAMPLES, --samples SAMPLES
                        Jak wiele pomiar�w ma by� wykonanych w obr�bie jednej iteracji dla danych nastaw.
  -i ITERATIONS, --iterations ITERATIONS
                        Jak wiele iteracji pomiar�w ma by� wykonanych.
  -si SIZEINCREASE, --sizeIncrease SIZEINCREASE
                        O ile rozmiar zbioru powi�ksza si� z ka�d� kolejn� iteracj�
  -sci SUBSETCOUNTINCREASE, --subsetCountIncrease SUBSETCOUNTINCREASE
                        O ile powi�ksza si� ilo�� podzbior�w z ka�d� kolejn� iteracj�.


###############################
Dane wej�ciowe:

Zar�wno zbi�r jak i jego podzbiory powinny by� podane w pliku testowym w postaci kolejnych liczb oddzielonych spacjami. W przypadku podzbior�w, ka�dy kolejny podzbi�r powinien znajdowa� si� w nowej linii.

###############################
Dane wyj�ciowe:

W trybie pracy pomiaru czasu, czasy dla jednej iteracji wypisane s� w jednej linii i odseparowane od siebie tabulatorami. Ka�da kolejna iteracja znajduje si� w nowej linii.

w trybie pracy nastawionym na wynik wypisywane s�: jakie podzbiory by�y wykorzystane (tablica B), podzbi�r S1 (tablica E), podzbi�r S2 (tablica F), liczba element�w g��wnego zbioru (N) oraz ile p�tli wykona� algorytm (loops).

###############################
Wykorzystane struktury danych i algorytm:

Ca�y projekt opiera si� na operacjach na listach i zbiorach; wyr�niamy w nim nast�puj�ce struktury:
A - (u�yte tylko w algorytmie naiwnym) - lista, kt�ra zawiera kolejne liczby od 1...N
B - lista, ktora zawiera zbiory C1...Cm
C - lista list - ka�da z podlist odpowiada kolejnej liczbie tablicy A i zawiera indeksych tych podzbior�w z B, w kt�rych ta liczba wyst�puje.
D - lista sk�adaj�ca si� z 0 lub 1 (jest ich N). Zawiera informacj� czy podzbi�r odpowiadaj�cy danej warto�ci spe�nia za�o�enia (1) lub nie spe�nia (0).
E - lista zawieraj�ca elementy trafiaj�ce do S1.
F - lista zawieraj�ca elementy trafiaj�ce do S2.

Wszystkie te elementy s� spi�te razem w klasie stuff, kt�ra zawiera przy tym funkcje generate_variables i check_values odpowiadaj�ce odpowiednio za generacj� danych losowych do programu oraz za sprawdzenie, kt�re elementy danego podzbioru spe�niaj� obecne za�o�enia, a kt�re nie.

Sam algorytm opiera si� na pr�bie rozwi�zania problemu podzia�u zbioru w z�o�ono�ci mniejszej ni� 2^n. Zamiast sprawdza� wszystkie mo�liwe kombinacje podzia�u, sprawdzane s� te, kt�re w danym kroku s� w stanie spe�ni� warunki zadania; jad�c po kolejnych elementach tablicy E sprawdzamy czy przesuni�cie tej liczby do F spowoduje spe�nienie warunk�w zadania czy nie. Je�li tak, to zostawiamy j� w F i idziemy dalej. Je�li nie, to spradzamy czy dla tych podzbior�w, gdzie ona wyst�puje i powoduje niespe�nienie warunk�w jest ona najwi�kszym elementem. Je�li nie, to wci�� jest szansa, �e to jedynie tymczasowy problem, wi�c przechodzimy do kolejnej liczby. je�li jest to ostatni element, to znaczy, �e obecny uk�ad nie ma szans na bycie poprawnym, wi�c przenosimy liczb� z powrotem do E i cofamy si� do ostatniej przeniesionej. J� przenosimy z powrotem do E i przechodzimy do kolejnej liczby, gdzie zn�w spradzamy cze jest ostatnim elementem. Czynim to tak d�ugo, a� lista F stanie si� pusta (i wtedy nie ma rozwi�zania), albo dana liczba nie b�dzie ostatnim elementem zbior�w niespe�niaj�cych warunk�w. Gdy trafimy na tak� liczbe, wtedy przechodzimy na pocz�tek algorytmu. Sam algorytm ko�czy dzia�anie, gdy dojdziemy do ostatniego elementu, albo gdy wszystkie podzbiory spe�ni� wymagania.

Dzi�ki takiemu rozwi�zaniu algorytm jest w stanie znale�� rozwi�zanie potencjalnie bez ani jednego cofania si�, co znacz�co redukuje jego z�o�ono�� obliczeniow�. W przpyadku skomplikowanych danych, z�o�ono�� mo�e tymczasowo urosn�� do z�o�ono��i wyk�adniczej, jednak�e pot�ga b�dzie < n oraz zwykle rozwi�zanie nie wymaga sprawdzenia wszystkich mo�liwo�ci. Tak samo jest w przypadku, gdy rozwi�zania w og�le nie ma.

###############################
Ograniczenia i za�o�enia:

Algorytm pomimo swojej pesymistycznej z�o�ono�ci dzia�a bardzo dobrze dla nawet bardzo du�ych N (rz�du tysi�cy). Wynika to z faktu, �e o ile nie trafi si� wyj�tkowo trudny przypadek jego efektywna z�o�ono�� jest quasi-liniowa. Jednak na wypadek wyst�pienia przypadku powoduj�cego przej�cie na z�o�ono�� 2^n wprowadzi�em ograniczenie do maksymalnej d�ugo�ci czasu pracy - je�li algorytm mia�by si� wykonywa� d�u�ej, wtedy przera dzia�anie. W takim przypadku istnieje zar�wno mo�liwo��, �e jest rozwiazanie jak i to, �e go nie ma, jednak�e potencjalny czas pracy (np. w przypadku 2^1000) skutecznie niszczy sens czekania na odpowied�.







