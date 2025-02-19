names = ['Charlie', 'Colt', 'Caisee', 'Costas']

# print(all([name for name in names if name[0].lower() == 'c']))

print(all([name[0]== 'C' for name in names]))