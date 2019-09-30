# 3
import re

string = "The ghost that says boo haunts the loo"
m = re.findall(".o{2}", string)
print(m)


