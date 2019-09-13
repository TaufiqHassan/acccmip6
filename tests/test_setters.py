# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 04:25:50 2019

@author: Taufiq
"""

from acccmip6.utilities.c6db import SearchDB

def setup_module(module):
    global d
    d = SearchDB()
    
def test_model_setters():
    d.model = 'model1, model2, model3, modelN'
    assert d._mod == ['model1', 'model2', 'model3', 'modelN']
    
def test_exp_setters():
    d.experiment = 'exp1, exp2, exp3, expN'
    assert d._exp == ['exp1', 'exp2', 'exp3', 'expN']
    
def test_var_setters():
    d.variable = 'var1, var2, var3, varN'
    assert d._var == ['var1', 'var2', 'var3', 'varN']
    
def test_freq_setters():
    d.frequency = 'freq1, freq2, freq3, freq4'
    assert d._freq == ['freq1', 'freq2', 'freq3', 'freq4']