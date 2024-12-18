with open ('day1_input.txt', 'r') as f:
    ints1 = []
    ints2 = []
    line = f.readline()
    while line != '':
        a = (line.strip().split('   ')[0])
        b = (line.strip().split('   ')[1])
        ints1.append(int(a))
        ints2.append(int(b))
        line = f.readline()
    

def distance_lists(list1, list2):
    list1.sort()
    list2.sort()
    distance = 0
    for x in range(len(list1)):
        distance += abs(list1[x] - list2[x])
    return distance

def similarity_score(list1, list2):
    similarity = 0
    for i in list1:
        similarity += (i*list2.count(i))
    return similarity
        



def main():
    print(distance_lists(ints1, ints2))
    print(similarity_score(ints1, ints2))


if __name__ == "__main__":
    main()