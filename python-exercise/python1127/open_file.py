

#with 语句块，可以将文件打开之后，操作完毕，自动关闭这个文件


with open('data.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
   # print(f.readlines())

