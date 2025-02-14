kms = input('Type in the km you want to convert to miles: ')

answer = kms
print(f'Ok! You said {answer} km')


miles = float(answer) * 0.621371

print(f'Thas is equal to {round(miles, 2)} miles')
