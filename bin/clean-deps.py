#!/usr/bin/env python
import yaml
import subprocess


with open('requirements.yml', 'r') as handle:
    desired = yaml.safe_load(handle)

desired = {x.get('name', x['src']): x['version'] for x in desired}
if any([isinstance(v, int) or isinstance(v, float) for v in desired.values()]):
    raise Exception("One of your values is a float! Please make it a string in the yaml file.")


current = subprocess.check_output(['ansible-galaxy', 'role', 'list', '-p', 'roles']).decode('utf8').split('\n')
current = [x[2:].split(', ') for x in current if x.startswith('- ')]
current = {x[0]: x[1].strip() for x in current}

for k, v in desired.items():
    # If we haven't installed that library yet
    if k not in current:
        continue

    if v != current[k]:
        print("role=%s\tcurrent=%s\tdesired=%s" % (k, current[k], desired[k]))
        print("Removing role!")
        print(subprocess.check_output(['ansible-galaxy', 'remove', k, '-p', 'roles']).decode('utf-8'))
