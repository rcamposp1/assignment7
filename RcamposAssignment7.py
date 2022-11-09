# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:07:42 2022

@author: ronal
"""
import pandas as pd
# Load .csv file from remote
def get_csv(web_link):
    df = pd.read_csv(web_link)
    return df

# Call the function
data = get_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")

import matplotlib.pyplot as plt

# Bar Plot
plt.figure()
plt.figure(figsize=(10,7))
plt.title('Region Wise Count of Countries', fontsize=20, fontweight='bold')
plt.xlabel('Region', fontsize=15)
plt.ylabel('Count', fontsize=15)
region_wise_count = data.groupby(['Region']).size()
plt.bar(region_wise_count.index,region_wise_count.values)