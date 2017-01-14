def str_algs(str_1):
	str_2=""
	for i in range(len(str_1)):
		str_2=str_2+str_1[-i-1]
	return str_2

print("Введите слово: ")
s=input()
print("Слово наоборот: ")
print(str_algs(s))

