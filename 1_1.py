#三位数组合
digits = [1, 2, 3, 4]
count = 0

for hundreds in digits:
    for tens in digits:
        for ones in digits:
            if hundreds != tens and hundreds != ones and tens != ones:
                number = hundreds * 100 + tens * 10 + ones
                print(f"{number} ")
                count += 1

print()
print(f"一共有 {count} 个三位数。")
