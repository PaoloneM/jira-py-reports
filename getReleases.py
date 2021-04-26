from atlassian import Jira
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

packages = 0

key_cert_data = None
key_cert = './jira.pem'
with open(key_cert, 'r') as key_cert_file:
    key_cert_data = key_cert_file.read()

oauth_dict = {
    'access_token': os.environ['access_token'],
    'access_token_secret': os.environ['access_token_secret'], 
    'consumer_key': os.environ['consumer_key'],
    'key_cert': key_cert_data
}

jira = Jira(
    url=os.environ['JIRA_URL'],
    oauth=oauth_dict
)

projects = jira.projects(included_archived=None)

for prj in projects:
    try:
        if prj['projectCategory']['name'] == os.environ['CATEGORY']:
          versions = [v for v in jira.get_project_versions(prj['key']) if v['released'] and v['releaseDate'].find(os.environ['YEAR']) != -1]
          if versions is not None and len(versions) > 0:
            print('Project: ' + prj['name'])
          for v in versions:
            print('            |--' + v['name'] + ' - ' + v['releaseDate'])
            packages += 1
    except Exception:
        None

print('\n********************************************')
print('*** Total releases in year', os.environ['YEAR'], ': ', packages, ' ***')
print('********************************************\n')
