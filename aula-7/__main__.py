import pandas as pd

lido = pd.read_csv('aula-7/daily_engagement_full.csv')


print len(lido['acct'].unique())
