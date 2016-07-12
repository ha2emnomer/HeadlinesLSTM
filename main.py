import load_datasets
import em_model
from sklearn.cross_validation import train_test_split
maxepochs=60
batch_size=128
test_split_ratio=0.33
maxlen = 10
minlen =6
x,y,words,indices_words=load_datasets.LoadDatasets(maxlen,minlen)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_split_ratio, random_state=42)
model = em_model.buildmodel(words,128,128,maxlen)
model =em_model.train(model,x_train,y_train,maxepochs,maxlen,'headlinesemb_gen')
em_model.Generateheadline(100,model,maxlen,indices_words)
