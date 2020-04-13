# 读取文本文件
try:
    f = open("d:/source/pythonLearn/pythonLearn/funTest.py", 'r', encoding='utf-8')
    print("读到的文件内容：")
    for i in range(10):
        s = f.read(100)
        print('s=', s)
        print(len(s))
    print(dir(f))
finally:
    if f:
        f.close()

# 读二进制文件，‘rb’ 读取二进制文件, read(size) 每次读取指定大小
# readLine

# 使用with可自动帮我们调用close()方法
with open('d:/source/pythonLearn/pythonLearn/funTest.py', 'r', encoding='utf-8') as f:
    print(f.read(100))

