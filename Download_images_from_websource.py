# unnecessary print statements are in the code so i can better visualize the execution
import urllib.request
import urllib.parse
import re
from os.path import basename
import tld

url = input("ENTER THE WEBSITE URL : ")
source_file_name = tld.get_tld(url) + ".txt"
print(source_file_name)
response = urllib.request.urlopen(url)
source = response.read()
with open(source_file_name, "wb") as file:
    file.write(source)

patten = '(http)?s?:?(\/\/[^"]*\.(?:png|jpg|jpeg|gif|png|svg))'
for line in open(source_file_name):
    for m in re.findall(patten, line):
        # re.findall saves the results in an array thats why we use m[1], m[0] not relevant here
        print(re.findall(patten, line))
        # m[1] contains the path to the file without the https: so we add it below
        print('https:' + m[1])
        # urlsplit has different parameters we take the [2] one to get the location without the TLD in it
        print(urllib.parse.urlsplit(m[1]))
        # basename returns the final component of an address eg. www.google.com/t/hello.png would return hello.png
        fileName = basename(urllib.parse.urlsplit(m[1])[2])
        print("File is saved as " + fileName)
        try:
            img = urllib.request.urlopen('https:' + m[1]).read()
            with open(fileName, "wb") as file:
                file.write(img)
        except:
            pass
        break