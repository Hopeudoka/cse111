#for the "exceeding the requirements" section, i added a new function called get_adjective() and called it in the make_sentence() function.

import random

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    cap_word = word.capitalize()
    return cap_word


def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "Happy", "Bright", "Tall", "Soft", "Loud", "Quick", "Smooth", "Fresh", "Bitter", "Lazy"
    Return: a randomly chosen adjective.
    """
     
    adjectives = ["happy", "bright", "tall", "soft", "loud", "quick", "smooth", "fresh", "bitter", "lazy"]
    adjective = random.choice(adjectives)
    return adjective


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.lower() == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense.lower() == "present" and (quantity == 1):
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense.lower() == "present" and (quantity != 1):
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense.lower() == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb



def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    #randomly choose and return a preposition
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """

    if quantity == 1:
        phrase = f"{get_preposition()} {get_determiner(1).lower()} {get_noun(1)}"
    elif quantity != 1:
        phrase = f"{get_preposition()} {get_determiner(2).lower()} {get_noun(2)}"

    period_phrase = f"{phrase}"
    return period_phrase


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(1)
    determiner_plural = get_determiner(2)
    noun = get_noun(1)
    noun_plural = get_noun(2)
    verb_past = get_verb(1, "past")
    verb_single_present = get_verb(1, "present")
    verb_plural_present = get_verb(2, "present")
    verb_future = get_verb(1, "future")
    phrase_single = get_prepositional_phrase(1)
    phrase_plural = get_prepositional_phrase(2)
    adjective = get_adjective()
    

    if quantity == 1 and (tense.lower() == "past"):
        sentence = f"{determiner} {adjective} {noun} {verb_past} {phrase_single}."
    elif quantity != 1 and (tense.lower() == "past"):
        sentence = f"{determiner_plural} {adjective} {noun_plural} {verb_past} {phrase_plural}."
    elif quantity == 1 and (tense.lower() == "present"):
        sentence = f"{determiner} {adjective} {noun} {verb_single_present} {phrase_single}."
    elif quantity != 1 and (tense.lower() == "present"):
        sentence = f"{determiner_plural} {adjective} {noun_plural} {verb_plural_present} {phrase_plural}."
    elif quantity == 1 and (tense.lower() == "future"):
        sentence = f"{determiner} {adjective} {noun} {verb_future} {phrase_single}."
    elif quantity != 1 and (tense.lower() == "future"):
        sentence = f"{determiner_plural} {adjective} {noun_plural} {verb_future} {phrase_plural}."
    
    return sentence


main()
