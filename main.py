import os
from boxsdk import BoxAPIException, Client, JWTAuth

print("hello heroku")
dbURI = os.environ.get("DATABASE_URL")
print(dbURI)
try:
    command = "pg_dump --exclude-table-data to_exclude -O -x -f latest_without_to_excluede.sql -v " + dbURI
    print(command)
    os.system(command)
    # os.system("pg_dump -T '\"Test2\"' " + dbURI + " > mydb2.sql")
    print("Backup completed")

    auth = JWTAuth(
            client_id= os.environ.get("BOX_CLIENT_ID"),
            client_secret=os.environ.get("BOX_CLIENT_SECRET")
        )
    auth.authenticate_instance()
    client = Client(auth)
    folder_id = '12345'
    file_name = 'latest_without_to_excluede.sql'
    stream = open('file.pdf', 'rb')

    new_file = client.folder(folder_id).upload_stream(stream, file_name)
    print(f'File "{new_file.name}" uploaded to Box with file ID {new_file.id}')

except Exception as e:
    print("!!Problem occured!!")
    print(e)
print("end")
