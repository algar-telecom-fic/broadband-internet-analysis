import abc
import datetime
import sys
sys.path.append('/home/gardusi/github/broadband_internet_analysis/')
import mysql_gardusi

class XDSL(abc.ABC):
  database_name = 'kappacidade',
  date = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
  host = '0.0.0.0',
  passwd = 'pe',
  primary_key = 'id',
  user = 'peduardo',

  @abc.abstractmethod
  def add_port(self):
    pass

  @abc.abstractmethod
  def build_documents(self):
    pass

  def insert_documents(self):
    db = mysql_gardusi.mySQL(
      database = self.database_name,
      host = self.host,
      passwd = self.passwd,
      user = self.user,
    )
    db.create_table(
      primary_key = self.primary_key,
      table_info = self.table_info,
      table_name = self.table_name,
    )
    db.insert_into(
      self.table_name,
      self.table_info,
      self.documents,
    )