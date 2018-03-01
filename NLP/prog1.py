from nltk import word_tokenize
from nltk.util import ngrams
from nltk.probability import FreqDist
from nltk.corpus import inaugural

def get_ngram(tokens, i):
    print('\n',i,'_Grams:\n')
    grams=ngrams(tokens,i)
    gramslist = list(grams)
    freq = FreqDist(gramslist)
    print(gramslist)
    print('\n\n')
    print(freq.items())
    print('\n\n')
    problist = [(i,freq[i]/len(gramslist)) for i in gramslist]
    print('Probability-', problist)


file_content = open("input_text.txt").read()
tokens = word_tokenize(file_content)
print('\nTokens List:\n')
print(tokens)

get_ngram(tokens, 3)

obwords = word_tokenize(inaugural.raw('2009-Obama.txt'))
waswords = word_tokenize(inaugural.raw('1789-Washington.txt'))
print('\n\nOBAMA')
ob = FreqDist(obwords)
print('No. of words:', len(obwords))
print('No. of distinct words:', len(ob.keys()))

sortob = sorted(ob.items(), key=lambda x:x[1])
print('\n\nOBAMA50-', sortob[-50:])

was = FreqDist(waswords)
sortwas = sorted(was.items(), key=lambda x:x[1])
print('\n\nWASHINGTON0-', sortob[-50:], '\n\n')

obuni = FreqDist(list(ngrams(obwords, 1)))
obbi =  FreqDist(list(ngrams(obwords, 2)))
obtri = FreqDist(list(ngrams(obwords, 3)))
sortobuni = sorted(obuni.items(), key=lambda x:x[1])
sortobbi = sorted(obbi.items(), key=lambda x:x[1])
sortobtri = sorted(obtri.items(), key=lambda x:x[1])

print("Unigrams: ", sortobuni[-10:])
print("Bigrams: ", sortobbi[-10:])
print("Trigrams: ", sortobtri[-10:])

