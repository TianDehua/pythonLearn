import os
import os.path

#当前路径
currentPath = os.path.abspath('.')

print('currentPath=', currentPath)

#增加一个路径
testDir = os.path.join(currentPath, 'testdir')
if not os.path.exists(testDir):
    os.mkdir(testDir)

splitDir = os.path.split(testDir)
print(splitDir)

#查看当前路径下的文件
L = os.listdir('.')
print('fileList=', L)

#过滤文件夹
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print('dirList=', L)

L = [x for x in os.listdir('.') if os.path.isfile(x)]
print('fileList=', L)

def listAllFile(di):
    print('checkPath=', di)
    for x in os.listdir(di):
        if os.path.isfile(x):
            print('file:', os.path.relpath(x))
        elif os.path.isdir(x):
            print('dir:', os.path.abspath(x))
            listAllFile(os.path.join(di, x))
        else:
           print('unkown:', os.path.abspath(x)) 

listAllFile('.')
