def main():
    reviewfile = "reviewfile.txt"
    # string -> [int]
    wordmap = {}
    reviews = []

    with open(reviewfile, 'r') as f:
        idx = 0
        for line in f:
            reviews.append(line.rstrip())
            words = line.rstrip().split(' ')
            for word in words:
                if word.lower() not in wordmap:
                    wordmap[word.lower()] = [idx]
                else:
                    wordmap[word.lower()].append(idx)
            idx = idx + 1

    user = raw_input("Enter word: ")
    while user != "":
        print user, "appears in:"
        for idx in wordmap[user]:
            print reviews[idx]
        user = raw_input("Enter word: ")



if __name__ == '__main__':
    main()