# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:58:23 2019

@author: Taufiq
"""

from acccmip6.utilities.c6db import SearchDB
from acccmip6.utilities.CMIP6_database import CMIP6DB
from acccmip6.utilities.util import color, _mod_help

def SearchCmip6(**kwargs):
        _var = kwargs.get('variable', None)
        _mod = kwargs.get('model', None)
        _exp = kwargs.get('experiment', None)
        _freq = kwargs.get('frequency', None)
        _realm = kwargs.get('realm', None)
        _check = kwargs.get('check', None)
        _desc = kwargs.get('desc', None)
        _time = kwargs.get('time', None)
        year = kwargs.get('year', None)
        module = kwargs.get('module', None)
        
        if (module == 'on'):
            _mod_help()
            if (_var == 'show') or (_var == 'Show'):
                ModDB = CMIP6DB()
                print(ModDB.var_stdName())
            if (_mod == 'show') or (_mod == 'Show'):
                ModDB = CMIP6DB()
                print(ModDB.available_models())
            if (_exp == 'show') or (_exp == 'Show'):
                ModDB = CMIP6DB()
                print(ModDB.available_experiments())
            if (_freq == 'show') or (_freq == 'Show'):
                ModDB = CMIP6DB()
                print(ModDB.available_frequencies())
            if (_realm == 'show') or (_realm == 'Show'):
                ModDB = CMIP6DB()
                print(ModDB.available_realmns())
            raise SystemExit
    

        search=SearchDB()
        if (_check == 'Yes') or (_check == 'yes'):
            print('\n'+color.UNDERLINE+color.BOLD+'TIPS:'+color.END+" If you are not sure about what you are looking for use CMIP6DB module \n      to look for currently available models/experiments/variables and so on . . ."+color.END)
            search._set_check('Yes')
        else:
            print('\n'+color.UNDERLINE+color.BOLD+'TIPS:'+color.END+" Use the check (-c) argument to check your inputs."+color.END)
            search._set_check('No')
        if (_mod != None):
            try:
                search.model=_mod
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_mod)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_exp != None):
            try:
                search.experiment=_exp
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_exp)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_var != None):
            try:
                search.variable=_var
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_var)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_freq != None):
            try:
                search.frequency=_freq
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_freq)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_realm != None):
            try:
                search.realm=_realm
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_realm)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
                
        if (year != None):
            try:
                search.year=year
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(year)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        
        info = search.get_info()

        if (year!=None):
            all_links = search.get_links(0)
            links=[]
            if int(year)>0:
                end_year = int(info.year[0])+int(year)
            else:
                end_year = int(info.year[len(info.year)-1])+int(year)
            interested_years=[]
            for y in info.year:
                if (int(year)>0) and (int(y)-1<end_year):
                    interested_years.append(y)
                elif (int(year)<0) and (end_year<int(y)+1):
                    interested_years.append(y)
                else:
                    continue
            for item in interested_years:
                for link in all_links:
                    if '_'+item in link:
                        links.append(link)
            search.links = links
            info = search.get_info()
        
        print(color.LGREEN+"\n\n Currently available models based on your search: \n\n"+color.END,info.mod)
        print(color.LGREEN+"\nCurrently available variables based on your search: \n\n"+color.END,info.var)
        print(color.LGREEN+"\nCurrently available experiments based on your search: \n\n"+color.END,info.exp,"\n\n")
        print(color.LGREEN+"\nNumber of files:"+color.END, info.n_files,"\n\n")
        print(color.LGREEN+"\nAvailable realizations:"+color.END, info.rlzn,"\n\n")
        if (_time != None):
            print(color.YELLOW+"< < < Data available for these time periods > > >\033[0m \n")
            print(info.year)
        if (_desc != None):
            print(color.YELLOW+"< < < Here are the experiment descriptions > > >\033[0m")
            for item in info.exp:
                print("\n\n"+color.CYAN+str(item)+":\033[0m \n"+CMIP6DB._get_definition(item))
        print(color.RED+"\n\n       <===============Exiting now!================>\033[0m\n\n")
        raise SystemExit