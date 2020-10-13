import time
import json
import dicttoxml
t = time.time()
with open('raspis.json') as f:
  a = json.load(f)
xml = dicttoxml.dicttoxml(a)
with open("output.xml", "w+") as h:
  h.write(xml)
t = (time.time() - t)
