# tactic_summary

import sys
import csv
import pandas as pd
import numpy as np
import re

df = pd.read_csv(sys.argv[1]+'.csv')

df['Landing_Page'] = df.Landing_Page.replace(r"^(?:dt)\-?.*", "DT", regex=True) # Replace dt-xxxxxx with DT


count = df.pivot_table(index=['Sub_ID', 'Pub_ID', 'Landing_Page'], values='email', aggfunc='count', margins=True)

print(count)

count.to_csv('tactic.csv', index=True, columns=["email"]) # Save summary to CSV
