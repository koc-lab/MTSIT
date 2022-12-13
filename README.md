# MTSIT
This is the GitHub repository for the [paper](https://ieeexplore.ieee.org/document/9964035): A. Y. Yıldız, E. Koç, A. Koç, **“Multivariate Time Series Imputation with Transformers”**, IEEE Signal Processing Letters, 2022. This paper is based on [Multivariate Time Series Transformer Framework](https://github.com/gzerveas/mvts_transformer) and extended on imputation tasks.

## Datasets

[Physionet Healthcare Dataset](https://physionet.org/content/challenge-2012/1.0.0/) and [Beijing Air Quality Dataset](https://www.microsoft.com/en-us/research/publication/forecasting-fine-grained-air-quality-based-on-big-data/) are used for imputation task.

For any dataset, including Healthcare and Air Quality, `Pandas Time Series Data (ptsd)` format is used. We preprocess the datasets following [BRITS](https://github.com/caow13/BRITS). The input shapes are (number of samples &#215; features &#215; time points). `.pickle` files for training inputs - labels, and test inputs - labels are stored in a folder. `--data_dir` option parameter holds the directory of this folder.

## Requirements

Codes are implemented on Linux based systems, e.g. Ubuntu. Packages that are used with versions are included in `requirements.txt`. Additionally, for conda users, `venv.yml` file is also included.

## Experiments

Models are trained and saved in `experiments` folder. You are expected to create this folder beforehand, by `mkdir experiments`. Models can be tested by using the best model checkpoint for any model saved in `experiments`. Additionally, for any task implemented, e.g. imputation for our case, results are recorded in the file determined by `--records_file` with the row name `--name`. Corresponding sample terminal option parameters are shown below.

**Training**

For Air Quality experiment:

```
python src/main.py --output_dir experiments --name imputation_air_quality --records_file imputation_air_quality.xls --data_dir air_quality_data/ --data_class ptsd --pattern train --val_ratio 0.2 --epochs 400 --lr 0.001 --optimizer RAdam --pos_encoding learnable --task imputation
```

For Healthcare experiment:

```
python src/main.py --output_dir experiments --name imputation_healthcare --records_file imputation_healthcare.xls --data_dir healthcare_data/ --data_class ptsd --pattern train --val_ratio 0.2 --epochs 400 --lr 0.001 --optimizer RAdam --pos_encoding learnable --task imputation
```

**Test**

In `--load_model`, `$experiment_name` is the trained model folder to be tested. `--masking_ratio` and `--mask_distribution` parameters are specific for the test requirements, and may not be used if not wanted. Default values for these parameters are shown in `options.py`.

For Air Quality experiment:

```
python src/main.py --output_dir experiments --name imputation_air_quality --records_file imputation_air_quality.xls --data_dir air_quality_data/ --data_class ptsd --pattern train --val_ratio 0.2 --epochs 400 --lr 0.001 --optimizer RAdam --pos_encoding learnable --task imputation --test_only testset --test_pattern test --load_model experiments/$experiment_name/checkpoints/model_best.pth
```

For Healthcare experiment:

```
python src/main.py --output_dir experiments --name imputation_healthcare --records_file imputation_healthcare.xls --data_dir healthcare_data/ --data_class ptsd --pattern train --val_ratio 0.2 --epochs 400 --lr 0.001 --optimizer RAdam --pos_encoding learnable --task imputation --test_only testset --test_pattern test --load_model experiments/$experiment_name/checkpoints/model_best.pth --masking_ratio 0.1 --mask_distribution bernoulli
```

After testing; three `numpy array` files are saved under the folder `visualize_data`, which are `target`, `target_mask` and `predictions` whose shape are also (number of samples &#215; features &#215; time points). These files correspond to the **ground-truth values**, the **masked indexes**, and the **imputed values** of the test data respectively. These can be used to visualize the time points of the testing data by selecting any sample index and any feature index.
