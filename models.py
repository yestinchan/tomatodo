#-*- coding : utf-8 -*-
import MySQLdb
from  config import settings
from datetime import datetime

class DBHelper(object):
    def __init__(self):
        pass

    def conn(self):
        self.connection = MySQLdb.connect(host=settings['db_host'], \
            port=settings['db_port'],user=settings['db_user'], \
            passwd=settings['db_password'],db=settings['db_db'],\
            charset=settings['db_charset'])
        return self.connection

#    def close(self):
#        return self.connection.close()


class TODOItem(object):
    
    table = 'todos'

    def __init__(self,id=None,content=None,user_id=None,created=None,finished=None):
        if not content:
            raise RuntimeError("must be some content")
        if not created:
            created = datetime.now()
        self.id = id
        self.content = content
        self.created = created
        self.user_id = user_id
        self.finished = finished
        #connection
        self.dbhelper = DBHelper()

    def list(self,fromid=None,limit=None):
        conn = self.dbhelper.conn()
        cursor = conn.cursor()
        nums = cursor.execute("select * from {0}".format(self.table))
        for row in cursor.fetchall():
            print row
        cursor.close()
        conn.close()

    def save(self,todo=None):
        if todo :
            #store this
            it = todo
        else:
            it = self
        #store logic
        conn = self.dbhelper.conn()
        cursor = conn.cursor()
        sql = "insert into {0} values (null,'{1}',{2},'{3}',null)"\
            .format(self.table,it.content,it.user_id,it.created.strftime("%y-%m-%d %H:%M:%S"))
        print sql
        nums = cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return nums > 0

    def delete(self,id=None):
        if id:
            #delete this
            it = id
        else:
            it = self
        #delete
        conn = self.dbhelper.conn()
        cursor = conn.cursor()
        sql = "delete from {0} where id = {1}".format(self.table,it.id)
        print sql
        nums = cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return nums > 0

class TODOToday(object):
    table = "todaylist"
    maintable = "todos"

    def list(self):
        '''
        List today todos
        '''
        conn = self.dbhelper.conn()
        cursor = conn.cursor()
        sql = "select * from {0},{1} \
            where {0}.id = {1}.todo_id and to_days({1}\
            .added)=to_days(now())".format(self.maintable,self.table)
        nums = cursor.execute(sql)
        result =  cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def add(self,row):
        

    def set(self,row,item,value):
        conn = self.dbhelper.conn()
        cursor = conn.cursor()
        sql = "update {0} set {1} = {2} \
            where {0}.id = {3}".format(self.table,item,value,row)
        nums = cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return nums > 0

class TODOHistory(object):
    table = "dohistory"
    maintable = "todos"

    def list(self):
        '''
        History overview
        '''
        pass

    def start(self):
        pass

    def finish(self):
        pass

    def addInterrupt(self):
        pass


if __name__ == "__main__":
    item = TODOItem(id=2,content="First todo",user_id=1)
    #item.save()
    item.list()
    item.delete()
    item.list()
