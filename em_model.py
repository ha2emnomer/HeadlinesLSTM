import  numpy as np
from keras.layers import LSTM, Dropout, TimeDistributed, Dense, Activation, Embedding, GRU
from keras.models import Sequential

import matplotlib.pylab as plt
def CreateSampleWeights(y,maxlen):
    sw = np.zeros((len(y), maxlen))
    for i in range(len(y)):
        for t, char in enumerate(y[i]):
            if(y[i,t,char]==1):
                sw[i,t]=1
    return sw


#x_train=sequence.pad_sequences(x_train,maxlen)
#x_test=sequence.pad_sequences(x_test,maxlen)
def buildmodel(words,embsize, hiddensize ,maxlen,name='headlines_gen',loadweights=False):
    model = Sequential()
    model.add(Embedding(words, embsize, input_length=maxlen,mask_zero=True))
    model.add(LSTM(hiddensize, return_sequences=True)) #,input_shape=(maxlen, 100)))
    model.add(Dropout(0.2))
    model.add(TimeDistributed(Dense(words)))
    model.add(Activation('softmax'))
    if(loadweights):
        model.load_weights(name)
    model.compile( sample_weight_mode="temporal",loss='categorical_crossentropy', optimizer='rmsprop')
    return model
def train(model,x_train,y_train,epochs,maxlen, name, batch_size=128):
    model.fit(x_train, y_train, batch_size=batch_size,
         sample_weight=CreateSampleWeights(y_train,maxlen),
     nb_epoch=epochs,validation_split=0.33)
    model.save_weights(name,overwrite=True)
def sample(a, temperature=1.0):
    a = np.log(a) / temperature
    a = np.exp(a) / np.sum(np.exp(a))
    return np.argmax(np.random.multinomial(1, a, 1))
def Generateheadline(sample_no,x_test,model,maxlen,indices_words):
    for j in range(100):
        input_pre = np.zeros((1,maxlen))
        input_pre[0]=x_test[j]
        pred= model.predict(input_pre,batch_size=1)
        headline = list(input_pre[0])
        headlinetext=''
        for word in range(len(headline)):
            if(headline[word]!=0.0):
                headlinetext= headlinetext +' '+indices_words[headline[word]]
        #headlinetext=headlinetext+'<'
        length=np.random.randint(1,10)
        for word in range(length):
            chart= list(pred[0,word])
            next_index = chart.index(max(chart)) #use sample instead to sample from probability distrbution
            headlinetext= headlinetext +' '+indices_words[next_index]
        print(headlinetext+'.')
    print('\n')