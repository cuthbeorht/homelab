import dropbox
import os
import json
from dropbox.files import FolderMetadata, FileMetadata

dropbox_access_token = os.getenv('DROPBOX_ACCESS_TOKEN')



if __name__ == "__main__":

    if not dropbox_access_token:
        raise Exception("No Dropbox token present")

    dbx = dropbox.Dropbox(dropbox_access_token)

    print(f"User: {dbx.users_get_current_account()}")

    list_folder_result = dbx.files_list_folder('/Music')

    for file in list_folder_result.entries:
        print(f"File: {file}")

        if type(file) is FolderMetadata:
            print("File is a folder")

        elif type(file) is FileMetadata:
            print(f"Item is a File")
            dbx.files_download_to_file("/home/homelab/media" + file.path_lower)
