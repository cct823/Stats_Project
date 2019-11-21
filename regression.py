
import pandas as pd
import math as m
import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
import numpy as np

#Global data for all functions
# import data for all functions
df = pd.read_csv('all_data.csv', header=0, index_col=0)
# filter the SAT submit rate > 0.6, and reset index for sorting
df_filter = df[df['Students Submitting SAT'] >= 0.6].reset_index()

# convert ranking to dummies number
df_ranking = df_filter.loc[:,'Academics':'Safety']  # select ranking columns
for i in list(df_ranking.columns):
    for j in range(len(df_ranking[i])):
        if df_ranking[i][j].split()[0][0] == 'A':
            df_ranking[i][j] = 1
        else:
            df_ranking[i][j] = 0
print(df_ranking)


