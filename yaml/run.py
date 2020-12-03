import yaml

data = {}

with open('et.yml','r+') as f:
    data = yaml.safe_load(f)
    print(data)

data['test'] = "vs"

with open('et.yml','wt') as f:
    yaml.dump(data, f)
