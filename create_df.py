import pandas as pd

def create_df(input_array):
    
    IDs = list(range(len(input_array)))
    train_prep_eegs_inputs_df = pd.DataFrame(index=IDs,
                       columns=["dim_{}".format(ch) for ch in range(input_array.shape[1])])
    for sample_idx in range(input_array.shape[0]):
        for ch_idx in range(input_array.shape[1]):
            train_prep_eegs_inputs_df.at[train_prep_eegs_inputs_df.index[sample_idx], train_prep_eegs_inputs_df.columns[ch_idx]] = \
                pd.Series(input_array[sample_idx, ch_idx])
    return train_prep_eegs_inputs_df