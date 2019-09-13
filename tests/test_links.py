# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 04:07:07 2019

@author: Taufiq
"""
import requests

def setup_module(module):
    global url1 
    global url2 
    global url3 
    global url4
    url1 = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_source_id.html"
    url2 = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_experiment_id.html"
    url3 = "https://esgf-data.dkrz.de/search/cmip6-dkrz/"
    url4 = "https://esgf-node.llnl.gov/esg-search/wget?project=CMIP6"
    
def teardown_module(module):
    r.close()

def test_checkUrl1():
    global r
    r = requests.get(url1)
    assert r.status_code == 200
    
def test_checkUrl2():
    global r
    r = requests.get(url2)
    assert r.status_code == 200
    
def test_checkUrl3():
    global r
    r = requests.get(url3)
    assert r.status_code == 200
    
def test_checkUrl4():
    global r
    r = requests.get(url4)
    assert r.status_code == 200