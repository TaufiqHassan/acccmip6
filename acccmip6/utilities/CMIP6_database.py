# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:39:39 2019
"""
import re
import pandas as pd # pandas for data handling
import pkg_resources

from acccmip6.utilities.util import _fetch_url, _choose_server

class CMIP6DB:
    
    _Turl = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_source_id.html"
    _ETurl = "https://rawgit.com/WCRP-CMIP/CMIP6_CVs/master/src/CMIP6_experiment_id.html"
    _Curl = "https://esgf-node.llnl.gov/search/cmip6/"
    
    def __init__(self, **options):
        self._total = 0
        self._avail = 0
        self._holder = []
        self._fdata = []
    
    @classmethod
    def _set_curl(cls, url):
        cls._curl = url
        return cls._curl
        
    def available_models(self):
        try:
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_source_id_',self._fdata))
                print("\nCurrently ", self._avail," models has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_source_id_')[zz+2].split('" name="')[0])
                print("Available models: \n\n")
                return self._holder
        except:
            self._Curl=_choose_server()
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_source_id_',self._fdata))
                print("\nCurrently ", self._avail," models has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_source_id_')[zz+2].split('" name="')[0])
                print("Available models: \n\n")
                return self._holder
    
    def all_models(self):
        with _fetch_url(self._set_curl(self._Turl)) as self._fdata:
            self._total = len(re.findall('<tr><td>',self._fdata))
            print("\nCMIP6 has ", self._total," models in total!\n")
            for zz in range(self._total):
                self._holder.append(self._fdata.split('<tr><td>')[zz+1].split('</td>\\n')[0])
            print("List of all CMIP6 models: \n\n")
            return self._holder
            
    def available_experiments(self):
        try:
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_experiment_id_',self._fdata))
                print("\nCurrently ", self._avail," experiments has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_experiment_id_')[zz+2].split('" name="')[0])
                print("Available experiments: \n\n")
                return self._holder
        except:
            self._Curl=_choose_server()
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_experiment_id_',self._fdata))
                print("\nCurrently ", self._avail," experiments has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_experiment_id_')[zz+2].split('" name="')[0])
                print("Available experiments: \n\n")
                return self._holder
    
    def all_experiments(self):
        with _fetch_url(self._set_curl(self._ETurl)) as self._fdata:
            self._total = len(re.findall('<tr><td>',self._fdata))
            print("\nCMIP6 has ", self._total," experiments in total!\n")
            for zz in range(self._total):
                self._holder.append(self._fdata.split('<tr><td>')[zz+1].split('</td>\\n')[0])
            print("List of all CMIP6 experiments: \n\n")
            return self._holder
            
    def CMIP6_variables(self):
        try:
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_variable_id_',self._fdata))
                print("\nCurrently ", self._avail," variables has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_variable_id_')[zz+2].split('" name="')[0])
                print("Available variables: \n\n")
                return self._holder
        except:
            self._Curl=_choose_server()
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_variable_id_',self._fdata))
                print("\nCurrently ", self._avail," variables has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_variable_id_')[zz+2].split('" name="')[0])
                print("Available variables: \n\n")
                return self._holder
        
    def available_frequencies(self):
        try:
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_frequency_',self._fdata))
                print("\nCurrently ", self._avail," frequencies has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_frequency_')[zz+2].split('" name="')[0])
                print("Available frequencies: \n\n")
                return self._holder
        except:
            self._Curl=_choose_server()
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_frequency_',self._fdata))
                print("\nCurrently ", self._avail," frequencies has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_frequency_')[zz+2].split('" name="')[0])
                print("Available frequencies: \n\n")
                return self._holder
        
    def available_realmns(self):
        try:
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_realm_',self._fdata))
                print("\nCurrently ", self._avail," realms has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_realm_')[zz+2].split('" name="')[0])
                print("Available realms: \n\n")
                return self._holder
        except:
            self._Curl=_choose_server()
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_realm_',self._fdata))
                print("\nCurrently ", self._avail," realms has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_realm_')[zz+2].split('" name="')[0])
                print("Available frequencies: \n\n")
                return self._holder
            
    def var_stdName(self):
        try:
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_cf_standard_name_',self._fdata))
                print("\nCurrently ", self._avail," variables has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_cf_standard_name_')[zz+2].split('" name="')[0])
                print("Available variables: \n\n")
                return self._holder
        except:
            self._Curl=_choose_server()
            with _fetch_url(self._set_curl(self._Curl)) as self._fdata:
                self._avail = len(re.findall('id="checkbox_cf_standard_name_',self._fdata))
                print("\nCurrently ", self._avail," variables has outputs!\n")
                for zz in range(self._avail):
                    self._holder.append(self._fdata.split('checkbox_cf_standard_name_')[zz+2].split('" name="')[0])
                print("Available frequencies: \n\n")
                return self._holder
    
    @staticmethod
    def _get_definition(exp):
        resource_package = __name__
        resource_path = '/'.join(('data', 'CMIP6_exps.xlsx'))
        tmp = pkg_resources.resource_stream(resource_package, resource_path)
        did=pd.read_excel(tmp)
        exp_name=pd.DataFrame(did,columns=['canonical_name'])
        exp_def=pd.DataFrame(did,columns=['description'])
        for zz in range(len(exp_name.values)):
            if (exp_name.values[zz]==exp):
                definition=(exp_def.values[zz][0]).split('\n')[0].strip()
        return definition
    
    @staticmethod
    def _get_longName(var):
        resource_package = __name__
        resource_path = '/'.join(('data', 'var_list.xlsx'))
        tmp = pkg_resources.resource_stream(resource_package, resource_path)
        did=pd.read_excel(tmp)
        v=pd.DataFrame(did,columns=['variable'])
        v_long=pd.DataFrame(did,columns=['Long_name'])
        for zz in range(len(v.values)):
            if (v.values[zz]==var):
                longName=v_long.values[zz][0]
        return longName
            