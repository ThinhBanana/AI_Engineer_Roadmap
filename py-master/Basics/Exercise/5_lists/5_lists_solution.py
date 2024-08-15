# 1
month = ['January', 'February', 'March', 'April', 'May']
expense = [2200, 2350, 2600, 2130, 2190]
ex1_1 = expense[1] - expense[0]

ex1_2 = sum(expense[:3])

idx = [id for id, exp in enumerate(expense) if exp == 2200]
ex1_3 = []
for id in idx:
    ex1_3.append(month[id])

ex1_4 = ''
month.append('June')
expense.append(1980)

expense[3] -= 200

# 2
heros=['spider man', 'thor', 'hulk', 'iron man', 'captain america']
ex2_1 = len(heros)

ex2_2 = ''
heros.append('black panther')

ex2_3 = ''
heros.remove('black panther')
heros.insert(3, 'black panther')

ex2_4 = ''
heros[1:3] = ['doctor strange']
print(heros)

ex2_5 = ''
heros.sort()

print(heros)
