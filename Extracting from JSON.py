import urllib
import json

url = input("Enter json URL: ")
# http://py4e-data.dr-chuck.net/comments_458707.json
connection = urllib.urlopen(url)
raw_data = connection.read()
parsed_data = json.loads(raw_data)
counts = []

comments = parsed_data["comments"]

for comment in comments:
    counts.append(comment['count'])

print ("Count: {0}".format(len(counts)))
print ("Sum: {0}".format(sum(counts)))