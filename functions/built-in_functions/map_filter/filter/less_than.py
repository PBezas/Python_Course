# Given the products:
# 
# products = {"apple": 1.5, "banana": 0.8, "orange": 1.2, "grape": 2.5}
# 
# use filter() to keep only the products that cost more than $1.

products = {"apple": 1.5, "banana": 0.8, "orange": 1.2, "grape": 2.5}

def filter_products(products): 
  return dict(filter(lambda p: p[1]<1, products.items()))

print(filter_products(products))
