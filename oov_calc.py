import json

f = open('single.json')

a = json.load(f)

#set of all the english words, the english sentences have only english words
set_english = set()
#the code mixed sentences have a mix of english and hindi words
set_both = set()


for i in a:
    english = i['sentence']
    mixed = i['code_mixed_sentence']

    #make a set
    for j in english.split():
        set_english.add(j)

    for k in mixed.split():
        set_both.add(k)

#Since we're considering common words to be IN VOCAB, and not OOV, we can safely remove all non english words from the set of both and they will be all hindi words
hindi_words = set_both.difference(set_english)



print(len(hindi_words) / len(set_both))