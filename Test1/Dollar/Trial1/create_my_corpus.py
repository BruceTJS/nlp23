import re
if __name__=="__main__":
    f=open('mycorpus.txt','w')
    for i in range(4):
        f.write('this is 4'+str(i)+' dollars'+'\n')
    for i in range(5,10):
        f.write('this is $4'+str(i)+' million'+'\n')
    for i in range(1,2):
        f.write('I have many many $'+str(i)+' cash'+'\n')
    f.write("and I have $10 cash also 666")
    f.close

    print('---sucess---------')
    print(re)
    print(dir(re))