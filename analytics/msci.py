import pandas as pd
from Portfoliomgr.common import db
import matplotlib.pyplot as plt

df = pd.read_sql_query('select * from "load_index_perf"',con=db.engine)
df = df.drop(columns=['index'])

bchmks = df.benchmark.drop_duplicates().tolist()
bchmk_num = len(bchmks)

for bchmk in bchmks:
    bchmk_df = df[df.benchmark == bchmk]
    bchmk_df['rtn_1day_temp'] = ( bchmk_df.mkt_val - bchmk_df.mkt_val.shift(1) ) / bchmk_df.mkt_val.shift(1)
    df = df.merge(bchmk_df, on=['mrkt_dt','benchmark','mkt_val'], how='left')

df['rtn_1day'] = df[df.columns[3:]].bfill(axis=1).iloc[:, 0]
df = df.loc[:,['mrkt_dt','benchmark','mkt_val','rtn_1day']]

for bchmk in bchmks:
    mtd_df = df[df.benchmark == bchmk]
    mtd_df['rtn_temp'] = mtd_df.rtn_1day.cumsum()
    df = df.merge(mtd_df, on=['mrkt_dt','benchmark','mkt_val','rtn_1day'], how='left')

df['rtn_tot'] = df[df.columns[4:]].bfill(axis=1).iloc[:, 0]
df = df.loc[:,['mrkt_dt','benchmark','rtn_tot']]

pivoted = df.pivot(index='mrkt_dt',columns='benchmark',values='rtn_tot')
pivoted.plot()
plt.show()


# df.to_sql('temp_rtn', db.engine)