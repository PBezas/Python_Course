# statistics
# Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.

# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)

# ---------- My Way -----------------------


def statistics(f_name):
    with open(f_name) as file:
        lines = file.readlines()

    words = 0
    chars = 0
    for line in lines:
        chars += len(line)
        words += len(line.split(" "))

    return {"lines": len(lines), "words": words, "chars": chars}


print(statistics("file_io/story.txt"))


# ---------- Colt's Way ---------------------


def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return {
        "lines": len(lines),
        "words": sum(len(line.split(" ")) for line in lines),
        "characters": sum(len(line) for line in lines),
    }
