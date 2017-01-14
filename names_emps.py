def names_emps(arr):
	names=[]
	for i in arr:
		for m in i['children']:
			if m['age']>=18:
				names.append(i['name'])
				break
	return names

ivan = {
    "name":"ivan",
	"age":34,
	"children":
		[{
		"name":"vasja",
		"age":12,
		},
		{
		"name":"petja",
		"age":10,
		}],
	}
darja={
	"name":"darja",
	"age":41,
	"children":
		[{
		"name":"kirill",
		"age":21,
		},
		{
		"name":"pavel",
		"age":20,
		}],
	}


emps=[ivan, darja]
print(names_emps(emps))
