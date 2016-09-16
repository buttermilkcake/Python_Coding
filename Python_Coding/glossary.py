from collections import OrderedDict

glossary = OrderedDict()

glossary['dictionary'] = 'a collection of key-value pairs'
glossary['boolean_expression'] = 'a condtional test'
glossary['immutable'] = 'values that cannot change'
glossary['tuple'] = 'an immutable list'

for word, definition in glossary.items():
    print("A " + word + " is a " + definition + ".")
      
