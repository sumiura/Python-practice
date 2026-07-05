print("Hello, World!")
print("Hello, Codex!")
print("Hello, Python!") 
print("Hello, GitHub!")

numbers = []

for i in range(3):
    number = float(input(f"{i + 1}つ目の数字を入力してください: "))
    numbers.append(number)

average = sum(numbers) / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(f"平均値: {average:.3f}")
print(f"最大値: {maximum}")
print(f"最小値: {minimum}")
