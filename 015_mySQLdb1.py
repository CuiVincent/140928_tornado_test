import MySQLdb

__author__ = 'cui'

if __name__ == "__main__":

    con=MySQLdb.connect(user='mcms_dba',passwd='mcms_dba',host='192.168.174.90',db='mcms', charset="utf8")
    cur=con.cursor()
    cur.execute('''INSERT INTO mcms.SYS_USER(
   ID
  ,CODE
  ,NAME
  ,CUSERID
  ,CDATE
  ,EUSERID
  ,EDATE
  ,PASSWORD
  ,ISVALID
) VALUES (
   NULL -- ID - IN int(20)
  ,'lisi'  -- CODE - IN varchar(100)
  ,'李四'  -- NAME - IN varchar(100)
  ,0   -- CUSERID - IN int(20)
  ,NULL  -- CDATE - IN datetime
  ,0   -- EUSERID - IN int(20)
  ,NULL  -- EDATE - IN date
  ,'123'  -- PASSWORD - IN varchar(100)
  ,'0'  -- ISVALID - IN varchar(1)
)''')
    for data in cur.fetchall():
        print(data)
    cur.execute('select CODE,NAME from SYS_USER')
    for CODE,NAME in cur.fetchall():
        print(CODE+'-'+NAME)
    cur.execute('select * from SYS_USER')
    for data in cur.fetchall():
        print(data[1])
    cur.close()
    con.commit()
    con.close()