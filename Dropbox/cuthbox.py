import pathlib

import dropbox
import os
import json
from dropbox.files import FolderMetadata, FileMetadata

dropbox_access_token = os.getenv('DROPBOX_ACCESS_TOKEN')



def process_folder(dbx, folder):

    list_folder_result = dbx.files_list_folder(folder)

    for file in list_folder_result.entries:
        print(f"File: {file}")

        if type(file) is FolderMetadata:
            print("File is a folder")
            process_folder(dbx, file.path_lower)

        elif type(file) is FileMetadata:
            print(f"Item is a File")
            full_path = pathlib.Path("/opt" + file.path_lower)
            print(f"Full Path: {full_path}")
            if not os.path.isfile(full_path):
                full_path.parent.mkdir(parents=True, exist_ok=True)
                dbx.files_download_to_file(str(full_path), file.path_lower)


if __name__ == "__main__":

    print(f"Cuthbeorht's Sync Script starting...")

    if not dropbox_access_token:
        raise Exception("No Dropbox token present")

    dbx = dropbox.Dropbox(dropbox_access_token)

    print(f"User: {dbx.users_get_current_account()}")

    process_folder(dbx, '/Music')

    print(f"Cuthbeorht's Sync Script finished")
