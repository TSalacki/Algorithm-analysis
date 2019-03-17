import bisect
import time
import random
import argparse


# klasa odpowiedzialna za obsluge danych
class SetDivider:
    def __init__(self):
        self.B = []
        self.C = []
        self.D = []
        self.E = []
        self.F = []

    def generate_variables(self, n, subsetNum, maxSize):
        for i in range(1, n+1):                                 # generujemy listę zawierającą wszystkie elementy
            self.E.append(i)
        for i in range(1, subsetNum+1):                         # generujemy podzbiory C od i do zadanej wartości
            tmpset = set()
            tmpset = tmpset.union(set(random.sample(self.E, int(random.uniform(2, self.E.__len__()*maxSize)))))
            self.B.append(tmpset)

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

    def divideSets(self):
        i = 0
        # liczba podzbiorów spełniających warunki zadania
        j = 0
        # ilość elementów głównego zbioru
        N = self.E.__len__()
        tmp = 0
        # pomocnicze liczniki
        counter1 = 0
        counter2 = 0
        # licznik ile pętli wykonał prgoram (gdyż może być to rozbierznie z i)
        loopCounter = 0
        switch = 0

        while i < N:
            loopCounter = loopCounter + 1
            # ze względu na możliwość wystapienia 2^n, sprawdzamy czy maksymalny czas został przekroczony i jeśli tak, to kończymy
            if (time.process_time() - start) > args.maxExecTime:
                break
            i = i + 1
            # punkt 5
            if j == self.B.__len__():
                break
            # punkt 1
            counter1 = 0
            for x in self.C[i - 1]:
                if self.D[x] == 1:
                    counter1 = counter1 + 1
            if counter1 == self.C[i - 1].__len__():
                continue
            # punkt 2
            bisect.insort_left(self.F, i)
            self.E.remove(i)
            counter2 = j
            j = self.check_values(j, i)
            counter2 = counter2 - j
            if counter2 == self.C[i - 1].__len__():
                continue
            # punkt 3
            while True:
                switch = 1
                for x in self.C[i - 1]:
                    if self.D[x] == 0 and i == max(self.B[x]):
                        switch = 0
                        break
                if switch == 1:
                    break

                # punkt 4
                if switch == 0:
                    if self.F.__len__() == 0:
                        switch = 2
                        break
                    i = self.F[-1]
                    bisect.insort_left(self.E, self.F[-1])
                    self.F.remove(self.F[-1])

                    # sprawdzenie
                    j = self.check_values(j, i)

            if switch == 2:
                break
        return time.process_time(), switch

    def prepareData(self, mode, fname, subfname, size, subsetCount, maxSize):
        if mode == 1:
            with open(fname, 'r') as setFile:
                tempSet = setFile.readline()
                tempSet = tempSet.split()
                tempSet = map(int, tempSet)
                for x in tempSet:
                    self.E.append(x)
            with open(subfname, 'r') as subsetFile:
                tempSubSet = []
                for line in subsetFile:
                    line = line.split()
                    line = map(int, line)
                    tempSubSet.append(line)
                for x in tempSubSet:
                    self.B.append(set(x))
        else:
            self.generate_variables(size, subsetCount, maxSize)
        for x in range(0, self.E.__len__()):
            self.C.append([])
        for x in range(0, self.B.__len__()):
            self.D.append(0)
        tmp3 = 0
        for x in self.B:
            for y in x:
                self.C[y - 1].append(tmp3)
            tmp3 = tmp3 + 1

    def printResults(self, mode, file, start, end, switch):
        if mode == 3:
            print('Czas startu: ', start, ' Czas konca: ', end, ' Czas wykonania algorytmu: ', round((end - start), 2))
            file.write((end - start).__str__().replace('.', ','))
            file.write('\t')
        else:
            for i in range(0, self.B.__len__() - 1):
                if self.B[i].issubset(self.E) or self.B[i].issubset(self.F):
                    print('###############################')
                    print('Brak rozwiazania')
                    print('###############################')
                    switch = 2
                    if not mode == 3:
                        file.write('BRAK ROZWIAZANIA\n')
                    break
            if not switch == 2:
                file.write('B: ' + self.B.__str__() + '\n')
                file.write('E: ' + self.E.__str__() + '\n')
                file.write('F: ' + self.F.__str__() + '\n')
                print('B: ', self.B)
                print('E: ', self.E)
                print('F: ', self.F)

#######################################################################################################################


parser = argparse.ArgumentParser(description="How to divide set into two subsets.")
parser.add_argument('-m', '--mode', dest='mode', type=int, required=True,
                    help='Mode of execution:\n1 - data from file \n2 - random data\n3 - random data with time measurmenets and multiple iterations')
parser.add_argument('-sf', '--setFile', dest='setFileName', required=False,
                    help='Name of file with set')
parser.add_argument('-sbf', '--subsetFile', dest='subsetFileName', required=False,
                    help='Name of file with subsets')
parser.add_argument('-ss', '--setSize', dest='size', type=int, required=False,
                    help='How much elements are in set')
parser.add_argument('-sbc', '--subsetCount', dest='subsetCount', type=int, required=False,
                    help='How many subsets will be generated.')
parser.add_argument('-ms', '--maxSize', dest='maxSize', type=float, required=False,
                    help='Which percent of elements from set subsets are allowed to have.')
parser.add_argument('-rf', '--resultFile', dest='resultFile', required=True,
                    help='Name of file where results will be stored')
parser.add_argument('-et', '--execTime', dest='maxExecTime', type=float, required=True,
                    help='What is the maximum time the program is allowed to run.')
parser.add_argument('-s', '--samples', dest='samples', type=int, required=False, default=1,
                    help='How much samples per iteration')
parser.add_argument('-i', '--iterations', dest='iterations', type=int, required=False, default=1,
                    help='How much iterations')
parser.add_argument('-si', '--sizeIncrease', dest='sizeIncrease', type=int, required=False,
                    help='How much size increase per iteration')
parser.add_argument('-sci', '--subsetCountIncrease', dest='subsetCountIncrease', type=int, required=False,
                    help='How much subset count increase per iteration')


args = parser.parse_args()

resultFile = open(args.resultFile, 'a')

for i in range(1, args.iterations+1):
    if i > 1:
        args.size = args.size + args.sizeIncrease
        args.subsetCount += args.subsetCountIncrease
    for j in range(1, args.samples+1):
        myStuff = SetDivider()

        myStuff.prepareData(args.mode, args.setFileName, args.subsetFileName, args.size, args.subsetCount, args.maxSize)

        start = time.process_time()

        end, switch = myStuff.divideSets()

        myStuff.printResults(args.mode, resultFile, start, end, switch)

    resultFile.write('\n')

resultFile.close()

