import os
print("hello heroku")
dbURI = os.environ.get("DATABASE_URL")
print(dbURI)
try:
    command = "pg_dump -T \"public.\"Test2\"\" " + dbURI + " > mydb2.sql"
    print(command)
    os.system("pg_dump -T \"public.\"Test2\"\" " + dbURI + " > mydb2.sql")
    print("Backup completed")
except Exception as e:
    print("!!Problem occured!!")
    print(e)
print("end")
