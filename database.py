import oracledb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DevServerAlpha
#DIALECT = 'oracle'
#SQL_DRIVER = 'oracledb'
#USERNAME = 'system'
#PASSWORD = 'test=123'
#HOST = 'es-286-6'
#PORT = 1521
#SERVICE_NAME = 'xepdb1'

#SA92DEV
DIALECT = 'oracle'
SQL_DRIVER = 'oracledb'
USERNAME = '1959649[sysadm]'
PASSWORD = '!Barbatos1'
HOST = 'horautlt805.fast.uh.edu'
PORT = 1521
SERVICE_NAME = 'sa92dev'

cp = oracledb.ConnectParams()
cp.parse_connect_string(f"{HOST}:{PORT}/{SERVICE_NAME}")
thick_mode = None

engine = create_engine(
    f'oracle+oracledb://{USERNAME}:{PASSWORD}@{cp.host}:{cp.port}/?service_name={cp.service_name}',
    thick_mode=thick_mode)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()