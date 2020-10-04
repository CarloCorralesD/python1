import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print(x)

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"],y["name"])
print(y)

z= json.dumps(y, indent=4, sort_keys=True)
print(z)
print(z==x)
