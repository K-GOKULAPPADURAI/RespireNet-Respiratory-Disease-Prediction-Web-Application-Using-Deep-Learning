Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 5, in <module>
    filenames = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith('.wav'))]
NameError: name 'listdir' is not defined
>>> 
= RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 17, in <module>
    data = extract_features(file_name)
NameError: name 'extract_features' is not defined
>>> 
= RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Al_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Pr_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/102_1b1_Ar_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/103_2b2_Ar_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Al_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Ar_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Ll_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Lr_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pl_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pr_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/105_1b1_Tc_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/106_2b1_Pl_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/106_2b1_Pr_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Al_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Ar_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Ll_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Lr_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Pl_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Pr_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Tc_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b4_Al_mc_AKGC417L.wav
Finished feature extraction from  21  files
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 51, in <module>
    model.load_weights(path)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 3023, in load_weights
    "Unable to load weights saved in HDF5 format into a "
ValueError: Unable to load weights saved in HDF5 format into a subclassed Model which has not created its variables yet. Call the Model first, then load the weights.
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Al_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Pr_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/102_1b1_Ar_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/103_2b2_Ar_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Al_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Ar_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Ll_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Lr_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pl_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pr_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/105_1b1_Tc_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/106_2b1_Pl_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/106_2b1_Pr_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Al_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Ar_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Ll_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Lr_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Pl_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Pr_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Tc_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b4_Al_mc_AKGC417L.wav
Finished feature extraction from  21  files
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 51, in <module>
    model.load_model(path)
AttributeError: 'Model' object has no attribute 'load_model'
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Al_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Pr_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/102_1b1_Ar_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/103_2b2_Ar_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Al_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Ar_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Ll_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Lr_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pl_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pr_sc_Litt3200.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/105_1b1_Tc_sc_Meditron.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/106_2b1_Pl_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/106_2b1_Pr_mc_LittC2SE.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Al_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Ar_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Ll_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Lr_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Pl_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Pr_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b3_Tc_mc_AKGC417L.wav
Error encountered while parsing file:  archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/107_2b4_Al_mc_AKGC417L.wav
Finished feature extraction from  21  files
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 52, in <module>
    savedModel = model.load_weights(path)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 3023, in load_weights
    "Unable to load weights saved in HDF5 format into a "
ValueError: Unable to load weights saved in HDF5 format into a subclassed Model which has not created its variables yet. Call the Model first, then load the weights.
>>> features
array([None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None],
      dtype=object)
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 53, in <module>
    savedModel = model.load_weights(path)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 3023, in load_weights
    "Unable to load weights saved in HDF5 format into a "
ValueError: Unable to load weights saved in HDF5 format into a subclassed Model which has not created its variables yet. Call the Model first, then load the weights.
>>> features

>>> features[0]
array([[-4.25929626e+02, -4.74543427e+02, -5.26268555e+02, ...,
        -5.21922974e+02, -5.18371826e+02, -5.24104553e+02],
       [ 7.59593506e+01,  9.57673111e+01,  1.07862137e+02, ...,
         1.13700607e+02,  1.18766586e+02,  1.06290695e+02],
       [ 7.67765198e+01,  8.34067230e+01,  7.01855469e+01, ...,
         7.70387115e+01,  8.18043213e+01,  7.64635773e+01],
       ...,
       [ 3.02516103e-01,  7.77786791e-01,  3.45391810e-01, ...,
        -6.93254948e+00, -3.68614340e+00, -1.21863639e+00],
       [ 3.72309828e+00,  4.03583717e+00,  2.32282257e+00, ...,
        -2.24807978e+00, -2.22762990e+00, -9.33637738e-01],
       [ 2.72636032e+00,  3.96600580e+00,  4.09331608e+00, ...,
         3.13393116e+00, -9.88742232e-01, -4.00402451e+00]], dtype=float32)
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 54, in <module>
    model = tensorflow.keras.models.load_model('path/to/location')
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\saving\legacy\save.py", line 228, in load_model
    f"No file or directory found at {filepath_str}"
OSError: No file or directory found at path/to/location
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py", line 56, in <module>
    print(savedModel.predict(np.array([features[11]])))
AttributeError: 'NoneType' object has no attribute 'predict'
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
1/1 [==============================] - ETA: 0s1/1 [==============================] - 0s 140ms/step
[[0.34432802 0.00814287 0.38072217 0.00841277 0.18814225 0.07025192]]
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
1/1 [==============================] - ETA: 0s1/1 [==============================] - 0s 133ms/step
[[0.40781286 0.00282191 0.13897392 0.0089603  0.28684494 0.15458609]]
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
1/1 [==============================] - ETA: 0s1/1 [==============================] - 0s 132ms/step
[[2.0997408e-05 2.6008937e-01 1.5914723e-02 5.4484128e-04 7.5876765e-02
  6.4755332e-01]]
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
1/1 [==============================] - ETA: 0s1/1 [==============================] - 0s 144ms/step
[2.0997408e-05 2.6008937e-01 1.5914723e-02 5.4484128e-04 7.5876765e-02
 6.4755332e-01]
[[2.0997408e-05 2.6008937e-01 1.5914723e-02 5.4484128e-04 7.5876765e-02
  6.4755332e-01]]
>>> 
========================== RESTART: C:/Users/Admin/Desktop/respiratory disease prediction/result of model.py ==========================
Finished feature extraction from  21  files
1/1 [==============================] - ETA: 0s1/1 [==============================] - 0s 130ms/step
0.6475533
[[2.0997408e-05 2.6008937e-01 1.5914723e-02 5.4484128e-04 7.5876765e-02
  6.4755332e-01]]
>>> 
