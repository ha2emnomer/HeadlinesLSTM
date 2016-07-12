import  numpy as np
def LoadDatasets(maxlen,minlen):
    text=''
    words=set()
    files = ['dataset_bbc.txt', 'datasetcnbc.txt', 'dataset_ellie_vice.txt', 'dataset_foxnews.txt'
            ,'dataset_nytimes.txt','dataset_pcmag.txt',
           'dataset_ted.txt',
            'dataset_time.txt','dataset_slate.txt','dataset_vhl.txt'
             ]
    path ='news_datasets/'
    for file in files:
     text = text +open(path+file).read().lower()
    sentences=text.split("\n")
    for s in text.split("\n"):
        #if(len(s.split(" ")) >= maxlen):
        #    maxlen=len(s.split(" "))
        for word in s.split(" "):
            words.add(word)
    print('total words:', len(words))
    words_indices = dict((c, i) for i, c in enumerate(words))
    indices_words = dict((i, c) for i, c in enumerate(words))
    X = np.zeros((len(sentences), maxlen), dtype=np.int32)
    y = np.zeros((len(sentences), maxlen, len(words)), dtype=np.bool)
    print('Vectorization...')
    for i, sentence in enumerate(sentences):
        for t , word in enumerate(sentence.split(" ")[0:minlen]):
            X[i, t] = words_indices[word]
        for t ,char in enumerate(sentence.split(" ")[minlen:maxlen]):
            y[i, t, words_indices[char]] = 1
    return X ,y,len(words),indices_words
