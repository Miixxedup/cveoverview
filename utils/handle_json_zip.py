import pathlib
import zipfile
import json

# Unzip the feed and store it into a new folder with the json blob
def unzip_feed(feed):
    print(f"Unzipping: {feed}")
    feed_store_location = f"{pathlib.Path().absolute()}/blobs/json/{feed}.json.zip"
    with zipfile.ZipFile(feed_store_location, 'r') as zipped:
        zipped.extractall(feed_store_location.split(".zip")[0])
        print("Done")

# Loads the correct .json file corresponding with the feedname.
def load_json(feed):
    feed_store_location = f"{pathlib.Path().absolute()}/blobs/json/{feed}.json"
    # Checks for json files in the dir
    filename = list(pathlib.Path(feed_store_location).iterdir())
    if len(filename) != 1:
        print("Found multiple .json files, exiting...")
        exit()
    
    with open(filename[0], 'r', encoding="utf8") as f:
        blob = json.load(f)
        print("json imported!")
    return blob
    
