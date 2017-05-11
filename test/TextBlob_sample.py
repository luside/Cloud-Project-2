'''
install guide
$ pip install -U textblob
$ python -m textblob.download_corpora
'''
from textblob import TextBlob
analysis = TextBlob("I hate deadline")
print(analysis.sentiment.polarity)

#print -0.8