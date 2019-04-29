# nox90.com
# python 2.7 so it can run on Qradar servers...
# Close an offense via API
# usage run.py <apiToken> <hostname> <offense_id> <close reason id>

import requests
import sys

apiToken = sys.argv[0]

# Get host
endpoint = 'https://'+sys.argv[1]+'/api/siem/offenses/'

# Get offense id
offenseId = sys.argv[2]

# Get close reason id
closeReasonId = sys.argv[3]

# strings assemble
url = endpoint+offenseId+'?closing_reason_id='+closeReasonId+'&status=CLOSED'

r = requests.post(url, headers={'Accept': 'application/json', 'SEC': apiToken})
print(r.status_code, r.reason, r.text)
