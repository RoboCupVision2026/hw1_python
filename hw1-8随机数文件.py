import random
with open('data.txt', 'w', encoding='utf-8') as f:
    nums = [str(random.randint(1, 100)) for i in range(10000)]
    f.write('\n'.join(nums))