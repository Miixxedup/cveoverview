import requests
import pathlib
import utils.import_config as c

DOWNLOAD_FILETYPE = "json"


# Request the payload, checks for existence of feeds
def do_request(feed, meta = False):
    # Check if feed exists
    if check_feed(feed) == "Unknown":
        exit()
    # Checks for a metafile download or the jsonblob and sets variables
    # Currently windows only! #TODO edit filepaths
    if meta:
        store_location = f"{pathlib.Path().absolute()}/blobs/xml/"
        config_type = "META"
        extension = ".meta"
    else:
        store_location = f"{pathlib.Path().absolute()}/blobs/json/"
        config_type = "ZIP"
        extension = ".json.zip"

    #Collect and store feed data
    print(f"Fetching {feed} ... ")
    print(c.CONFIG["feeds"][feed][config_type])

    response = requests.get(c.CONFIG["feeds"][feed][config_type])
    
    print(f"Storing data in {store_location+feed+extension}")
    with open(f'{store_location+feed+extension}', 'wb+') as file:
        file.write(response.content)
        print("Done!")
    

# Check if the feed is known in the config
def check_feed(feed):
    if feed not in c.CONFIG["feeds"]:
        print(f"Please choose a feed specified in the config.yml")
        return "Unknown"
    else:
        return "Known" 