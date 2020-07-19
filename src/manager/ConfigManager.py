#!/usr/bin/python
#-*- coding: utf-8 -*-

import manager.FileManager as fm

class ConfigManager:
    def __init__(self):
        print("__init__")
        self.config = {'region':[], 'newtork':[], 'country':{}}
        self.__loadConfigfile()
        self.__loadWorldInfo()

    def __loadConfigfile(self):
        self.config = fm.loadConfig('info/config.json')
        self.config['country'] = {}
        for region in self.config['region']:
            self.config['country'][region] = []

    def __loadWorldInfo(self):
        country = fm.loadWorldInfo('info/worldinfo.cfm')
        for k, c in country.items():
            self.config['country'][c['region']].append(c['name'])

    def getRegionList(self):
        print(self.config['region'])
        return self.config['region']

    def getCountryList(self, region):
        if len(region) == 0:
            return []
        #print(self.config['country'][region])
        return self.config['country'][region]

    def getNetworkList(self):
        return self.config['network']
