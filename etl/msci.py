import pandas as pd
from Portfoliomgr.common import db
import sys, os, sqlalchemy, psycopg2

index_xl = Path(__file__).parent / '../data/historyIndex.xls'
df = pd.read_excel(index_xl,sheet_name='History Index',header=6)

### Subset rows where no indices have data ###
df = df[df[df.columns[1:]].notnull().all(axis=1)]

### Convert to correct datatypes ###
df['Date'] = df['Date'].astype('datetime64[ns]')
df[df.columns[1:]] = df[df.columns[1:]].replace('[\$,]', '', regex=True).astype('float64')
df = df.melt(id_vars='Date',var_name='benchmark')
df = df.rename(columns={"Date": "mrkt_dt", "value": "mkt_val"}, errors="raise")

db.exec_sql(schema='webapp',cmd='DROP TABLE IF EXISTS load_index_perf')
df.to_sql('load_index_perf', db.engine)
