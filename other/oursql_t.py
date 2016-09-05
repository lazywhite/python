import oursql
from pprint import pprint

def main():
    db_name='examPython'
    conn=oursql.connect('127.0.0.1','root','1234',db=db_name)

    cur=conn.cursor()
    cur.execute('insert into a(user,level,errormsg,msgtime) values(?,?,?,?)',('bob',5,'hehe',20131122))
    conn.commit()
    cur.execute('select * from a')

    result=cur.fetchall()

    pprint result

    cur.close()
    conn.close()

if __name__=='__main__':
    main()
