sorted_list = list(range(1000))

def binary_search(sorted_list, target):
    
    search_area = sorted_list
    i = 0
    while len(search_area) >=1:
        print('Search area: ', search_area)
        end = len(search_area) - 1
        middle = int((0+end)/2)
        i = i + 1
        
        if target < search_area[middle]:
            search_area = search_area[:middle]
        elif target > search_area[middle]:
            search_area = search_area[middle:]
        else:
            return print("Found it", str(search_area[middle]))
    else:
        return print("Not in list")


binary_search(sorted_list, 100)