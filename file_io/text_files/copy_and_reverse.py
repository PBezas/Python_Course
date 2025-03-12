# copy_and_reverse
# Write a function called copy_and_reverse, which takes in a file name and a new file name and copies the reversed contents of the first file to the second file.

# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)


def copy_and_reverse(f_name, new_f_name):
    with open(f_name) as file:
        data = file.read()

    with open(new_f_name, "w") as file:
        file.write(data[::-1])
