import pandas as pd
import os.path

df = pd.read_csv('data//Base-INFLUD-14-09-2020.csv', sep=";")
sample = df.sample(n=1000)

if not os.path.isfile("data//sample.csv"):
    sample.to_csv('data//sample.csv')