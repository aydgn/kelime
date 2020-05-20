print ("Bu program Türkçedeki istediğiniz harfle başlayan ve istediğiniz harfle biten kelimeleri sıralar.")
firstLetter = input("İLK HARF: ")
lastLetter = input("SON HARF: ")

wordList = open("full.txt","r", encoding="utf-8") # full.txt dosyasını utf-8 e çevirerek açar
word = wordList.read().splitlines() # keliemeleri liste haline getirdik 

for i in word:
    w = i.split()[0]
    # full.txt dosyasında kelimeler yanlarında numaralarla olduğu için .split ile kelimeleri ayırdık.
    # .split default olarak whitespace ile öğeyi ayırıyor. [0] ile ilk olanı yani kelimeyi seçmiş olduk.
    if w.startswith(firstLetter) and w.endswith(lastLetter):
        print(w)