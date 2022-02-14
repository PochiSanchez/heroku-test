import os
print("hello heroku")
dbURI = os.environ.get("DATABASE_URL")
print(dbURI)
try:
    command = "pg_dump --exclude-table-data to_exclude -O -x -f latest_without_to_excluede.sql -v " + dbURI
    print(command)
    os.system(command)
    # os.system("pg_dump -T '\"Test2\"' " + dbURI + " > mydb2.sql")
    print("Backup completed")
except Exception as e:
    print("!!Problem occured!!")
    print(e)
print("end")
