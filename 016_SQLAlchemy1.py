from sqlalchemy import *
from sqlalchemy.orm import *
__author__ = 'cui'

class Test(object):
    def __repr__(self):
            return '%s(%r, %r)' % (self.__class__.__name__, self.name, self.email)

if __name__ == "__main__":

    engine = create_engine('mysql://mcms_dba:mcms_dba@192.168.174.90/mcms', pool_recycle=60, connect_args={"charset": "utf8"}, echo=True)
    metadata = MetaData(engine)

    test_table = Table('test2', metadata,
        Column('id', Integer, primary_key=True),
        Column('text', Text),
        Column('email', String(120)))
    test_table.create()

    test_table = Table('test', metadata, autoload=True)
    i = test_table.insert()
    i.execute(name='rsj217', email='rsj21@gmail.com')
    i.execute({'name': 'ghost'},{'name': 'test'})

    mapper(Test, test_table)
    Session = sessionmaker(bind=engine) # 建立会话的方式 sqlalchemy 的版本不同 sessionmaker 的方式更好
    session = Session()
    query = session.query(Test)
    u = query.filter_by(name='new').first()
    print (u.name)

    Session = sessionmaker(bind=engine) # 建立会话的方式 sqlalchemy 的版本不同 sessionmaker 的方式更好
    session = Session()
    u = Test()
    u.name = 'avsd'
    session.add(u)
    session.flush()
    session.commit()