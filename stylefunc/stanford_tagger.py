from nltk.tag import StanfordNERTagger
from nltk.tag import StanfordPOSTagger

tagger="D:\\Hideko\\poo\\stanford-postagger\\models\\spanish.tagger"
jar="D:\\Hideko\\poo\\stanford-postagger\\stanford-postagger.jar"

etiquetador = StanfordPOSTagger(tagger, jar)

def get_stanford_tags(source):
    return etiquetador.tag(source)

def get_sort_stanford_tags(source):
    return etiquetador.tag(sorted(source))

