test = {
    "name": "Dictionaries WWPD",
    "points": 0,
    "suites": [
        {
            "type": "wwpp",
            "cases": [
                {
                    "code": """
          >>> pokemon = {'pikachu': 25, 'dragonair': 148}
          >>> pokemon
          {'pikachu': 25, 'dragonair': 148}
          >>> 'mewtwo' in pokemon
          False
          >>> len(pokemon)  
          2
          >>> pokemon['mew'] = pokemon['pikachu']   #If this errors, just type Error
          >>> pokemon[25] = 'pikachu'
          >>> pokemon
          {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu'}
          >>> pokemon['mewtwo'] = pokemon['mew'] * 2  
          >>> pokemon
          {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu', 'mewtwo': 50}
          >>> pokemon[['firetype', 'flying']] = 146  # If this errors, just type Error. Note that dictionary keys must be hashable.
          Error
          """,
                }
            ],
        },
        # {
        #     "type": "wwpp",
        #     "cases": [
        #         {
        #             "code": """
        #   >>> letters = {'a': 1, 'b': 2, 'c': 3}
        #   >>> 'a' in letters
        #   True
        #   >>> 2 in letters
        #   False
        #   >>> sorted(list(letters.keys()))
        #   ['a', 'b', 'c']
        #   >>> sorted(list(letters.items()))
        #   [('a', 1), ('b', 2), ('c', 3)]
        #   """,
        #         }
        #     ],
        # },
    ],
}