group1 = [3, 4, 2, 1, 3, 3]
group2 = [4, 3, 5, 3, 9, 3]


def distance_lists(list1, list2):
    list1.sort()
    list2.sort()
    distance = 0
    for x in range(len(list1)):
        distance += abs(list1[x] - list2[x])
    return distance

def main():
    print(distance_lists(group1, group2))


if __name__ == "__main__":
    main()