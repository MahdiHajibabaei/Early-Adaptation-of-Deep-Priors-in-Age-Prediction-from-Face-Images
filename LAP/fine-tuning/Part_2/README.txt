In this section of experiments we:
1. first create multiple datasets for each fine-tuning portion
2. create a network description file for each dataset
3. create a solver for each network description
4. train the network using the solver and weight defined in the shell script
5. calculate the network MAE on both 20% Chalearn train set and Chalearn validation set and add this value to a csv
6. delete the model files (Caffemodel & Solverstate)

The CNN deployed uses the softmax with loss for training, validation and testing. 
