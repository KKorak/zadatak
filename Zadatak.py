#Prvi znak:
#-          1 – ako se u tekstu nalazi barem 5 riječi koje završavaju sa „abc“, a ne počinju sa x
#-          0 - inače
#Drugi znak:
#-          Zadnja znamenka broja koji se dobije tako da se pomnože svi brojevi u tekstu („broj u tekstu“ znači „riječ“ koja se sastoji samo od znamenki)
#-          Ako nema brojeva, izlaz je znak „n“
#Treći znak:
#-          Zadnja znamenka broja riječi u tekstu
#Četvrti znak:
#-          Zadnja znamenka broja ne-praznih znakova u tekstu


testni_string = "abc xabc xabcx aabc aabc bcab abcabcabc 123abc"
brojRijeci=0
umnozak=0

words = testni_string.split()

for i in range(len(words)):
    if len(words[i]) > 2 and words[i].endswith('abc') and not words[i].startswith('x'):
        brojRijeci=brojRijeci + 1

if brojRijeci > 5:
    print(1)
else:
    print(0)

for i in range(len(words)):
    if (words[i]).isdigit():
        if umnozak == 0:
            umnozak = int(words[i])
        else:
            umnozak = umnozak * int(words[i])

if umnozak == 0:
    print('n')
else:
    print(umnozak)

numberOfWords = len(words)
print(numberOfWords)

numChars = len(testni_string) - testni_string.count(' ')
print(numChars % 10)
