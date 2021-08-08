motorcycles = []
motorcycles.append('honda')
motorcycles.insert(1, 'yamaha')
motorcycles.append('suzuki')
motorcycles.insert(1, 'ducati')

del motorcycles[1]

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
