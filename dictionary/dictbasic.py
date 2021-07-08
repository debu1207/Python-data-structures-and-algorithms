Dict = {1:'Debu', 2:'Patra', 3: {'A':'welcome', 'B':'t0', 'c': 'geeks'}}
print(Dict)

# accessing a element using get:

print(Dict.get(3))
# pop = Dict.popitem()
print(Dict)
# Dict.clear()

values = Dict.values()
print(values)

if Dict.has_key(2):
	print(Dict[2])
