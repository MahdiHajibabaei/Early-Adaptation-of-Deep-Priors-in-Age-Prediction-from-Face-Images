The code and data regarding to the paper: 
M. Hajibabaei, A. Volokitin, R. Timofte. Early Adaptation of Deep Priors in Age Prediction from Face Images. In IEEE International Conference on Computer Vision Workshop (ICCVW 2017), October 2017, Italy.

The expeiments are done for two dataset and the code and result regrading to each dataset is put in a folder with the name of the target dataset. However, the pre-trainings of network with resampled IMDB dataset with original distribution of IMDB and uniform age distribution is done only once and code and result is in LAP folder.
In this project, fine-tunings were executed in two phases: the trials with more samples from target dataset and the trials with fewer samples from target dataset; mainly because the trials with more samples from target dataset did not show any performance difference between different pre-trainings thus we added the phase two trails to see when performances converge.

In some shell script there is reference to files in the directory "glusterfs", please change this to the directory of the corresponding files in your own computer.
