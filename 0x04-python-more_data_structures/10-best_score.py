#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    return max(a_dictionary, key=a_dictionary.get)
    return [key  for (key, value) in a_dictionary.items() if value == max(a_dictionary.values())]
