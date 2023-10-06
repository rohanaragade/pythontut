import os
import shutil
# os.mkdir("./DemoDir")   #Create new directory in specifies path
# os.mkdir("./DemoDir1")   #Create new directory in current dir
# print(os.getcwd())      #Retruns current working dir

# os.chdir('./DemoDir')
# print(os.getcwd())

# print(os.listdir())     # list all sub-directories

# os.mkdir("./Test")

# os.rename('Test','New Dir') #Renaming dir

os.remove("./DemoDir/Test.py")  #removing file

# shutil.rmtree('./New Dir')    #Removing dir with its contents
# shutil.rmtree('./Test')    #Removing dir with its contents

# delete the empty directory "mydir"
# os.rmdir("./Test")