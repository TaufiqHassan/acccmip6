# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 04:07:07 2019

@author: Taufiq
"""
import requests

def setup_module(module):
    global url1 
    global url2 
    global url3_1
    global url3_2
    global url3_3
    global url3_4
    global url4_1
    global url4_2
    global url4_3
    global url4_4
    
    url1 = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_source_id.html"
    url2 = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_experiment_id.html"
    url3_4 = "https://esgf-data.dkrz.de/search/cmip6-dkrz/"
    url3_3 = "https://esgf-index1.ceda.ac.uk/search/cmip6-ceda/"
    url3_1 = "https://esgf-node.llnl.gov/search/cmip6/"
    url3_2 = "https://esgf-node.ipsl.upmc.fr/search/cmip6-ipsl/"
    url4_1 = "https://esgf-node.llnl.gov/esg-search/wget?project=CMIP6"
    url4_2 = "https://esgf-node.ipsl.upmc.fr/esg-search/wget?project=CMIP6"
    url4_3 = "https://esgf-index1.ceda.ac.uk/esg-search/wget?project=CMIP6"
    url4_4 = "https://esgf-data.dkrz.de/esg-search/wget?project=CMIP6"
    
def teardown_module(module):
    R.close()

def test_checkUrl1():
    global R
    R = requests.get(url1)
    assert R.status_code == 200
    
def test_checkUrl2():
    global R
    R = requests.get(url2)
    assert R.status_code == 200
    
def test_checkUrl3():
    global R
    try:
        if (requests.get(url3_1,timeout=10)):
            R=requests.get(url3_1)
    except:
        try:
            if (requests.get(url3_2,timeout=10)):
                R=requests.get(url3_2)
        except:
            try:
                if (requests.get(url3_3,timeout=10)):
                    R=requests.get(url3_3)
            except:
                try:
                    if (requests.get(url3_4,timeout=10)):
                        R=requests.get(url3_4)
                except:
                    print("\nAll servers down!!\nCheck back later.")
        
    assert R.status_code == 200
    
def test_checkUrl4():
    global R
    try:
        if (requests.get(url4_1,timeout=10)):
            R=requests.get(url4_1)
    except:
        try:
            if (requests.get(url4_2,timeout=10)):
                R=requests.get(url4_2)
        except:
            try:
                if (requests.get(url4_3,timeout=10)):
                    R=requests.get(url4_3)
            except:
                try:
                    if (requests.get(url4_4,timeout=10)):
                        R=requests.get(url4_4)
                except:
                    print("\nAll servers down!!\nCheck back later.")
        
    assert R.status_code == 200