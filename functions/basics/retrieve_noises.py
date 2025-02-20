noises = {
  'dog': 'woof',
  'pig': 'oink',
  'cat': 'meow',
  'duck': 'quack'
}

def retrieve_noises(animal = 'dog'):
  for key, value in noises.items():
    if key == animal:
      return value
  return '?'

print(retrieve_noises())
print(retrieve_noises('dog'))
print(retrieve_noises('pig'))
print(retrieve_noises('cat'))
print(retrieve_noises('duck'))
print(retrieve_noises('avocado'))

def speak(animal="dog"):
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

# speak()
    
  
    
    