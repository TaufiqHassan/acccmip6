#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_accmip6
----------------------------------

Tests for `accmip6` module.
"""
import pytest
from pathlib import Path

from acccmip6.utilities.c6db import SearchDB
from acccmip6.utilities.util import _dir_path, _Construct_urls
    
def test_url_getter():
    d = SearchDB()
    d.variable = 'var1, var2, var3, varN'
    url = d.get_url()
    durl=_Construct_urls(['var1', 'var2', 'var3', 'varN'],None,None,None,None)._Durl
    assert url == durl+"&variable=var1&variable=var2&variable=var3&variable=varN&limit=10000"
        
def test_dir_path():
    d = _dir_path()
    p=Path('.')
    assert d._get_dir('') == p.absolute() / 'CMIP6'
    
