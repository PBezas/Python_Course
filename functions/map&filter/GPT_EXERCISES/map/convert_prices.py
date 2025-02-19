# You have a dictionary of products with their prices in USD:

products = [
  {'name': 'apple', 'price': '1.5$'},
  {'name':'banana', 'price': '0.8$'},
  {'name':'orange', 'price': '1.2$'},
  {'name': 'grape', 'price': '2.5$'}
  ]

# Use map() to convert the prices to EUR (assume 1 USD = 0.92 EUR).

# 1$ = 0.92€
def convert_prices(products):
  return list(map(lambda p: {'name': p['name'], 'price': f"{round(float(p['price'][0:-1]),2)}€"}, products))

converted_products = convert_prices(products)

print(converted_products)


# float(products[0]['price'][0:-1]

# print(round(float(products[0]['price'][0:-1]) * 0.92, 2))


