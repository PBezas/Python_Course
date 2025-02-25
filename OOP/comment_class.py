# #It's time to define your own class! Suppose we're creating a social network application where users can comment on posts and photos.

# Create a class called Comment .  Each comment should have the following attributes:

# username  - the username of the person who created the comment (like "bluethecat")
# text  - the actual comment itself (like "omg so cute!" or "hahah")
# likes  - the number of likes the comment has.  Likes should default to 0.

# The following code should work:

# c = Comment("davey123", "lol you're so silly", 3)
# c. username       #"davey123"
# c. text           #"lol you're so silly"
# c.likes           #3
# another_comment = Comment("rosa77", "soooo cute!!!")
# another_comment.username        #"rosa77"
# another_comment.text            #"soooo cute!!!"
# another_comment.likes           #0


class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


user_comment = Comment("Mpokolis", "OMG! Amazing!!", 2)

print(f"User: {user_comment.username}")
print(f"Comment: {user_comment.text}")
print(f"Likes: {user_comment.likes}")
