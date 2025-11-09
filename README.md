copy and paste your excel file's components into txt1 = '' 

you can set whether to divide by 1000000 or not by moving the location of #. If you put # in front of the 25th line, it will divide by 1000000, and if you put # in front of the 26th line as default, it will not divide by 1000000
    file2.write(element[0]+'-'+element[1]+'\t'+'{:.6f}'.format(float(element[2])/1000000)+'\n')
    #file2.write(element[0]+'-'+element[1]+'\t'+'{:.3f}'.format(float(element[2]))+'\n')

run the code and input the output filename
