
#쓰기!

with open('test.txt','w') as fd:
    fd.write("test")
    fd.write("test2")

#읽기!
with open('test.txt', 'r') as fd:
    for line in fd:
        print(line)