midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# zip these lists together making a dict where key will be the name and value will be the highest score for each student in order

# expected output: {dan: 98, ang: 91, kate: 78}

# -----------------------1st way(MY SOLUTION)----------------------------------

final_grades = dict(
  zip(
    students, 
    list(max(num) for num in zip(midterms, finals))
  )
)

# -----------------------2nd way-----------------------------------------------

                                                      # [('dan',80,98), ('ang', 91, 89), ('kate', 78, 53)]
final_grades = {tup[0]:max(tup[1], tup[2]) for tup in zip(students, midterms, finals)}

# -----------------------3rd way(VERY SIMILAR TO MINE)--------------------------

final_grades = dict(zip(students, map(lambda pair: max(pair), zip(midterms, finals))))

# print(final_grades)

# zip these lists together making a dict where key will be the name and value will be the average score for each student in order

final_averages = dict(
  zip(
    students, 
    list(round(sum(scores_pair) / len(scores_pair)) for scores_pair in zip(midterms, finals))
    )
)

print(final_averages)