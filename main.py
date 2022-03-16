import os
source = 'C:\\Users\\allan\\OneDrive\\Desktop\\FolderA\\File0314.txt'
destination = 'C:\\Users\\allan\\OneDrive\\Desktop\\FolderB\\File0314(moved).txt'
try:
    os.rename(source,destination)
    print(source+' has been successfully moved from FolderA to FolderB!')
except FileNotFoundError:
    os.rename(destination,source)
    print(source+' has been successfully moved from FolderB to FolderA!')