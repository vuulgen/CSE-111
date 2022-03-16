import random

def main():
    print(get_determiner(1).capitalize(), get_noun(1), get_verb(1,'past'), get_prepositional_phrase(1))
    print(get_determiner(1).capitalize(), get_noun(1), get_verb(1,'present'),get_prepositional_phrase(1))
    print(get_determiner(1).capitalize(), get_noun(1), get_verb(1,'future'), get_prepositional_phrase(1))
    print(get_determiner(2).capitalize(), get_noun(2), get_verb(2,'past'), get_prepositional_phrase(2))
    print(get_determiner(2).capitalize(), get_noun(2), get_verb(2,'present'), get_prepositional_phrase(2))
    print(get_determiner(2).capitalize(), get_noun(2), get_verb(2,'future'), get_prepositional_phrase(2))



def get_determiner(quantity):
   
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
  
    if quantity == 1:
        words = [ "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense == 'present' and quantity == 1:
        words = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == 'present' and quantity != 1:
        words = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        
    elif tense == 'future':
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    """ Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
#    the text above is where you stoped at.
        
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_preposition(prepositon):
     if prepositon == 1:
        words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

        # """Return: a randomly chosen preposition.
        # """
        word = random.choice(words)
        return word

def get_prepositional_phrase(quantity):
    if quantity == 1:
        # prepositinal_phrase = [get_preposition, get_determiner, get_noun]
        prepositinal_phrase = print(f'{get_preposition} {get_determiner(1)} {get_noun(1)}')
        prepositinal_phrase = (get_determiner(1).capitalize(), get_noun(1), get_verb(1,'past'))

    else:
        prepositinal_phrase = print(f'{get_preposition} {get_determiner(2)} {get_noun(2)}')
        # prepositinal_phrase = [get_preposition, get_determiner, get_noun]

        word = random.choice(prepositinal_phrase)
        return word
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
main()