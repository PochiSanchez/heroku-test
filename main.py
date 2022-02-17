import os
from boxsdk import Client, JWTAuth, OAuth2
from datetime import datetime

print("hello heroku")
dbURI = os.environ.get("DATABASE_URL")
print(dbURI)
try:
    filename = 'latest_without_to_excluede_' + (datetime.now().isoformat()) + ".dump"
    print('filename: ' + filename)
    command = "pg_dump --exclude-table-data to_exclude -O -x -Fc -f " + filename + " -v " + dbURI
    print(command)
    os.system(command)
    # os.system("pg_dump -T '\"Test2\"' " + dbURI + " > mydb2.sql")
    print("Backup completed")
    20000000
    auth = OAuth2(
        client_id=os.environ.get("BOX_CLIENT_ID"),
        client_secret=os.environ.get("BOX_CLIENT_SECRET"),
        access_token= os.environ.get("DEVELOPER_TOKEN"),
        )
    
    client = Client(auth)
    me = client.user().get()
    print(f'My user ID is {me.id}')

    folder_id = '156414997477'

    with open(filename, 'rb') as stream:
        total_size = os.stat(filename).st_size
        if(total_size < 20000000): #chunked upload api has a minimun size allowed
            uploaded_file = client.folder(folder_id).upload_stream(stream, filename)
        else:
            upload_session = client.folder(folder_id).create_upload_session(total_size, filename)
            chunked_uploader = upload_session.get_chunked_uploader_for_stream(stream, total_size)

            try:
                uploaded_file = chunked_uploader.start()
            except: 
                uploaded_file = chunked_uploader.resume()
        print(f'File "{uploaded_file.name}" uploaded to Box with file ID {uploaded_file.id}')
    print("removing local copy")
    os.remove(filename)

except Exception as e:
    print("!!Problem occured!!")
    print(e)
print("end")
