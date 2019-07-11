import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")                   #data frame



#each column here is a feature.
#all features and labels may be related to each other but we use only meaningfull feature.

df = df [['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df [['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print (df.head())



# features are attributes that make out the label
#label is a prediction into the future.
# so we have got data by now lets start making real prediction over this.
