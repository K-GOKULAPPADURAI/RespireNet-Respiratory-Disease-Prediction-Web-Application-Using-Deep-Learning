import tensorflow
from os import listdir
from os.path import isfile, join
import librosa
import librosa.display
import numpy as np
import pandas as pd

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.core.window import Window

#Window.size=(320,600)
username_input="""
MDTextField:
    
    hint_text: "Enter the file path"
    hint_text_size:30
    helper_text: "must be a text with file extension"
    helper_text_mode: "on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.8}
    size_hint_x:.5
    size_hint_y:.1
    font_size:'15sp'
    width:400
"""
def extract_features(file_name):
    max_pad_len = 862
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

def predicter(mypath):
    D_names = ['Bronchiectasis', 'Bronchiolitis', 'COPD', 'Healthy', 'Pneumonia', 'URTI']
    features = [] 
    data = extract_features(mypath)
    features.append(data)
    print('Finished feature extraction from ', mypath)
    features = np.array(features)

    # create object
    model=tensorflow.keras.Model()

    # assign location
    path='resp_model_300.h5'

    # save
    #model.load_model(path)


    model = tensorflow.keras.models.load_model(path)
    result=model.predict(np.array([features[0]]))
    dp=list(zip(D_names,list(*result)))
    s=''' '''
    for i,j in dp:
        print(i,':',j)
        s+=str(i)+':'+str(j)+'\n'
    res=max(dp,key=lambda x:x[1])
    print('The predicted Disease for the patient was:',res[0],':{:.2f}'.format(res[1]),'%')
    ss=str(res[0])+':{:.2f}'.format(res[1])+'%'
    r=s,ss
    return  r
class DemoApp(MDApp):    
    def build(self):
        self.screen=Screen()
        self.theme_cls.primary_palette = "Green"
        self.label = MDLabel(text="RESPIRATORY DISEASE PREDICTION", halign="center",theme_text_color='Custom',
                        text_color=(0,1,0,1),font_style='H4',pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.username = Builder.load_string(username_input)
        self.btn = MDRectangleFlatButton(text='Test',font_size='20sp',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.1},size_hint=(.2, .1)
                                             ,on_release=self.mul)
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.username)
        self.screen.add_widget(self.btn)
        return self.screen
    def mul(self,obj):
        self.screen.remove_widget(self.label)
        self.screen.remove_widget(self.username)
        self.screen.remove_widget(self.btn)
        print(self.username.text,type(self.username.text))
        r=predicter(str(self.username.text))
        self.label1 = MDLabel(text="PREDICTION RESULTS", halign="center",theme_text_color='Custom',
                        text_color=(0,1,0,1),font_style='H4',pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.label_1 = MDLabel(text="PREDICTED DISEASE:   "+str(r[1]), halign="center",theme_text_color='Custom',
                        text_color=(1,0,0,1),font_style='H5',pos_hint={'center_x': 0.5, 'center_y': 0.4})
        c=(0,1,0,1)
        self.label2 = MDLabel(text=str(r[0]), halign="center",theme_text_color='Custom',
                        text_color=(0,0,1,1),font_style='H6',pos_hint={'center_x': 0.5, 'center_y': 0.7})
##        self.label12 = MDLabel(text=str(r[1]), halign="center",theme_text_color='Custom',
##                        text_color=c,font_style='H4',pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.button = MDRectangleFlatButton(text='Back',
                                       pos_hint={'center_x': 0.8, 'center_y': 0.1   },
                                            on_release=self.back)
        self.screen.add_widget(self.label1)
        self.screen.add_widget(self.label_1)
        self.screen.add_widget(self.label2)
        #self.screen.add_widget(self.label12) 
        self.screen.add_widget(self.button)
    def back(self,obj):
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.username)
        self.screen.add_widget(self.btn)
        self.screen.remove_widget(self.button)
        self.screen.remove_widget(self.label1)
        self.screen.remove_widget(self.label2)
        self.screen.remove_widget(self.label_1)
        #self.screen.remove_widget(self.label12)
        self.screen.remove_widget(self.button)
DemoApp().run()
#archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pr_sc_Litt3200.wav
