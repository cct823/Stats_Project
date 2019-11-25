
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math as m
import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
import numpy as np
import statsmodels.api as sm


#Global data for all functions
# import data for all functions
df = pd.read_csv('all_data.csv', header=0, index_col=0)
# filter the SAT submit rate > 0.6, and reset index for sorting
df_filter = df[df['Students Submitting SAT'] >= 0.6].reset_index()


applicants = [int(applications.replace(',','')) for applications in df_filter['Total_Applicants']]
# Get the average score for SAT score by (lower+upper)//2
avg_sat  = [(int(item.split('-')[0])+int(item.split('-')[1]))//2 for item in df_filter['SAT Range']]
avg_reading = [(int(item.split('-')[0])+int(item.split('-')[1]))//2 for item in df_filter['SAT Reading']]
avg_math = [(int(item.split('-')[0])+int(item.split('-')[1]))//2 for item in df_filter['SAT Math']]

# to dataframe
# table = pd.DataFrame({
#      'Applicants':applicants,
#      'SAT':avg_sat,
#      'Reading':avg_reading,
#      'math':avg_math}
#      )


def regression_SAT():
    x = np.array(avg_sat).reshape((-1, 1))
    y = np.array(applicants)
    model = LinearRegression().fit(x,y)
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)

    # print()


def regression_reading():
    x = np.array(avg_reading).reshape((-1, 1))
    y = np.array(applicants)
    model = LinearRegression().fit(x,y)
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)


def regression_math():
    x = np.array(avg_math).reshape((-1, 1))
    y = np.array(applicants)
    model = LinearRegression().fit(x,y)
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)


# grade_dict, count for the descriptive data for each columns
grade_dict = {}
# convert ranking to dummies number
df_ranking = df_filter.loc[:,'Academics':'Safety']  # select ranking columns
for i in list(df_ranking.columns):
    grade_dict[i] = {}
    for j in range(len(df_ranking[i])):
        try:
            grade_dict[i][df_ranking[i][j]] += 1
        except:
            grade_dict[i][df_ranking[i][j]] = 1

        if df_ranking[i][j].split()[0][0] == 'A':
            df_ranking[i][j] = 1
        else:
            df_ranking[i][j] = 0
print(df_ranking)
print(grade_dict)


