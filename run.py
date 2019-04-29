# nox90.com
# python 2.7 so it can run on Qradar servers...
# Close an offense via API
# usage run.py <hostname> <offense_id> <close reason id>

APIKEY = ''


import requests
import sys

# Get host
endpoint = 'https://'+sys.argv[0]+'/api/siem/offenses/'

# Get offense id
offenseId = sys.argv[1]

# Get close reason id
closeReasonId = sys.argv[2]

# strings assemble
url = endpoint+offenseId+'?closing_reason_id='+closeReasonId+'&status=CLOSED'

r = requests.post(url)
print(r.status_code, r.reason)
