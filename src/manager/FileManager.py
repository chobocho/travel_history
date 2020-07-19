#!/usr/bin/python
#-*- coding: utf-8 -*-
import logging
import os
import json
from store import loadfilev2, savefilev2


class FileManager:
    def __init__(self):
        self.logger = logging.getLogger("chobomemo")
        self.saveFileName = ".\\20201105.cfm"
        self.alternativeDataFileName = "d:\\cfm20181105.cfm"

    def loadDataFile(self, fileName=""):
        dataFile = self.saveFileName

        if len(fileName) > 0:
            self.logger.info(fileName)
            dataFile = fileName
        if os.path.isfile(dataFile) == False:
            self.logger.warning("File not exist " + dataFile)
            dataFile = self.saveFileName
        if os.path.isfile(dataFile) == False:
            self.logger.warning("File not exist " + dataFile)
            dataFile = self.alternativeDataFileName

        if (os.path.isfile(dataFile)) == False:
            return {}

        version = ""
        try:
            file = open(dataFile, 'rt', encoding="UTF-8")
            version = file.readline()
            file.close()
        except:
            self.logger.exception("File to load " + dataFile)
            return {}

        self.saveFileName = dataFile
        fm = loadfilev2.LoadFile()
        return fm.loadfile(dataFile)


    def saveDataFile(self, memoList, fileName=""):
        saveFileName = self.saveFileName

        if len(fileName) > 0:
            saveFileName = fileName
            self.saveFileName = saveFileName

        fm = savefilev2.SaveFile()
        fm.savefile(memoList, saveFileName)

        self.logger.info("Success to save at " + self.saveFileName)
        return True


def loadConfig(filename):
    print("loadConfig: " + filename)
    if not os.path.exists(filename):
        print (filename, "not exist!")
        return {}

    config_data = {}
    with open(filename) as json_file:
        config_data = json.load(json_file)
    return config_data


def loadWorldInfo(filename):
    if not os.path.exists(filename):
        return {}

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

def test():
    fm = FileManager()
    fm.loadDataFile()
    '''For unittest'''

