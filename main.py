import os
print("hello heroku")
dbURI = os.environ.get("DATABASE_URL")
print(dbURI)
try:
    os.system("pg_dump " + dbURI + " > mydb.sql")
    print("Backup completed")
except Exception as e:
    print("!!Problem occured!!")
    print(e)
print("end")
