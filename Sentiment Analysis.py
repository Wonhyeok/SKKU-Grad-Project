from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

f=open('C:\\Users\\BSE\\Desktop\\csgraduation\\MammaMialyrics.txt','r')
lyriclines=f.readlines()
for lyricline in lyriclines:
    sentences=lyricline
    line = tokenize.sent_tokenize(sentences)


    sid = SentimentIntensityAnalyzer()
    for sentence in line:
        print(sentence)
        ss=sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()
