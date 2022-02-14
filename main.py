import os
from boxsdk import BoxAPIException, Client, JWTAuth, OAuth2

print("hello heroku")
dbURI = os.environ.get("DATABASE_URL")
print(dbURI)
try:
    command = "pg_dump --exclude-table-data to_exclude -O -x -f latest_without_to_excluede.sql -v " + dbURI
    print(command)
    os.system(command)
    # os.system("pg_dump -T '\"Test2\"' " + dbURI + " > mydb2.sql")
    print("Backup completed")

    auth = OAuth2(
        client_id=os.environ.get("BOX_CLIENT_ID"),
        client_secret=os.environ.get("BOX_CLIENT_SECRET"),
        access_token= os.environ.get("DEVELOPER_TOKEN"),
        )
    
    client = Client(auth)
    me = client.user().get()
    print(f'My user ID is {me.id}')

    folder_id = '12345'
    file_name = 'latest_without_to_excluede.sql'
    stream = open('latest_without_to_excluede.sql', 'rb')

    new_file = client.folder(folder_id).upload_stream(stream, file_name)
    print(f'File "{new_file.name}" uploaded to Box with file ID {new_file.id}')

except Exception as e:
    print("!!Problem occured!!")
    print(e)
print("end")
