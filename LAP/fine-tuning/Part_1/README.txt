To replicate results of this experiment:

1. run change_chalearn_directory.py to change the address of images within dataset .txt file to match the address of the images stored at your computer (through new_directory parameter)

2. prepare the data and script for each trial of experiment through executing prepare_files.py that:
 1. first creates multiple datasets for each fine-tuning portion
 2. creates a network description file for each dataset by creating modified version of age_train.prototxt
 3. creates a solver for each network description

3. run run_experiment.sh that trains the network using the solver and starting weight defined in the shell script

4. calculate the MAE score of each trained network on Chalearn validation set and add this value to a csv by running learning_curve.py

5. get the statistics of each dataset size by running learning_curve_statistics.py

Note: The different Learning_curve_prototxts_ files enable parallel instances of the experiment to be run at the same time
