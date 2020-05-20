print ("Bu program Türkçedeki istediğiniz harfle başlayan ve istediğiniz harfle biten kelimeleri sıralar.")
firstLetter = input("İLK HARF: ")
lastLetter = input("SON HARF: ")

wordList = open("full.txt","r", encoding="utf-8") # full.txt dosyasını utf-8 e çevirerek açar
word = wordList.read().splitlines() 

for i in word:
    w = i.split()[0]
    if w.startswith(firstLetter) and w.endswith(lastLetter):
        print(w)