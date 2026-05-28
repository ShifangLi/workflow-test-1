import yaml
from pathlib import Path

yamlPath = Path(__file__).parent / 'dev.yaml'
with open(yamlPath, 'r') as f:
    x = yaml.safe_load(f)

print(x)
# print(x['ip'])
# print(x['allow_hosts'])