import os
print("hello heroku")
dbURI = os.environ.get("DATABASE_URL")
print(dbURI)
print("end")
