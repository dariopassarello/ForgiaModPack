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
password = "**********" #Inserire password



def getNumberOfRequest():
    authResponse = requests.get(urlRate, auth=(user, password))
    print(authResponse.content)
    jsonResponse = authResponse.content.decode()
    j = json.loads(jsonResponse)
    return j['resources']['core']['limit']

'''
homeUrl: Root del repo e.g. /repos/dariopassarello/ForgiaModPack/contents
pathsToVisit: array che contiene le cartelle che devono essere analizzate ricorsivamente
outputJsonArray: Un array passato inizialmente vuoto 
'''
def getTreeJson(homeUrl,pathsToVisit,outputJsonArray):
    for dirToVisit in pathsToVisit:
        jsonTreeResponse = requests.get(homeUrl + dirToVisit,auth=(user, password))
        jsonTreeString  = jsonTreeResponse.content.decode()
        jsonTreeArray = json.loads(jsonTreeString)
        for element in jsonTreeArray:
            if element['type'] == 'file':
                elementStruct = {}
                print()
                elementStruct['path'] = element['path']
                elementStruct['download_url'] = element['download_url']
                outputJsonArray.append(elementStruct)
            else:
                newPaths = []
                newPaths.append(element['path'])
                getTreeJson(homeUrl,newPaths,outputJsonArray)
    return json.dumps(outputJsonArray)

ogg = []
print(getTreeJson(urlBase,['mods','config'],ogg))

