import time
import random
import sys


# klasa odpowiedzialna za obsluge danych
class Stuff:
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []
        self.D = []
        self.E = []
        self.F = []

    def generate_variables(self, n, subsetNum, maxSize):
        for i in range(1, n+1):                                 # generujemy listę zawierającą wszystkie elementy
            self.A.append(i)
            self.E.append(i)
        for i in range(1, subsetNum+1):                         # generujemy podzbiory C od i do zadanej wartości
            tmpSet = set()
            # tmpSet = {self.E[i%self.E.__len__()]}               # gwarantujemy, że w podzbiorach będą przynajmniej raz liczby z wyniku
            tmpSet = tmpSet.union(set(random.sample(self.E, int(random.uniform(2, self.E.__len__()*maxSize)))))
            self.B.append(tmpSet)

    def check_values(self, j, i):
        for x in self.C[i - 1]:
            if self.D[x] == 1:
                j = j - 1
                self.D[x] = 0
        for x in self.C[i - 1]:
            if not self.B[x].issubset(self.E) and not self.B[x].issubset(self.F):
                if self.D[x] == 0:
                    j = j + 1
                    self.D[x] = 1
        return j

# ######################################################################################################################

choice = int(sys.argv[1])

myStuff = Stuff()

if choice == 1:
    setFileName = sys.argv[2]
    with open(setFileName, 'r') as setFile:
        tempSet = setFile.readline()
        tempSet = tempSet.split()
        tempSet = map(int, tempSet)
        for x in tempSet:
            myStuff.E.append(x)
    subsetFileName = sys.argv[3]
    with open(subsetFileName, 'r') as subsetFile:
        tempSubSet = []
        for line in subsetFile:
            line = line.split()
            line = map(int, line)
            tempSubSet.append(line)
        for x in tempSubSet:
            myStuff.B.append(set(x))
else:
    n = sys.argv[2]
    subsetNum = sys.argv[3]
    size = sys.argv[4]
    myStuff.generate_variables(int(n), int(subsetNum), float(size))


start = time.process_time()

for x in range(0, myStuff.E.__len__()):
    myStuff.C.append([])

for x in range(0, myStuff.B.__len__()):
    myStuff.D.append(0)

start2 = time.process_time()

tmp3 = 0

for x in myStuff.B:
    for y in x:
        myStuff.C[y-1].append(tmp3)
    tmp3 = tmp3 + 1
end2 = time.process_time()

# Koniec przygotowań i część właściwa algorytmu

j = 0
N = myStuff.E.__len__()
tmp = 0
counter1 = 0
counter2 = 0
loopCounter = 0
switch = 0
max_exec_time = float(sys.argv[6])

i = '1' + '0' * (N-1)

while not i == '1' * i.__len__():
    j = 0
    switch = 2
    for x in i:
        if x == '1':
            myStuff.E.append(myStuff.A[j])
        else:
            myStuff.F.append(myStuff.A[j])
        j = j + 1
    for x in myStuff.B:
        if x.issubset(myStuff.E) or x.issubset(myStuff.F):
            switch = 0
    if switch == 2:
        break

    myStuff.E.clear()
    myStuff.F.clear()
    c = int(i, 2) + 1
    i = bin(c)[2:]
    print(i)
    loopCounter = loopCounter + 1


print("ROZWIAZANIE")
print(loopCounter)
print(myStuff.A)
print(myStuff.B)
print(myStuff.E)
print(myStuff.F)
end = time.process_time()
print('Czas startu: ' + start.__str__() + ' Czas konca: ' + end.__str__() + ' Czas wykonania algorytmu: ' + round((end - start), 2).__str__())
sys.exit()

fname = sys.argv[5]

if choice == 3:
    end = time.process_time()
    end3 = time.time()
    print('Czas startu: ' + start.__str__() + ' Czas konca: ' + end.__str__() + ' Czas wykonania algorytmu: ' + round((end-start), 2).__str__())
    print('Czas startu: ' + start2.__str__() + ' Czas konca: ' + end2.__str__() + ' Czas generowania danych: ' + round((end2-start2), 2).__str__())
    file = open(fname, 'a')
    file.write((end-start).__str__().replace('.', ','))
    file.close()
print('\n' + 'i: ' + i.__str__() + ' j: ' + j.__str__() + ' N: ' + N.__str__() + ' Loops: ' + loopCounter.__str__())


for i in range(0, myStuff.B.__len__()-1):
    if myStuff.B[i].issubset(myStuff.E) or myStuff.B[i].issubset(myStuff.F):
        print('###############################')
        print('Brak rozwiazania')
        print('###############################')
        switch = 2
        if not choice == 3:
            file = open(fname, 'a')
            file.write('BRAK ROZWIAZANIA\n')
            file.write('N: ' + N.__str__() + ' Loops: ' + loopCounter.__str__() + '\n')
            file.close()
        break
if not switch == 2 and not choice == 3:
    file = open(fname, 'a')
    file.write('koniec B: ' + myStuff.B.__str__() + '\n')
    file.write('koniec E: ' + myStuff.E.__str__() + '\n')
    file.write('koniec F: ' + myStuff.F.__str__() + '\n')
    file.write('N: ' + N.__str__() + ' Loops: ' + loopCounter.__str__() + '\n')
    file.close()
    print('koniec B: ' + myStuff.B.__str__())
    print('koniec E: ' + myStuff.E.__str__())
    print('koniec F: ' + myStuff.F.__str__())
