list = [10,25,32,29,1,76,53,69,70]

#Fonksiyonu oluşturduk.Parametremizi verdik.
def insertion_sort(list):

#Listemizi değişkene atadık.
    seq = list[:]

#Listemizin kaç tane elemandan oluştuğunu bulduk.
    n = len(seq)

#Döngümüzü açtık.
    for i in range(1,n):

#Her bir indisin pozisyonlarını aldık.
        value = seq[i]

#İndislerin pozisyonlarını kaydettik.
        position = i

#Pozisyon 0'dan büyük ama solundakinden küçükse
        while position > 0 and value < seq [position -1 ]:

#Sola kayar.
            seq[position] = seq[position -1]

#Ve sonraki sıraya kaydırırız.
            position -=1

#Döngüyü bitiren yer.
        seq[position] = value


        print(seq)


insertion_sort(list)
