# Regex Profanity Filter
# Define a function called censor  that accepts a single string. Rather than censoring any real profanity, we're going to censor any words that start with "frack".  This includes "fracking", "fracker", "frack", etc.  Replace the entire word with the string "CENSORED".  Your regex should be case insensitive. For example:

# censor("Frack you")                #"CENSORED you"
# censor("I hope you fracking die")  #"I hope you CENSORED die"
# censor("you fracking Frack")       #"You CENSORED CENSORED"

import re

def censor(str):
  censor_pattern = re.compile(r'\bfrack\w*\b', re.I)

  result = censor_pattern.sub('CENSORED', str)

  return result

print(censor("Frack you") )
print(censor("I hope you fracking die"))
print(censor("you fracking Frack") )
print(censor('sexy and befracking delicious'))
