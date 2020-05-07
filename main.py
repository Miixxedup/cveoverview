import utils.request_data as rd
import utils.handle_json_zip as hjz

FEEDNAME = "CVE-2020"

#Download the feed if exists
rd.do_request(FEEDNAME, meta = False)

#Unzips the feed if required
hjz.unzip_feed(FEEDNAME)

#Load .json into memory
data = hjz.load_json(FEEDNAME)