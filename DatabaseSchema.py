import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, create_engine, ForeignKey, Text, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class GCPServers(Base):
    __tablename__ = 'gcp_servers'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    timestamp = Column('timestamp', DateTime, default=datetime.datetime.utcnow)
    name = Column('name', String(63))
    project_id = Column('project_id', String(30))
    ip = Column('ip', String(15))


class OktaAsaServers(Base):
    __tablename__ = 'okta_servers'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    timestamp = Column('timestamp', DateTime, default=datetime.datetime.utcnow)
    name = Column('name', String(63))
    project_id = Column('project_id', String(30))
    ip = Column('ip', String(15))
    okta_id = Column('name', String(90))


class MissingOktaServers(Base):
    __tablename__ = "missing_okta_servers"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    timestamp = Column('timestamp', DateTime, default=datetime.datetime.utcnow)
    gcp_server_id = Column('gcp_server_id', Integer, ForeignKey('gcp_servers.id'))
    return_code = Column('return_code', Integer)
    return_msg = Column('return_code', Text)


class RequestVolley(Base):
    __tablename__ = "request_volley"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    start_timestamp = Column('start_timestamp', DateTime)
    end_timestamp = Column('end_timestamp', DateTime, default=datetime.datetime.utcnow)
    gcp_server_id = Column('gcp_server_id', Integer, ForeignKey('gcp_servers.id'))
    okta_servers_id = Column('okta_servers_id', Integer, ForeignKey('okta_servers.id'))
    succeeded = Column('succeeded', Boolean)
    attempts = Column('attempts', Integer)
    command = Column('command', String(90))


class Request(Base):
    __tablename__ = "request"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    start_timestamp = Column('start_timestamp', DateTime)
    end_timestamp = Column('end_timestamp', DateTime, default=datetime.datetime.utcnow)
    request_volley_id = Column('request_volley_id', Integer, ForeignKey('request_volley.id'))
    return_code = Column('return_code', Integer)
    return_msg = Column('return_code', Text)


engine = create_engine("mysql+pymysql://root:rootpassword@localhost/storage", echo=True)
Base.metadata.create_all(engine)
