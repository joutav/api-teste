import string

from textblob import TextBlob


def polaridade_sentimento(frase: string):
    tb = TextBlob(frase).translate(to='en')
    return tb.sentiment.polarity
