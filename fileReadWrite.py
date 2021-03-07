with open("fileRead_intro.txt", mode="r") as i_file:
    words_all = []
    for line in i_file.readlines():
        # print(line, end="")
        # stripped_string = line.strip()
        words = line.strip().split(" ")
        words_all += words
        # print(words)

    print(words_all)
    print(len(words_all))

    unique_words = set(words_all)
    print(len(unique_words))

    with open("unique.txt", mode="w") as fileWrite:
        for item in sorted(unique_words):
            fileWrite.write(item)
            fileWrite.write("\n")




