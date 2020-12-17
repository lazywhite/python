import yaml
from pprint import pprint

data = {}

with open('et.yml','r+') as f:
    data = yaml.safe_load(f)

pprint(data)
pprint(data.get("foo"))
pprint(data.get("bar"))

data['test'] = "vs"

#with open('et.yml','wt') as f:
#    yaml.dump(data, f)
