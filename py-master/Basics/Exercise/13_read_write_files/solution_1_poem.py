def occurance():
    dct = dict()
    f = open("poem.txt", "r")
    for line in f:
        tokens = line.split(" ")
        for token in tokens:
            if token in dct:
                dct[token] += 1
            else:
                dct[token] = 1

    f.close()
    max_occurance = max(list(dct.values()))
    print(max_occurance)
    for key, value in dct.items():
        if value == max_occurance:
            print(key)

def main():
    occurance()

if __name__ == "__main__":
    main()