sorted_list = list(range(200))

#Methodumuzu oluşturuken parametreleri ekliyoruz.Listemiz ve hedef sayı
def binary_search(sorted_list, target):

#Listeyi değişkene atadık.
    search_area = sorted_list

#Birden fazla sayı olması gerekiyor ki aramayı yapabilelim.
    while len(search_area) >=1:

#Elimizdeki listeyi gösteryiyoruz.
        print('Search area: ', search_area)

#Son indisi çekiyoruz.
        end = len(search_area) - 1

#İlk indisi çekiyoruz.
        middle = int((0+end)/2)

#Hedef sayı, ortadaki sayıdan daha küçükse
        if target < search_area[middle]:

#Hedef sayıyı, ortadaki sayıdan önce arıyoruz.
            search_area = search_area[:middle]

#Hedef sayı, ortadaki sayıdan önce büyükse
        elif target > search_area[middle]:

#Hedef sayıyı, ortadaki sayıdan sonra arıyor.
            search_area = search_area[middle:]

#Eğer hedef sayı, ortadaki sayıya eşitse dögümüz bitiyor.
        else:


            return print("Found it", str(search_area[middle]))

#Eğer 0 tane eleman varsa döngümüz çalışmaz.


    else:


        return print("Not in list")


binary_search(sorted_list, 7)
