# JOIN SOUNDS ALONG WITH TURNING EACH ONE IN CAPITAL LETTERS

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# ----------------------1st way----------------------

# result = ''

# for sound in sounds:
#     result += sound.upper()

# print(result)

# ----------------------2nd way----------------------

# new_sounds = []

# for sound in sounds:
#   new_sounds.append(sound.upper())

# print(''.join(new_sounds))

# ----------------------3rd way----------------------

joined_sounds = ''.join(sound.upper() for sound in sounds)

print(joined_sounds)
