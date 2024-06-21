import psycopg2
class DATABASE:
  def connect(self):
      conn = psycopg2.connect( 
         database="ENVIRONMENT_DATABASE", user='postgres', password='pass', host='127.0.0.1', port='5432'
      )
      return conn
      