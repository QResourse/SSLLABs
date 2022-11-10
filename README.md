This code is based on ssllabs.py
This code provide the capability to add domains to CSV and extract data for multiple certificates. 


# Use:
- Add domains to domains.csv.sample
- rename domains.csv.sample to domains.csv
- execute main.py

# ssllabs.py
Python module for the Qualys SSL Labs Server Test

Dependencies:

Requires the third-party Python Requests library - http://docs.python-requests.org/en/latest/

Developed with support of Python 2/3.

Use:

Download module and navigate inside ssllabs folder.

Then:

import ssllabsscanner

For results from cache:

data = ssllabsscanner.resultsFromCache("www.qualys.com")

data now contains a JSON object that can be parsed for your needs.

Parse the object to determine your grade:

print(data['endpoints'][0]['grade'])

For retrieving the data from a new scan:

data = ssllabsscanner.newScan("www.qualys.com")

data now contains a JSON object that can be parsed for your needs.
