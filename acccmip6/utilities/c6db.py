# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:16:28 2019

@author: Taufiq
"""

from acccmip6.utilities.util import _extract_info, _Construct_urls
from acccmip6.utilities.checkers import _checkers

class SearchDB(object):

    _check = 'No'
    
    def __init__(self, **kwargs):
        self._var = kwargs.get('variable', None)
        self._mod = kwargs.get('model', None)
        self._exp = kwargs.get('experiment', None)
        self._freq = kwargs.get('frequency', None)
        self._realm = kwargs.get('realm', None)
        self.n_files = kwargs.get('n_files', None)
        self.rlzn = kwargs.get('rlzn', None)
        self.year = kwargs.get('year', None)
        self.links = kwargs.get('links', None)

    @classmethod
    def _set_check(cls, val):
        cls._check = val
        return cls._check

    @property
    def model(self):
        return self._mod

    @model.setter
    def model(self, val):
        self._mod=[0]
        mods = [x.strip() for x in val.split(',')]
        for zz in range(len(mods)):
            if (self._check == 'Yes'):
                self._mod.append(_checkers(mods[zz])._check_model())
            else:
                self._mod.append(mods[zz])
        self._mod.remove(0)

    @property
    def experiment(self):
        return self._exp

    @experiment.setter
    def experiment(self, val):
        self._exp = [0]
        exps = [x.strip() for x in val.split(',')]
        for zz in range(len(exps)):
            if (self._check == 'Yes'):
                self._exp.append(_checkers(exps[zz])._check_exp())
            else:
                self._exp.append(exps[zz])
        self._exp.remove(0)
            
    @property
    def variable(self):
        return self._var

    @variable.setter
    def variable(self, val):
        self._var = [0]
        vars = [x.strip() for x in val.split(',')]
        for zz in range(len(vars)):
            if (self._check == 'Yes'):
                self._var.append(_checkers(vars[zz])._check_var())
            else:
                self._var.append(vars[zz])
        self._var.remove(0)
            
    @property
    def realm(self):
        return self._realm

    @realm.setter
    def realm(self, val):
        self._realm = [0]
        realms = [x.strip() for x in val.split(',')]
        for zz in range(len(realms)):
            if (self._check == 'Yes'):
                self._realm.append(_checkers(realms[zz])._check_realm())
            else:
                self._realm.append(realms[zz])
        self._realm.remove(0)
            
    @property
    def frequency(self):
        return self._freq

    @frequency.setter
    def frequency(self, val):
        self._freq = [0]
        freqs = [x.strip() for x in val.split(',')]
        for zz in range(len(freqs)):
            if (self._check == 'Yes'):
                self._freq.append(_checkers(freqs[zz])._check_freq())
            else:
                self._freq.append(freqs[zz])
        self._freq.remove(0)
        
    @property
    def realization(self):
        return self.rlzn

    @realization.setter
    def realization(self, val):
        self.rlzn = [0]
        rlzns = [x.strip() for x in val.split(',')]
        for zz in range(len(rlzns)):
            self.rlzn.append(rlzns[zz])
        self.rlzn.remove(0)
        
    @property
    def years(self):
        return self.year

    @years.setter
    def years(self, val):
        self.year = [0]
        year = [x.strip() for x in val.split(',')]
        for zz in range(len(year)):
            self.year.append(year[zz])
        self.year.remove(0)
    
    
    def get_links(self, manual):
        if manual==0:
            links = _Construct_urls(self._var, self._mod, self._realm, self._exp, self._freq)._get_wget(0)
        else:
            links = _Construct_urls(self._var, self._mod, self._realm, self._exp, self._freq)._get_wget(1)
        return links
    
    def get_info(self):
        info = _extract_info(self._var, self._mod, self._realm, self._exp, self._freq, self.n_files, self.rlzn, self.year,self.links)._get_info()
        return info
    
    def get_url(self):
        url = _Construct_urls(self._var, self._mod, self._realm, self._exp, self._freq)._get_url()
        return url
    