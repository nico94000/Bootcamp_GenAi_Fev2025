numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

print("---")

numbers = [1, 2, 3, 4]
for num in numbers:
    print(num * 20)

print("---")

names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)

print("---")

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)

print("---")

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
common = [val for val in l1 if val in l2]
print(common)

print("---")

words = ["Elie", "Tim", "Matt"]
inverted_lower = [word[::-1].lower() for word in words]
print(inverted_lower)

print("---")

s1 = "first"
s2 = "third"
common_letters = []
for letter in s1:
    if letter in s2 and letter not in common_letters:
        common_letters.append(letter)
print(common_letters)

print("---")

div_by_12 = [num for num in range(1, 101) if num % 12 == 0]
print(div_by_12)

print("---")

word = "amazing"
vowels = "aeiou"
no_vowels = [letter for letter in word if letter not in vowels]
print(no_vowels)

print("---")

list_3x = [[0, 1, 2] for _ in range(3)]
print(list_3x)

print("---")

matrix_10 = [[col for col in range(10)] for _ in range(10)]
print(matrix_10)

