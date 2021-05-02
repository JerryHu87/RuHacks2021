# Uses Noam Chomsky Syntactic Structures
# NP + VP
# (T + N) + (V + P)
import random as ran


# print(T, N)
def assemble(*args):
    return " ".join(args)


def NP(T, N):
    return assemble(T, N)


def VP(Verb, NP):
    return assemble(Verb, NP)


def sentence(NP, Adverb1, VP1):
    return assemble(NP, Adverb1, VP1+".")

# now i must make several different lists related to the different moods


def loop(X):
    T_1 = ['The', 'Their', 'Our', 'His', 'Her', 'That', 'This', 'Your']  # cap
    T_2 = ['the', 'their', 'our', 'his', 'her',
           'that', 'this', 'your']  # no cap

    N = ['man', 'ball', 'monkey', 'caroussel',
         'computer', 'edge', 'heart', 'guitar', 'fire']
    Verb = ['hit', 'polished', 'healed', 'tore', 'treated', 'coded', 'ran']

    # angry, joy, sorrow, surprised
    # Must put different conditional statements.
    angry_adverb = ['furiously', 'bitterly', 'terribly',
                    'violently', 'intensely', 'savagely']
    joy_adverb = ['joyfully', 'happily',
                  'cheerfully', 'merrily', 'ecstatically', 'gleefully', 'contentedly']
    sorrow_adverb = ['sadly', 'sorrowfully',
                     'dejectedly', 'gloomily', 'joylessly']

    surprised_adverb = ['suddenly', 'shockingly', 'surprisingly']

    for i in range(X):
        N1, N2 = ran.choice(N), ran.choice(N)
        T1, T2 = ran.choice(T_1), ran.choice(T_2)
        Adverb1 = ran.choice(joy_adverb)
        # need to make conditional statements dependent upon mood
        # if mood is happy, angry, sorrowful, adverb will be different
        Verb1 = ran.choice(Verb)

        NP1 = NP(T1, N1)
        NP2 = NP(T2, N2)
        VP1 = VP(Verb1, NP2)
        print(sentence(NP1, Adverb1, VP1))


# So what I'm thinking is the user will decide how many sentences they want to generate.
X = int(input("How many sentences would you like to generate for your caption? "))
result = loop(X)  # generates X amount of sentence
