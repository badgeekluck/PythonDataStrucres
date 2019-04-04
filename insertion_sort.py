list = [10,25,32,29,1,76,53,69,70]

def insertion_sort(list):
    seq = list[:]
    n = len(seq)
    for i in range(1,n):
        value = seq[i]
        position = i
        while position > 0 and value < seq [position -1 ]:
            seq[position] = seq[position -1]
            position -=1
        seq[position] = value
        print(seq)

insertion_sort(list)
