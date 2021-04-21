import os 
import shutil 

source= input("Enter the source path")
destination=input("Enter the destination")
source=source+'/'
destination=destination+'/'

ListOfFiles=os.listdir(source)
for file in ListOfFiles:
    shutil.copy((source+file),destination)