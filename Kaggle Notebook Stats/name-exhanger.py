from IPython.display import Markdown, display
import datetime, requests, json, os, re, sys, time
import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


from_this="➡️ Intro to Bias-Variance Tradeoff 📋 with Numpy"
to_this="➡️ Bias-Variance Tradeoff 📋 Theory & Code Ex."



links=[]
for dirname, _, filenames in os.walk('./data/'):
    for filename in filenames:
        link=os.path.join(dirname, filename)
        links.append(link)
        

for link in links:
    temp_df=pd.read_csv(link)
    print("Changing in ",link[25:35])
    temp_df=temp_df.replace(to_replace=from_this, value=to_this)
    temp_df.to_csv(link,index=False)

print("\n++++++++++++++++++++++++++++++\n            Done\n++++++++++++++++++++++++++++++\n")