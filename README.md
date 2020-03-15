This is a script to parse the COVID-19 data from Johns Hopkins CSSE then
put the data into Elasticsearch. A local copy of the data is in the data
directory. The README.md in that directory has a link to their github repo

# How to use
* Spin up Elasticsearch and Kibana. You can also run it in the cloud, visit
  elastic.co for more info and how to run.
* Run 'pip install -r requirements.txt' to install the depdendencies
* If you're not running Elasticsearch as http://localhost:9200 you will
  need to set the ESURL environment variable. If you need a username and
  password make sure it's part of the URL.
* Run './parser.py', it shouldn't take long.
