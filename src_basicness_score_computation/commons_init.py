from nltk.corpus import wordnet

synsets_da_evitare_1 = next(wordnet.all_synsets(pos="a"))
synsets_da_evitare_2 = next(wordnet.all_synsets(pos="s"))

SYNSET_DA_EVITARE = [
    next(wordnet.all_synsets(pos="a")), 
    next(wordnet.all_synsets(pos="s"))
]

SUPPORTED_POS = ['n'] # ci interessano solo i noun