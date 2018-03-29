import json
import requests



#COSTANTI
url = "https://api.github.com"
urlMods = url + "/repos/dariopassarello/ForgiaModPack/contents/mods"
urlBase = url + "/repos/dariopassarello/ForgiaModPack/contents"
urlConfig = url + "/repos/dariopassarello/ForgiaModPack/contents/config"
urlAuth = url + "/repos/d/ForgiaModPack"
urlRate = url + "/rate_limit"
user = "spiritodellaforgia@gmail.com"
password = "********" #password here



def getNumberOfRequest():
    authResponse = requests.get(urlRate, auth=(user, password))
    print(authResponse.content)
    jsonResponse = authResponse.content.decode()
    j = json.loads(jsonResponse)
    return j['resources']['core']['limit']

'''
homeUrl: Root del repo e.g. /repos/dariopassarello/ForgiaModPack/contents
pathsToVisit: array che contiene le cartelle che devono essere analizzate ricorsivamente
outputJsonArray: Un array passato inizialmente o con altri dati
'''
def getTreeJson(homeUrl,pathsToVisit,outputJsonArray):
    files = 0
    subFolders = 0
    for dirToVisit in pathsToVisit:
        jsonTreeResponse = requests.get(homeUrl + dirToVisit,auth=(user, password))
        jsonTreeString  = jsonTreeResponse.content.decode()
        jsonTreeArray = json.loads(jsonTreeString)
        for element in jsonTreeArray:
            if element['type'] == 'file':
                elementStruct = {}
                print("Found file: ",element['path'])
                files = files + 1
                elementStruct['path'] = element['path']
                elementStruct['download_url'] = element['download_url']
                elementStruct['size'] = element['size']
                elementStruct['hash'] = element['sha']
                outputJsonArray['files'].append(elementStruct)
            else:
                subFolders = subFolders + 1
                newPaths = []
                print("Found folder: ",element['path'])
                newPaths.append(element['path'])
                getTreeJson(homeUrl,newPaths,outputJsonArray)
    print("FOLDER ",dirToVisit," FINISHED")
    print("NUMBER OF FILES FOUND:",files)
    print("NUMBER OF FOLDERS FOUND:",subFolders)
    print("--------------------------------------------")
    return json.dumps(outputJsonArray,indent=4)

def getDirsHashesJson(homeUrl,dirsToSearch,outputJsonStruct):
    outputJsonStruct['hashes'] = []
    jsonString = requests.get(homeUrl, auth=(user,password)).content.decode()
    jsonArray = json.loads(jsonString)
    for dirName in dirsToSearch:
        for object in jsonArray:
            if dirName == object['name']:
                jsonHashStruct = {}
                jsonHashStruct['name'] = object['name']
                jsonHashStruct['hash'] = object['sha']
                outputJsonStruct['hashes'].append(jsonHashStruct)
    return json.dumps(outputJsonStruct,indent=4)



ogg = {}
getDirsHashesJson(urlBase,['mods','config'],ogg)
print("JSON PARSER")
print("NUMBER OF REQUEST REMAINING: ",getNumberOfRequest())
ogg['files'] = []
jsonOut = getTreeJson(urlBase,['mods','config'],ogg)
print("SCAN COMPLETED\nHERE'S THE JSON:\n",jsonOut)
print("You can find the json in manifest.json")
f = open("manifest/manifest.json","w")
f.write(jsonOut)
