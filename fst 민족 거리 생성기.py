txt1 =''
popList = []
lines = txt1.split('\n')
for i in lines:
    namePop = i.split('\t')[0]
    popList.append(namePop)
filename = input('파일 이름을 입력하시오 : ')
file2 = open(filename+'.txt','w',encoding='utf8')

lst = []
numVertical = 1
while numVertical < len(lines):
    numHorizontal = 1
    while numHorizontal < len(lines):
        line = lines[numVertical]
        lst.append([lines[numVertical].split('\t')[0], 
                lines[0].split('\t')[numHorizontal],
                lines[numVertical].split('\t')[numHorizontal]])
        numHorizontal+=1
    numVertical += 1
lst = sorted(lst,key = lambda x:(x[0],float(x[2])))
for element in lst:
    if float(element[2]) <= 0:
        element[2] = 0.000000
    file2.write(element[0]+'-'+element[1]+'\t'+'{:.6f}'.format(float(element[2])/1000000)+'\n')
    #file2.write(element[0]+'-'+element[1]+'\t'+'{:.3f}'.format(float(element[2]))+'\n')


file2.close()