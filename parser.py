#!/usr/bin/env python
# coding: utf-8



import sys
import os
import json
from UserInfo import *



#method to read a file by taking file path  
def readFile(fileName):

    lines = list()
    with open(fileName,'r') as infile:
        try:
            lines = infile.readlines()
        except Exception as e:
            raise Exception('Unable to read the file')
    return lines
    
# parse passwd file to get the grps of each user
def parsePasswd(passwdFile):

    lines = readFile(passwdFile)
    
    if len(lines) > 0:

        dict = {}
        for l in lines:
            
            userInfo = l.split(':')
            if len(userInfo) == 7 :

                newUser = User()
                newUser.uid = userInfo[2]
                newUser.full_name = userInfo[4]
                username = userInfo[0]
                dict[username] = newUser
        return dict

    else:
        raise Exception("passwd file is empty")
  
# check if file is present
def isFilePresent(path):

    flag = os.path.isfile(path)       

    if not flag:
        raise Exception(path + " file not found")
    return True
        

# controller to call all methods and print the output     
def controller(filePaths):

    
    grpFile = ''
    passwdFile = ''
    if len(filePaths) < 2:
        grpFile = '/etc/group'   #default grp file path
        passwdFile = '/etc/passwd' #default passwd file path
    else :
        grpFile = filePaths[2]
        passwdFile =filePaths[1]

    userDataMap = []
    if isFilePresent(grpFile) & isFilePresent(passwdFile):
        userDataMap = parsePasswd(passwdFile)
        userDataMap = parseGrp(grpFile,userDataMap)
   

    for key,value in userDataMap.items():
        userDataMap[key] = {"uid":value.uid,"full_name":value.full_name,"groups":value.groups}
        
    print(json.dumps(userDataMap,indent=4))
    
    

# parse grp file to get the grps of each user
def parseGrp(grpFile,userDataMap):

    lines = readFile(grpFile)

    if len(lines) > 0:

       for l in lines:
            grps = l.split(':')

            if len(grps) == 4 and grps[3] != '\n':
                grps[3] = grps[3].strip()
                usrs = grps[3].split(',')
                for usr in usrs:
                    tempUserData = userDataMap[usr]  
                    presentgrps = tempUserData.groups
                    presentgrps.append(grps[0])
                    tempUserData.grps = presentgrps
                    userDataMap[usr] = tempUserData
        
    else :
        raise Exception("grps is empty")

    return userDataMap







if __name__ == '__main__':

    controller(sys.argv)











