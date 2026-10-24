# hw1_python 作业提交（梁煜炜）

图片题目中已打勾（红色手写对勾）的题目共 16 道，全部用 `.py` 实现，放在 `python/hw1/` 目录下，脚本都是独立可运行的，只用标准库。

## 题目与文件对应

| 文件 | 原题位置 | 题目内容 |
| --- | --- | --- |
| `q01_three_digit_numbers.py` | 第 1 天 第一题 | 1、2、3、4 组成多少个互不相同且无重复数字的三位数，各是多少 |
| `q02_sort_three_numbers.py` | 第 1 天 第二题 | 输入三个整数 x、y、z，由小到大输出 |
| `q03_fibonacci.py` | 第 1 天 第三题 | 输出斐波那契数列前 20 项 |
| `q04_digit_count_and_reverse.py` | 数字位数页 第三题 | 求任意正整数是几位数，并逆序打印各位数字 |
| `q05_palindrome.py` | 数字位数页 第四题 | 判断任意正整数是不是回文数 |
| `q06_find_bug.py` | 找 bug 页 第六题 | 找出并说明删除列表奇数代码的 bug，并给出改正方案 |
| `q07_josephus.py` | 找 bug 页 第七题 | 233 人围成一圈报数，报到 3 的人退出，问最后剩下第几号 |
| `q08_person_student.py` | 类与魔术方法页 第三题 | Person 类 + Student 子类，重写 personInfo，重写 `__str__` |
| `q09_random_number_file.py` | 随机数文件页 第三题 | 创建 data.txt，共 100000 行，每行一个 1~100 的随机整数 |
| `q10_create_sequential_files.py` | 随机数文件页 第四题 | 新建 img 目录，创建 100 个文件名互不相同的文件（形如 X4G5.png） |
| `q11_rename_to_jpg.py` | 随机数文件页 第五题 | 在上一题基础上，随机把 50 个文件改名为 .jpg 结尾 |
| `q12_file_second_column_stats.py` | 第 7 天 第一题 | 生成 10 行 3 列逗号分隔的随机数文件，输出第二列的最大/最小/平均/中位数 |
| `q13_file_copy.py` | 第 7 天 第二题 | 生成含 i 行随机 ASCII 可打印字符的 test.txt，并复制为 copy_test.txt |
| `q14_file_append_python.py` | 第 7 天 第三题 | 读取 test.txt，在文件开头和结尾处追加字符串 python |
| `q15_file_diff.py` | 第 7 天 第四题 | 逐行比较 test.txt 与 copy_test.txt，输出内容不同的行号 |
| `q16_batch_create_and_rename.py` | 第 7 天 第五题 | 新建 test 目录，创建 i 个文件、每个 j 行随机字符，再给文件名和每一行末尾加 -python |

## 运行方式

需要 Python 3.8 及以上。

```bash
cd python/hw1
python3 q01_three_digit_numbers.py
```

带输入的题（排序、数字位数、回文数、生成行数、文件个数与行数）在交互模式下按提示输入；直接回车或不输入时会使用脚本内置的示例值，方便一键运行验证。

文件类题目会在**当前工作目录**下生成 `data.txt`、`matrix.csv`、`test.txt`、`copy_test.txt`、`img/`、`test/` 等产物，所以建议先进入一个空目录再运行，例如：

```bash
mkdir -p /tmp/hw1_run && cd /tmp/hw1_run
python3 /path/to/python/hw1/q10_create_sequential_files.py
```

`q11` 依赖 `img/` 里已有文件，`q14` 依赖 `test.txt`，`q15` 依赖 `test.txt` 与 `copy_test.txt`；这些脚本在缺少前置文件时会自动补建，单独运行也不会报错。

## 说明

- `q06` 的输出里包含 bug 原因分析：`range(len(list))` 的长度在循环开始时固定，`list.pop` 让列表变短后索引越界（IndexError）；同时删除元素会让后面的元素前移，导致漏删。改正方案给了倒序遍历、列表推导式、while 修正下标、切片四种，都验证过结果是 500 个偶数。
- `q07` 用列表模拟报数，答案与递推法（`f(n) = (f(n-1) + 3) % n`）交叉验证一致，最后剩下的是原来第 227 号。
