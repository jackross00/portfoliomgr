import pandas as pd
from Portfoliomgr.common import db
import matplotlib.pyplot as plt

df = pd.read_sql_query('select * from "load_index_perf"',con=db.engine)
df = df.drop(columns=['level_0','index'])
pivoted = df.pivot(index='mrkt_dt',columns='benchmark',values='mkt_val')
pivoted.plot()
plt.show()