import dropbox
import os
import json
from dropbox import FolderMetadata

dropbox_access_token = os.getenv('DROPBOX_ACCESS_TOKEN')



if __name__ == "__main__":

    if not dropbox_access_token:
        raise Exception("No Dropbox token present")

    dbx = dropbox.Dropbox(dropbox_access_token)

    print(f"User: {dbx.users_get_current_account()}")

    for file in dbx.files_list_folder('/Music').entries:
        print(f"File: {file}")

        if type(file) is FolderMetadata:
            print("File is a folder")