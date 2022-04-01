
count_of_person = int(input("Please enter the number of people you wanted to try for gun shooting ...! "))
def index_of_soldier_won(count_of_person):
	array = [0] * count_of_person

	for i in range(count_of_person):
		array[i] = i + 1

	index_of_person = 0

	while (len(array) > 1):
		index_of_person += 1
		index_of_person %= len(array)
		del array[index_of_person]

	return(array[0])

print(index_of_soldier_won(count_of_person))
