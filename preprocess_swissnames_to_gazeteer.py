import io
import zipfile

import pandas as pd
import requests
swissnames = pd.read_csv('data/swissNAMES3D_PKT.csv', sep=';', usecols=['OBJEKTART','OBJEKTKLASSE_TLM', 'NAME','E','N'])


# Download Zip from link and unzip it in memory: https://data.geo.admin.ch/ch.swisstopo.swissnames3d/swissnames3d_2022/swissnames3d_2022_2056.csv.zip
url = 'https://data.geo.admin.ch/ch.swisstopo.swissnames3d/swissnames3d_2022/swissnames3d_2022_2056.csv.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
res = pd.DataFrame()
for name in z.namelist():
    if name.endswith('.csv'):
        df = pd.read_csv(z.open(name), sep=';',usecols=['OBJEKTART','OBJEKTKLASSE_TLM', 'NAME','E','N'])
        res = pd.concat([res, df])

# REMOVE DUPLICATES
res = res.drop_duplicates()


## Make a index dictionary. Key is "Name" and Value is Number of Occurences
swissnames_dict = dict((res['NAME']).str.lower().value_counts())

## Save the dictionary to a csv
swissnames_dict = pd.DataFrame.from_dict(swissnames_dict, orient='index').reset_index()
swissnames_dict.columns = ['Name', 'Count']
swissnames_dict.to_csv('swissnames_dict.csv', index=False)