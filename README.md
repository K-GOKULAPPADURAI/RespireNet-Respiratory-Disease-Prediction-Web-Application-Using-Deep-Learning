# Respiratory-Disease-Prediction-using-Deep-Learning
# To run the Flask local web application goto this repository 

``` https://github.com/K-GOKULAPPADURAI/Render-Deployment-of-Respiratory-Disease-Prediction-using-Deep-leanring-model ```

ABSTRACT :

  Prediction of respiratory diseases such as
COPD(Chronic obstructive pulmonary disease), URTI(upper
respiratory tract infection), Bronchiectasis, Pneumonia,
Bronchiolitis with the help of deep neural networks or deep
learning. We have constructed a deep neural network model
that takes in respiratory sound as input and classifies the
condition of its respiratory system. It not only classifies among
the above-mentioned disease but also classifies if a person’s
respiratory system is healthy or not with higher accuracy and
precision.

Index Terms:
  
  Respiratory disease recognition, Deep neural
network,GRU(Gated Recurrent Unit), sound data, data augmentation, feature extraction, classification

# To run the project very quick and agile follow the instructions bellow:

-> First download the git repo as a zip and extract it are else git clone to your environment.

-> Then get the dataset which's link is provided inside the Link_TO_Dataset.txt in the give repository and extract the downloaded 
dataset folder 'archive' to the main repository of our porject files present

About the Dataset:

These recordings were taken from 126 patients. It includes 920 annotated recordings
of varying length from 10s to 90s.There are a total of 5.5 hours
of recordings containing 6898 respiratory cycles - 886 contain
wheezes, 1864 contain crackles and 506 contain both crackles
and wheezes. The patients span all age groups - children,
adults and the elderly. The respiratory sounds in the dataset are of different category such as Healthy, COPD(Chronic
obstructive pulmonary disease), URTI(upper respiratory tract
infection), Bronchiectasis, Pneumonia, Bronchiolitis, Asthma,
LRTI(Lower respiratory tract infection) which would be classified or predicted by out neural network model.

-> To the accuracy of our model and data balancing we have droped the LRTI and ASTHMA from our dataseta and trained because of its very low 
level of number count in the dataset collection.

-> Iam using Python version 3.7.5 which is very flexible and capatible with all pip packages for me compared to other
bug fitted new versionsss....!

-> So version is your choice and then run the command, to install all the requirements and the supporting libraries for our project.
	# pip install -r requirements.txt

-> After installing all these packages successfully just run the respiratory-disease.py for training the dataset and deploying a new model

	python respiratory-disease.py

-> If you dont want to train again means, i have attached my locally trained deep learning model in the repo using that you can direct predict
disease easily without any overhelming tasks or cpu hanging....!!!
	
	python "result of model.py"

-> To get the result of first audio from the dataset of the patients run the file results of model.py, it will give you a predicted disease with
probobility of other disease witht there percentages also.

-> To run in GUI format and to check a new audio file means, i have created a Simple GUI for getting the input as path of the audio file with the 
extension and return the results in the desktop manner using the kivy frame work in python.
	
	python main.py

-> To run GUI mode just run the main.py inside the main repo of our project and give the input below:

	#archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pr_sc_Litt3200.wav

	nor like below formats 
	
	archive//Respiratory_Sound_Database//Respiratory_Sound_Database//audio_and_txt_files//104_1b1_Pr_sc_Litt3200.wav
						or
	archive\Respiratory_Sound_Database\Respiratory_Sound_Database\audio_and_txt_files\104_1b1_Pr_sc_Litt3200.wav

-> After giving input in click the Test button and you can view the predicted disease immediately in the GUI in the desktop easily.


INTRODUCTION: 

  In this research paper, we are going to discuss how deep
learning could be used in the recognition of respiratory disease
just from the respiratory sound. Respiratory audios are important indicators of respiratory health and respiratory disorder.
For example, a wheezing sound is a common sign that a patient
has an obstructive airway disease like asthma or chronic
obstructive pulmonary disease (COPD). We have approached
the problem with different neural network model architecture,
and choose the model with would give us the best possible
results, we also performed data augmentation over the data-set.
The data-set we have used consists of respiratory sounds taken
from different patients from different locations around the
chest. We have used Accuracy score, Precision score, Recall
score, f1-score, Cohen’s kappa score, Matthews correlation
coefficient as metrics to evaluate and compare the performance
of different models against the same data-set. With this model
we have achieved an accuracy of 95.67 % ± 0.77 %,precision
of 95.89 % ± 0.8 %,Sensitivity of 95.65 % ± 0.753 %,f1-score
of 95.66 %±0.79 %, Cohen’s kappa score of 94.74 %±0.96 %
and Matthews correlation coefficient of 94.79 % ± 0.96 %.

-> All the deep learning model structure and the architecture are attached a pic inside the screenshots folder 

-> And The metrics that we have used to evaluate the performance
of the model are Accuracy, Precision, Recall/sensitivity,
F1-score, Cohens kappa score(CK), Matthews correlation
coefficient(MCC). For all the above metrics if the score is 1,
then the model is performing in the best way possible and
predicting every class perfectly. Lower the score more is the
model facing difficulty while predicting the correct class and
also indicates poor model performance.


CONCLUSION

    Medical research and medical science could be progressed
further with the help of artificial intelligence. The neural network architecture has performed better than our expectations.
But still, it needs a lot of improvements to achieve higher
accuracy during prediction. We hope our research would
inspire future researchers to work on this subject and wish
they would approach with a better and encouraging solution.

In case of any doubts are struggles contact me and feel free to ping me you stranger.....!
phone: 9025421765
gmail: k.gokulappaduraikjgv@gmail.com

