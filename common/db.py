import sqlalchemy

def open_conn(schema='webapp'):
    global engine
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:pretzel123@localhost/{0}'.format(schema), pool_recycle=3600, connect_args={'options': '-csearch_path=intmed,datapit'})

open_conn()

def exec_sql(cmd=None,schema=None):
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:pretzel123@localhost/{0}'.format(schema), pool_recycle=3600, connect_args={'options': '-csearch_path=intmed,datapit'})
    engine.execute('{0}'.format(cmd))