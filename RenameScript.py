import os
import shutil
for folderName,subFolders, filenames in os.walk('C:/Users/addison/Documents/MainFolder'):
    for i in filenames:
        stringfile = str(i[0:-4])
        newstringfile = ''
        neweststringfile = ''
        for j in stringfile:
           
    
            if j !='$':
                newstringfile += j
        for k in newstringfile:
                if k == '.':
                    neweststringfile += '-'
                else:
                    neweststringfile += k
                    
        newfilename = (neweststringfile + '.txt')
        #newpath = os.join(folderName,newfilename)
        oldpath = folderName + '\\' + i
        newpath = folderName + '\\' + newfilename
        os.rename(oldpath,newpath)
        
        
