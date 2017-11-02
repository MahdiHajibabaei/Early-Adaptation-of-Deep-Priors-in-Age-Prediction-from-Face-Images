In this section of experiments we:
1. first create training and validation datasets for different sizes of fine-tuning dataset (prepare_files.py)
2. divide the computation to three equal parts to be run on 3 GPUs and scheduleit on cluster (run_experiment.sh)
3. evaluate the models in the same script using the MAE Python script on that same 3 GPUs (learning_curve.py)
4. evaluate the mean and variance of prediction error for each dataset size (learning_curve_statistics.py)
