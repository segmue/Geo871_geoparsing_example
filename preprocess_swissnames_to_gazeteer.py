import pandas as pd
swissnames = pd.read_csv('data/swissNAMES3D_PKT.csv', sep=';', usecols=['OBJEKTART', 'NAME'])

# Filter out only the relevant columns OBJEKTART and NAME

## Make one dictionary with Name as key and OBJEKTART as value
swissnames_dict = dict(zip(swissnames['NAME'], swissnames['OBJEKTART']))