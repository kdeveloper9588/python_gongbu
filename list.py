evennumbers = [2, 4, 6, 8, 10]
oddnumbers = [1, 3, 5, 7, 9]

numbers = evennumbers + oddnumbers
print(numbers)
print(numbers * 4)

numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[4] = 100
print(numbers)

numbers[2] = "hello"
print(numbers)

numbers[0] = numbers[9] #인덱스 9를 인덱스 0에 대입
print(numbers)

numbers[8] = ['a', 'b', 'c'] #리스트 전체를 형태 유지하며 대입
print(numbers)

numbers[:] = [1]
print(numbers)