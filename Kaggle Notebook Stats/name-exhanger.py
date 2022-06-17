from IPython.display import Markdown, display
import datetime, requests, json, os, re, sys, time
import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


from_this="✅ 07 Cross Validation Methods ➡️ Tutorial 📊"
to_this="➡️ Tutorial ✅ 07 Cross Validation Methods 📊"



links=[]
for dirname, _, filenames in os.walk('./data/'):
    for filename in filenames:
        link=os.path.join(dirname, filename)
        links.append(link)
        

for link in links:
    temp_df=pd.read_csv(link)
    temp_df=temp_df.replace(to_replace=from_this, value=to_this)
    temp_df.to_csv(link,index=False)
    