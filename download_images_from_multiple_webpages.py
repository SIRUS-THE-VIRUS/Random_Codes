# unnecessary print statements are in the code so i can better visualize the execution
import urllib.request
import urllib.parse
import re
from os.path import basename
import tld

url = 'https://www.packtpub.com/'
queary = 'all?search=&offset='

for i in range(0,48,12):
    url += queary + str(i)
    source_file_name = tld.get_tld(url) + str(i) + ".txt"
    print(source_file_name)
    response = urllib.request.urlopen(url)
    source = response.read()
    with open(source_file_name, "wb") as file:
        file.write(source)
for i in range(0,48,12):
    patten = '(http)?s?:?(\/\/[^"]*\.(?:png|jpg|jpeg|gif|png|svg))'
    for line in open(tld.get_tld(url) + str(i) + ".txt"):
        for m in re.findall(patten, line):
            print('https:' + m[1])
            fileName = basename(urllib.parse.urlsplit(m[1])[2])
            print("File is saved as " + fileName)
            request = 'https:' + urllib.parse.quote(m[1])
            img = urllib.request.urlopen(request).read()
            with open(fileName, "wb") as file:
                file.write(img)
            break