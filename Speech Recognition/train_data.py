# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:47:05 2022

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.io import wavfile
from scipy import signal
import librosa, librosa.display
import pandas as pd
from scipy.fftpack import fft

frequency_sampling, audio_signal = wavfile.read("Recording.wav")

# Normalleştirme yapıyoruz
audio_signal = audio_signal / np.power(2, 20)


############# Time Domain - 1
time_axis = 1 * np.arange(0, len(audio_signal), 1) / float(frequency_sampling)
f= plt.plot(time_axis, audio_signal, color='blue')
plt.title('First Time-Amplitude')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()
############# Time Domain - 2 Plot
N = len(audio_signal)
time = np.linspace(0, 60, N)
f1= plt.plot (time, audio_signal)
plt.title ('Time Domain Signal')
plt.xlabel ('Time')
plt.ylabel ('Amplitude')
plt.show ()
############# Frequency Domain Plot
frequency = np.linspace (0.0, frequency_sampling/2, int (N/2))
freq_data = fft(audio_signal)
y = 2/N * np.abs (freq_data [0:int (N/2)])
f2= plt.plot(frequency[1000:1200], y[1000:1200])
plt.title('Frequency Domain Signal')
plt.xlabel('Frequency in Hz')
plt.ylabel("Amplitude")
plt.show()

############# Sinyalin STFT sini buluyoruz ve çizdiriyoruz.
sr = 44100
hop_length = 256
n_fft = 2048
X = librosa.stft(audio_signal, n_fft=n_fft, hop_length=hop_length)
S = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(15, 5))
librosa.display.specshow(S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.show()
############# zero array oluşturuyoruz. Labellar için.
arr = np.zeros( (len(S[1]), ) , dtype=np.int64)
#5168/60 = 86.1 , stft grafiğinde nokta belirle(x) , sonra 86 ile çarp
arr[0:195]=0 # 0 , 3
#1
arr[195:255]=1   # 3    , 4
arr[255:390]=0   # 4    , 6
arr[390:480]=2   # 6    , 7
arr[480:528]=0   # 7    , 10
arr[840:960]=3   # 10   , 11.3
arr[894:963]=0  # 11.3 , 11.5
arr[1049:1100]=4 # 11.5 , 12
arr[1212:1272]=0 # 12   , 13.2
arr[1367:1427]=5 # 15   , 16
arr[1530:1599]=0 # 16   , 17.9
arr[1694:1763]=6 # 17.9 , 19.4
arr[1694:1763]=0 # 19.4 , 20.9
arr[1831:1900]=7 # 20.9 , 22.2

arr[1965:2029]=0 # 22.2 , 27.8
#2
arr[2094:2154]=1 # 27.8 , 28
arr[2227:2287]=0 # 28   , 31
arr[2356:2412]=2 # 31   , 32.1
arr[2481:2532]=0 # 32.1 , 34
arr[2610:2661]=3 # 34   , 35
arr[2734:2786]=0 # 35   , 37
arr[2842:2898]=4 # 37   , 38.5
arr[2971:3022]=0 # 38.5 , 41
arr[3078:3139]=5 # 41   , 41.9
arr[3182:3237]=0 # 41.9 , 44.6
arr[3182:3237]=6 # 44.6 , 45.2
arr[3182:3237]=0 # 45.2 , 46.3
arr[3403:3418]=7 # 46.3 , 46.9

arr[3418:3770]=0 # 46.9 , 51.3
#3
arr[3770:3888]=1 # 51.3 , 52.9
arr[3888:3984]=0 # 52.9 , 54.2
arr[3984:4101]=2 # 54.2 , 55.8
arr[4101:4263]=0 # 55.8 , 58
arr[4263:4329]=3 # 58   , 58.9
arr[4329:4454]=0 # 58.9 , 60.6
arr[4454:4512]=4 # 60.6 , 61.4
arr[4512:4645]=0 # 61.4 , 63.2
arr[4645:4726]=5 # 63.2 , 64.3
arr[4726:4843]=0 # 64.3 , 65.9
arr[4843:4887]=6 # 65.9 , 66.5
arr[4887:5020]=0 # 66.5 , 68.3
arr[5020:5071]=7 # 68.3 , 69
arr[5071:5373]=0 # 69   , 73.1
arr[5373:5439]=1 # 73.1 , 74
arr[5439:5644]=0 # 74   , 76.8
arr[5644:5725]=2 # 76.8 , 77.9
arr[5725:5895]=0 # 77.9 , 80.2
arr[5895:5983]=3 # 80.2 , 81.4
arr[5982:6115]=0 # 81.4 , 83.2
arr[6115:6181]=4 # 83.2 , 84.1
arr[6181:6358]=0 # 84.1 , 86.5
arr[6358:6417]=5 # 86.5 , 87.3
arr[6417:6762]=0 # 87.3 , 92
arr[6762:6814]=6 # 92   , 92.7
arr[6814:6967]=0 # 92.7 , 94.8
arr[6967:6997]=7 # 94.8 , 95.2
arr[6997:7247]=0 # 
arr[7247:7328]=1 # 98.6 , 99.7
arr[7328:7497]=0 # 
arr[7497:7497]=2 # 102 , 103
arr[7497:7717]=0 # 
arr[7717:7791]=3 # 105 , 106
arr[7791:7938]=0 # 
arr[7938:8011]=4 # 108 , 109
arr[8011:8159]=0 # 
arr[8159:8232]=5 # 111 , 112
arr[8232:8453]=0 # 
arr[8453:8526]=6 # 115 , 116
arr[8526:8673]=0 # 
arr[8673:8820]=7 # 118,  120

arr[8820:8967]=0 # 

arr[8967:9114]=1 # 122 , 124
arr[9114:9188]=0 # 
arr[9188:9335]=2 # 125, 127
arr[9335:9482]=0 # 
arr[9482:9555]=3 # 129 , 130
arr[9555:9702]=0 # 
arr[9702:9776]=4 # 132 , 133
arr[9776:9849]=0 # 
arr[9849:9923]=5 # 134 , 135
arr[9923:10143]=0 # 
arr[10143:10144]=6 # 138 , 140
arr[10144:10363]=0 # 
arr[10363:10438]=7 # 141,  142
## X ve y'mizi tanımlıyoruz.
X = S
y = arr

# data kaydetme
"""
df_data = pd.DataFrame(data=X)
df_data.to_csv(r'final-project\dataset.csv',index=False,header=True)
"""

######################## MACHINE LEARNING ########################
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.metrics import plot_confusion_matrix

#denenecek modellerin yüklenmesi
models = []
models.append(('RF', RandomForestClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('DT', DecisionTreeClassifier()))
models.append(('SVC', SVC()))

# Confusion Matrix için labelları listeye ekliyoruz.
#wait,  read: "computer", read: "engineering",  say your name,  say your last name,  cough once, ,  clap your hands once, wait,  snap your fingers once, wait 
labels_y = ['wait','computer','engineering','Name','Tan','cough','clap','finger_snap']

# modellerin sınanması
results = []
names = []

##### csv ye kaydetmek için gerekli listeler
kfolds = []
acc = [] 
micro_ps = []
micro_rs = [] 
micro_f1 = [] 
macro_ps = [] 
macro_rs = [] 
macro_f1 = [] 
weighted_ps = [] 
weighted_rs = [] 
weighted_f1 = [] 

validation_size = 0.20
seed = 7
num_folds = 10
RMS = 'neg_mean_squared_error'

# Datayı %20 test %80 train olacak şekilde ayırıyoruz.
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = validation_size,random_state = seed)
"""
# test verisinin çıkarımı
scaler = StandardScaler().fit(X_train)
rescaledX_train = scaler.transform(X_train)
# transform the validation dataset
X_test_rescaled = scaler.transform(X_test)
"""
# Machine Learning uyguladığımız yer.
for modelName , model in models:
    print(modelName+" kfold eğitiliyor")
    
    # kfold kısmı 'neg_mean_squared_error' kullanıyoruz
    kfold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring=RMS)
    results.append(cv_results)
    names.append(modelName)
    
    # Modeli eğitiyoruz.
    print(modelName+" normal eğitiliyor")
    model.fit(X_train,y_train)
    # Modelde test datasını deneyerek tahmin değerlerini alıyoruz.
    y_pred = model.predict(X_test)

    # precision, recall, f1, accuracy skorları hesaplıyoruz.
    ACC = accuracy_score(y_test,y_pred) 
    PS_mi = precision_score(y_test,y_pred,average='micro')
    RS_mi = recall_score(y_test,y_pred,average='micro')
    F1_mi = f1_score(y_test,y_pred,average='micro')
    
    PS_ma = precision_score(y_test,y_pred,average='macro')
    RS_ma = recall_score(y_test,y_pred,average='macro')
    F1_ma = f1_score(y_test,y_pred,average='macro')
    
    PS_we = precision_score(y_test,y_pred,average='weighted')
    RS_we = recall_score(y_test,y_pred,average='weighted')
    F1_we = f1_score(y_test,y_pred,average='weighted')
    
    print(modelName + "-" + " kfold neg_mean_score = " + str(cv_results.mean()))
    print(modelName + "-" + " accuracy_score = % " + str(ACC*100))
    print(modelName + "-" + " precision_score micro = % " + str(PS_mi*100))
    print(modelName + "-" + " recall_score micro = % " + str(RS_mi*100))
    print(modelName + "-" + " f1_score micro = % " + str(F1_mi*100))
    
    print(modelName + "-" + " precision_score macro = % " + str(PS_ma*100))
    print(modelName + "-" + " recall_score macro = % " + str(RS_ma*100))
    print(modelName + "-" + " f1_score macro = % " + str(F1_ma*100))
    
    print(modelName + "-" + " precision_score weighted = % " + str(PS_we*100))
    print(modelName + "-" + " recall_score weighted = % " + str(RS_we*100))
    print(modelName + "-" + " f1_score weighted = % " + str(F1_we*100))
    print(modelName," mse:", mean_squared_error(y_test, y_pred)) 
    
    # Confusion Matrix tablosu oluşturuyoruz.
    plot_confusion_matrix(model, X_test, y_test, display_labels=labels_y, xticks_rotation="vertical")
    plt.savefig(modelName +'.png')
        
    # Bu kısım modelin daha sonra da kullanılabilmesi için kayıt yapmaktadır.
    import pickle
    filename = modelName+'_scaled''_model.sav'
    pickle.dump(model , open(filename, 'wb'))
    
    ################################## Listelere sonuçları ekliyoruz.
    kfolds.append(cv_results.mean())
    acc.append(round(ACC*100, 2))
    micro_ps.append(round(PS_mi*100, 2))
    micro_rs.append(round(RS_mi*100, 2))
    micro_f1.append(round(F1_mi*100, 2))
    macro_ps.append(round(PS_ma*100, 2))
    macro_rs.append(round(RS_ma*100, 2))
    macro_f1.append(round(F1_ma*100, 2))
    weighted_ps.append(round(PS_we*100, 2))
    weighted_rs.append(round(RS_we*100, 2))
    weighted_f1.append(round(F1_we*100, 2))


################### Sonuçları csv ye kaydediyoruz.
d = {'Models': ['RF','KNN','DT','SVC'],'Kfold_NMSE': kfolds, 'Acc': acc, 'PS_micro': micro_ps, 'RS_micro': micro_rs,
      'F1_micro':micro_f1,'PS_macro':macro_ps,'RS_macro':macro_rs,'F1_macro':macro_f1,
      'PS_weighted':weighted_ps,'RS_weighted':weighted_rs,'F1_weighted':weighted_f1}

df_table = pd.DataFrame(data=d)
df_table.to_csv(r'table_no_scaled.csv',index=False,header=True)


