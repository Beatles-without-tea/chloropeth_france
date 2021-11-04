
import json
import pandas as pd
from geoviews import dim
import geopandas as gpd
import geoviews as gv
import geoviews.feature as gf
import numpy as np
import holoviews as hv

sf = gpd.read_file('https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson')
sf.iloc[0:9,0]=range(1,10)
sf['code']=sf['code'].astype('string')

df=pd.read_csv('dfinal.csv',encoding='ISO-8859-1')
csv=df.groupby('dep')['voix'].mean()
csv=pd.DataFrame(csv)
csv.reset_index(level=0,inplace=True)
csv['code']=csv['dep'].astype('string')

jf = sf.merge(csv,left_on='code', right_on='code')
regions = gv.Polygons(jf, vdims=['nom', 'voix'])
regions.opts(width=600, height=600, toolbar='above', color=dim('voix'), 
             colorbar=True, tools=['hover'], aspect='equal')

hv.save(regions,'regions.png',fmt='png')