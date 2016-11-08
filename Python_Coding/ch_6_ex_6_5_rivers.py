rivers = {'nile': 'egypt',
          'rhine': 'germany',
          'yangtze': 'china',
          }

for name, country in rivers.items():
    print("The " + name.title() + " is located in " + country.title() + ".")

for name in rivers:
    print(name.title())

for country in rivers.values():
    print(country.title())
