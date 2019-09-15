# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 04:07:07 2019

@author: Taufiq
"""
import requests

def test_checkUrl1():
    url1 = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_source_id.html"
    R = requests.get(url1)
    R.close()
    assert R.status_code == 200
    
def test_checkUrl2():
    url2 = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_experiment_id.html"
    R = requests.get(url2)
    R.close()
    assert R.status_code == 200
    
def test_checkUrl3():
    url3_4 = "https://esgf-data.dkrz.de/search/cmip6-dkrz/"
    url3_3 = "https://esgf-index1.ceda.ac.uk/search/cmip6-ceda/"
    url3_1 = "https://esgf-node.llnl.gov/search/cmip6/"
    url3_2 = "https://esgf-node.ipsl.upmc.fr/search/cmip6-ipsl/"
    try:
        if (requests.get(url3_1,timeout=10)):
            R=requests.get(url3_1)
            R.close()
    except:
        try:
            if (requests.get(url3_2,timeout=10)):
                R=requests.get(url3_2)
                R.close()
        except:
            try:
                if (requests.get(url3_3,timeout=10)):
                    R=requests.get(url3_3)
                    R.close()
            except:
                try:
                    if (requests.get(url3_4,timeout=10)):
                        R=requests.get(url3_4)
                        R.close()
                except:
                    print("\nAll servers down!!\nCheck back later.")
        
    assert R.status_code == 200
    
def test_checkUrl4():
    url4_1 = "https://esgf-node.llnl.gov/esg-search/wget?project=CMIP6"
    url4_2 = "https://esgf-node.ipsl.upmc.fr/esg-search/wget?project=CMIP6"
    url4_3 = "https://esgf-index1.ceda.ac.uk/esg-search/wget?project=CMIP6"
    url4_4 = "https://esgf-data.dkrz.de/esg-search/wget?project=CMIP6"
    try:
        if (requests.get(url4_1,timeout=10)):
            R=requests.get(url4_1)
            R.close()
    except:
        try:
            if (requests.get(url4_2,timeout=10)):
                R=requests.get(url4_2)
                R.close()
        except:
            try:
                if (requests.get(url4_3,timeout=10)):
                    R=requests.get(url4_3)
                    R.close()
            except:
                try:
                    if (requests.get(url4_4,timeout=10)):
                        R=requests.get(url4_4)
                        R.close()
                except:
                    print("\nAll servers down!!\nCheck back later.")
        
    assert R.status_code == 200