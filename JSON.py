import json
from jnpr.junos import Device
from pprint import pprint

dev = Device('10.209.1.228', user='regress', password='MaRtInI')

dev.open()
dev.facts['version_info']=dict(dev.facts['version_info'])
print "\nPrinting facts using pprint:\n"
pprint(dev.facts)

print "\nPrinting facts in JSON format:\n"
print json.dumps(dev.facts, indent=2)

print "\nPrinting facts in JSON format using pprint:\n"
pprint(json.dumps(dev.facts))

dev.close()
