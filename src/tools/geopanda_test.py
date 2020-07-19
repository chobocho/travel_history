import geopandas as gpd
import matplotlib.pyplot as plt
import json
import os

def loadJson(filename):
    if (os.path.isfile(filename)):
        file = open(filename, 'r', encoding="UTF-8")
        lines = file.readlines()
        file.close()

        result = {}
        for line in lines:
            country = json.loads(line)
            item = {}
            item['region'] = country["region"]
            item['name'] = country["name"]
            item['english_name'] = country["english_name"]
            result[item['name']] = item
        print("Success to load " + filename)
    return result

def save2file(data, fileName="world.cfm"):
    savedata = []
    for country in data:
        item = {}
        item["region"] = country[1]
        item["name"] = country[0]
        item["english_name"] = country[0]
        itemString = json.dumps(item)
        savedata.append(itemString)

    with open(fileName, 'w') as outfile:
        for item in savedata:
            outfile.write(item)
            outfile.write('\n')

    print("Success to save at " + fileName)
    return True

def saveJson(data):
    europe = data.drop(columns=['gdp_md_est', 'geometry'])
    print(len(europe))
    europe = europe.T
    worldinfo = []
    for k, c in europe.items():
        #print (c['continent'], c['name'])
        item = []
        item.append(c['name'])
        item.append(c['continent'])
        worldinfo.append(item)

    worldinfo.sort(key=lambda x: (x[1], x[0]))
    save2file(worldinfo)

def drawEurope(world):
   saveJson(world)
   #europe = world[world.reg]
   #plt.show()

def main():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world = world[(world.pop_est > 0) & (world.name != "Antarctica")]
    #world.plot(figsize=(15,10))
    #plt.show()
    drawEurope(world)
    data = loadJson("world.cfm")
    for i, v in data.items():
        print(v)

if __name__ == '__main__':
    main()