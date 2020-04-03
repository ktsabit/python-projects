from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)


    # Call the Drive v3 API
    # results = service.files().list(
    #     pageSize=10, fields="nextPageToken, files(id, name)").execute()
    # items = results.get('files', [])

    # if not items:
    #     print('No files found.')
    # else:
    #     print('Files:')
    #     for item in items:
    #         print(u'{0} ({1})'.format(item['name'], item['id']))

    file_name = str(sys.argv[1])

    aa = file_name.split(".")
    file_extension = aa[1]
    print(f"Filetype: {file_extension}")

    if (file_extension == "rar"):
        mimetype = 'application/x-rar-compressed'
    elif (file_extension == "zip"):
        mimetype = 'application/zip'
    elif (file_extension == "bz"):
        mimetype = 'application/x-bzip'
    elif (file_extension == "bz2"):
        mimetype = 'application/x-bzip2'
    elif (file_extension == "pdf"):
        mimetype = 'application/pdf'
    elif (file_extension == "txt"):
        mimetype = 'txt/plain'
    elif (file_extension == "7z"):
        mimetype = 'application/x-7z-compressed'
    elif (file_extension == "png"):
        mimetype = 'image/png'
    elif (file_extension == "gz"):
        mimetype = 'application/gzip'
    elif (file_extension == "json"):
        mimetype = 'application/json'
    
    try:
        file_metadata = {'name': f'{file_name}'}
        media = MediaFileUpload(file_name, mimetype=mimetype)
        upload = service.files().create(media_body=media, body=file_metadata, fields='id').execute()

        print(f"Uploaded {file_name}")
        print(f"File id: {upload.get('id')}")

    except:
        print("invalid arguments")


if __name__ == '__main__':
    main()
# [END drive_quickstart]
