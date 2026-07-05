import random

n = int(input("何回さいころを振りますか？ "))
for i in range(1, n + 1):
    input("さいころを振るにはエンターキーを押してください...")
    print(f"{i:>2} 回目 🎲", random.randint(1, 6))
