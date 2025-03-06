import re

text = 'You can find me in 555 235-5236 or 555 256-1562'
text2 = '555 235-5236'
phone_pattern = re.compile(r'\b\d{3} \d{3}-\d{4}\b')

# findall stores every match object inside a list (more memory consuming)
def extract_all_phones(input):
  return phone_pattern.findall(input)

phone_nums = extract_all_phones(text)
print(phone_nums) 

# with finditer iterator that yields one match object at the time in every iteration (less memory consuming)
def extract_all_phones(input):
  return [match.group() for match in phone_pattern.finditer(input)]

phone_nums = extract_all_phones(text)
print(phone_nums)

def validate_phone_number(input):
  valid_phone_pattern = re.compile(r'^\d{3} \d{3}-\d{4}$')
  if valid_phone_pattern.match(input):
    return True
  return False

print(validate_phone_number(text)) # False
print(validate_phone_number(text2)) # True