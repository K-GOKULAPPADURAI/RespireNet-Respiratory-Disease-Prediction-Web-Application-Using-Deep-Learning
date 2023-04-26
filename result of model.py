# import module
import tensorflow
from os import listdir
from os.path import isfile, join
import librosa
import librosa.display
import numpy as np
import pandas as pd
max_pad_len = 862
def extract_features(file_name):
    """
    This function takes in the path for an audio file as a string, loads it, and returns the MFCC
    of the audio"""
   
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast', duration=20) 
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        pad_width = max_pad_len - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
        
    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None 
    return mfccs
D_names = ['Bronchiectasis', 'Bronchiolitis', 'COPD', 'Healthy', 'Pneumonia', 'URTI']
mypath = "archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/"
filenames = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith('.wav'))] 


features = [] 
filepaths = [join(mypath, f) for f in filenames] # full paths of files

# Iterate through each sound file and extract the features
i=0
for file_name in filepaths[71:]:
    data = extract_features(file_name)
    features.append(data)
    if(i==20):
        break
    i+=1

print('Finished feature extraction from ', len(features), ' files')
features = np.array(features)

# create object
model=tensorflow.keras.Model()

# assign location
path='resp_model_300.h5'

# save
#model.load_model(path)


model = tensorflow.keras.models.load_model(path)
for i in range(1):
    result=model.predict(np.array([features[i]]))
    dp=list(zip(D_names,list(*result)))
    #print("Welcome to Respiratory Disease prediction".center(30,'#'))
    #print('Person had the posibilities of Diseases in percentage')
    for i,j in dp:
        print(i,':',j)
    res=max(dp,key=lambda x:x[1])
    print('The predicted Disease for the patient was:',res[0],':{:.2f}'.format(res[1]),'%')
    #print(max(result[0]))
    #print(result)

'''archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pr_sc_Litt3200.wav'''
