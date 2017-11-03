import yaml

with open('et.yml','r+') as f:
    data = yaml.load(f)
    print(data)
