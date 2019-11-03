# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:25:01 2019

@author: Taufiq
"""

from acccmip6.utilities.CMIP6_database import CMIP6DB
from acccmip6.utilities.util import HidePrint, color

class _checkers(object):
    
    def __init__(self, val):
        self.val = val
    
    def _check_model(self):
        print("\nChecking for", self.val,"model in CMIP6 database . . .")
        with HidePrint():
            models_av = CMIP6DB().available_models()
        if self.val not in models_av:
            n=0
            m_u=[x.upper() for x in models_av]
            print('\nCannot find model.\nLooking for other options . . .')
            for s in m_u:
                if self.val.upper() in s:
                    n=n+1
                    s = models_av[m_u.index(s)]
                    print('\nOption ', n, s)
            if (n==0):
                raise ValueError()
            else:
                raise Exception()
        else:
            print(color.LBLUE+'Found:'+color.END,self.val,'model.')
            return self.val
        
    def _check_exp(self):
        print("\nChecking for", self.val,"experiment in CMIP6 database . . .")
        with HidePrint():
            exp_av = CMIP6DB().available_experiments()
        if self.val not in exp_av:
            n=0
            m_u=[x.upper() for x in exp_av]
            print('\nCannot find experiment.\nLooking for other options . . .')
            for s in m_u:
                if self.val.upper() in s:
                    n=n+1
                    s = exp_av[m_u.index(s)]
                    print('\nOption ', n, s)
            if (n==0):
                raise ValueError()
            else:
                raise Exception()
        else:
            print(color.LBLUE+'Found:'+color.END,self.val,'experiment.')
            return self.val
        
    def _check_var(self):
        print("\nChecking for", self.val,"variable in CMIP6 database . . .")
        with HidePrint():
            var_av = CMIP6DB().CMIP6_variables()
        if self.val not in var_av:
            n=0
            m_u=[x.upper() for x in var_av]
            print('\nCannot find variable.\nLooking for other options . . .')
            for s in m_u:
                if self.val.upper() in s:
                    n=n+1
                    s = var_av[m_u.index(s)]
                    LN = CMIP6DB()._get_longName(str(s))
                    print('\nOption ', n, s,'(',LN,')')
            if (n==0):
                raise ValueError()
            else:
                raise Exception()
        else:
            print(color.LBLUE+'Found:'+color.END,self.val,'variable.')
            return self.val
        
    def _check_realm(self):
        print("\nChecking for", self.val,"realm in CMIP6 database . . .")
        with HidePrint():
            realm_av = CMIP6DB().available_realmns()
        if self.val not in realm_av:
            n=0
            m_u=[x.upper() for x in realm_av]
            print('\nCannot find realm.\nLooking for other options . . .')
            for s in m_u:
                if self.val.upper() in s:
                    n=n+1
                    s = realm_av[m_u.index(s)]
                    print('\nOption ', n, s)
            if (n==0):
                raise ValueError()
            else:
                raise Exception()
        else:
            print(color.LBLUE+'Found:'+color.END,self.val,'realm.')
            return self.val
        
    def _check_freq(self):
        print("\nChecking for", self.val,"frequency in CMIP6 database . . .")
        with HidePrint():
            freq_av = CMIP6DB().available_frequencies()
        if self.val not in freq_av:
            n=0
            m_u=[x.upper() for x in freq_av]
            print('\nCannot find frequency.\nLooking for other options . . .')
            for s in m_u:
                if self.val.upper() in s:
                    n=n+1
                    s = freq_av[m_u.index(s)]
                    print('\nOption ', n, s)
            if (n==0):
                raise ValueError()
            else:
                raise Exception()
        else:
            print(color.LBLUE+'Found:'+color.END,self.val,'frequency.')
            return self.val