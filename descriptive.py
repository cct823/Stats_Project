# Name: Tim Chen
# Date: 11/10/2019

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



def intro():

    print('function in this code:\nrate_bar()\nsat_reading_low()\nsat_reading_high()\n'
          'sat_reading_avg()\nsat_math_low()\nsat_math_high()\nsat_math_avg()')


def rate_bar():
        # read accept rate data
    rate = df_filter['Accept_Rate']
    new_rate = {'0.1-0.2': 0, '0.2-0.3': 0, '0.3-0.4': 0, '0.4-0.5': 0, '0.5-0.6': 0, '0.6-0.7': 0,
                '0.7-0.8': 0, '0.8-0.9': 0, '0.9-1.0': 0}
    # change the data from string to float
    for i in range(len(rate)):
        percentage = int(rate[i].split('%')[0])/100
        # if percentage <= 0.1:
        #     new_rate['0.1-0.2'] += 1
        if 0.1 < percentage <= 0.2:
            new_rate['0.1-0.2'] += 1
        elif 0.2 < percentage <= 0.3:
            new_rate['0.2-0.3'] += 1
        elif 0.3 < percentage <= 0.4:
            new_rate['0.3-0.4'] += 1
        elif 0.4 < percentage <= 0.5:
            new_rate['0.4-0.5'] += 1
        elif 0.5 < percentage <= 0.6:
            new_rate['0.5-0.6'] += 1
        elif 0.6 < percentage <= 0.7:
            new_rate['0.6-0.7'] += 1
        elif 0.7 < percentage <= 0.8:
            new_rate['0.7-0.8'] += 1
        elif 0.8 < percentage <= 0.9:
            new_rate['0.8-0.9'] += 1
        elif 0.9 < percentage <= 1.0:
            new_rate['0.9-1.0'] += 1

    # get how many bins for chart
    # k = m.ceil(1+ 3.3*m.log(len(rate),10))
    # print chart
    plt.bar(new_rate.keys(),new_rate.values(),edgecolor='black', linewidth=1.2)
    plt.xticks(rotation=45)
    plt.title('Accept Rate Distribution For 157 Schools')
    plt.xlabel('Accept Rate')
    plt.ylabel('Counts')

    plt.show()
    return new_rate

def sat_reading_low():
    SAT = df_filter['SAT Reading']
    low = {}
    count_low = []


    for i in range(400,800,50):
        low[str(i)+'-'+str(i+50)] = 0
    low_key = list(low.keys())

    for x in SAT:
        lower = int(x.split('-')[0])
        count_low.append(lower)  # for calculating mean/sum/etc.
        # print(lower)
        for k in range(len(low_key)-1):
            if int(low_key[k].split('-')[0]) <= lower < int(low_key[k].split('-')[1]):
                low[low_key[k]] += 1
            else:
                continue

    plt.bar(low.keys(),low.values(),edgecolor='black', linewidth=1.2)
    plt.xticks(rotation=45)
    plt.title('SAT Reading Lower Bound For 157 Schools')
    plt.xlabel('SAT Range')
    plt.ylabel('Counts')
    plt.show()
    return low

def sat_reading_high():
    SAT = df_filter['SAT Reading']
    high = {}
    count_high = []


    for i in range(450,850,50):
        high[str(i)+'-'+str(i+50)] = 0
    high_key = list(high.keys())

    for x in SAT:
        higher = int(x.split('-')[1])
        count_high.append(higher)  # for calculating mean/sum/etc.
        # print(lower)
        for k in range(len(high_key)-1):
            if int(high_key[k].split('-')[0]) <= higher < int(high_key[k].split('-')[1]):
                high[high_key[k]] += 1
            else:
                continue

    plt.bar(high.keys(),high.values(),edgecolor='black', linewidth=1.2)
    plt.xticks(rotation=45)
    plt.title('SAT Reading Higher Bound For 157 Schools')
    plt.xlabel('SAT Range')
    plt.ylabel('Counts')
    plt.show()
    return high


def sat_reading_avg():
    SAT = df_filter['SAT Reading']
    avg = {}
    count_avg = []

    for i in range(490, 840, 45):
        avg[str(i)+'-'+str(i+45)] = 0
    avg_key = list(avg.keys())

    for q in SAT:
        lower = int(q.split('-')[0])
        higher = int(q.split('-')[1])
        avg_num = (lower+higher)//2
        count_avg.append(avg_num)
        for k in range(len(avg_key) - 1):
            if int(avg_key[k].split('-')[0]) <= avg_num < int(avg_key[k].split('-')[1]):
                avg[avg_key[k]] += 1
            else:
                continue
    # avg['770'] += 1
    plt.bar(avg.keys(),avg.values(),edgecolor='black', linewidth=1.2)
    plt.xticks(rotation=45)
    plt.title('SAT Reading Average For 157 Schools')
    plt.xlabel('SAT Range')
    plt.ylabel('Counts')
    plt.show()
    return avg


def sat_math_low():
    SAT = df_filter['SAT Math']
    low = {}
    count_low = []

    for i in range(400, 800, 50):
        low[str(i)+'-'+str(i+50)] = 0
    low_key = list(low.keys())

    for x in SAT:
        lower = int(x.split('-')[0])
        count_low.append(lower)  # for calculating mean/sum/etc.
        # print(lower)
        for k in range(len(low_key) - 1):
            if int(low_key[k].split('-')[0]) <= lower < int(low_key[k].split('-')[1]):
                low[low_key[k]] += 1
            else:
                continue

    plt.bar(low.keys(), low.values(), edgecolor='black', linewidth=1.2)
    plt.xticks(rotation=45)
    plt.title('SAT Math Lower Bound For 157 Schools')
    plt.xlabel('SAT Range')
    plt.ylabel('Counts')
    plt.show()
    return low


def sat_math_high():
    SAT = df_filter['SAT Math']
    high = {}
    count_high = []

    for i in range(450, 850, 50):
        high[str(i)+'-'+str(i+50)] = 0
    high_key = list(high.keys())

    for x in SAT:
        higher = int(x.split('-')[1])
        count_high.append(higher)  # for calculating mean/sum/etc.
        # print(lower)
        for k in range(len(high_key) - 1):
            if int(high_key[k].split('-')[0]) <= higher < int(high_key[k].split('-')[1]):
                high[high_key[k]] += 1
            else:
                continue

    plt.bar(high.keys(), high.values(), edgecolor='black', linewidth=1.2)
    plt.xticks(rotation=45)
    plt.title('SAT Math Higher Bound For 157 Schools')
    plt.xlabel('SAT Range')
    plt.ylabel('Counts')
    plt.show()
    return high


def sat_math_avg():
    SAT = df_filter['SAT Math']
    avg = {}
    count_avg = []

    for i in range(490, 840, 45):
        avg[str(i)+'-'+str(i+45)] = 0
    avg_key = list(avg.keys())

    for q in SAT:
        lower = int(q.split('-')[0])
        higher = int(q.split('-')[1])
        avg_num = (lower + higher) // 2
        count_avg.append(avg_num)
        for k in range(len(avg_key) - 1):
            if int(avg_key[k].split('-')[0]) <= avg_num < int(avg_key[k].split('-')[1]):
                avg[avg_key[k]] += 1
            else:
                continue
    # avg['770'] += 1
    plt.bar(avg.keys(), avg.values(), edgecolor='black', linewidth=1.2)
    plt.xticks(rotation=45)
    plt.title('SAT Math Average For 157 Schools')
    plt.xlabel('SAT Range')
    plt.ylabel('Counts')
    # plt.figure(figsize = [30,30])
    plt.show()
    # figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

    return avg


# def scatter_math_rate():


