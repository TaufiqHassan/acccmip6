# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 21:05:20 2019

@author: Taufiq
"""
from __future__ import unicode_literals
import urllib.request
import os, sys
import time
from pathlib import Path

from acccmip6.utilities.util import color, _dir_path, TooSlowException, convertBToMb, _realizations
from acccmip6.utilities.util import _get_rlzn_links, _manual_wget, HidePrint, _get_skipped_links
from acccmip6.utilities.c6db import SearchDB


def dlControl(count, blockSize, totalSize):
    global startTime

    dLoaded = count*blockSize
    passedTime = time.time() - startTime
    tRate = convertBToMb(dLoaded) / passedTime
    csize = int(convertBToMb(dLoaded))
    tsize = int(convertBToMb(totalSize))

    barLength = 40
    progress = float(csize) / float(tsize)
    percent = (csize/tsize)*100
    block = int(round(barLength * progress))
    text2="\r%s %i%% |%s%s| %i/%iMB %.2f MB/s\r" % ("Downloading ", percent, "█"*block, "░"*(barLength-block), csize, tsize, tRate)
    sys.stdout.write(text2)
    sys.stdout.flush()

    if (tRate < 0.08) and (passedTime > 60):
        print ("\ndownload too slow! retrying...")
        time.sleep(2)
        raise TooSlowException

def dl_cmip6(durl, dir_path):
        
        if (not os.path.exists(dir_path / durl.split('/')[len(durl.split('/'))-1])):
            print("\n\n"+durl.split('/')[len(durl.split('/'))-1]+" is available!\n")
            urllib.request.urlretrieve(durl,durl.split('/')[len(durl.split('/'))-1],reporthook=dlControl)
        else:
            print("\n"+durl.split('/')[len(durl.split('/'))-1]+" already exists!\n")         
    

def DownloadCmip6(**kwargs):
    global startTime
    
    _var = kwargs.get('variable', None)
    _mod = kwargs.get('model', None)
    _exp = kwargs.get('experiment', None)
    _freq = kwargs.get('frequency', None)
    _realm = kwargs.get('realm', None)
    _check = kwargs.get('check', None)
    rlzn = kwargs.get('rlzn', None)
    year = kwargs.get('year', None)
    path = kwargs.get('path', None)
    skip = kwargs.get('skip', None)
    
    search=SearchDB()
    if (_check == 'Yes') or (_check == 'yes'):
        search._set_check('Yes')
    else:
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
    
    print("\nFinding server . . .")
    links = search.get_links(0)
    
    if (links == []):
        print('\n'+color.LRED+'<<Invalid search items!>>'+color.END)
        print('\n'+color.UNDERLINE+color.BOLD+'TIPS 1:'+color.END+' Use the check (-c) argument to check your inputs.'+color.END)
        print('\n'+color.UNDERLINE+color.BOLD+'TIPS 2:'+color.END+' Use CMIP6DB module to look for currently available '
              'models/experiments/variables and so on . . .')
        raise SystemExit
    
    
    if (year!=None):
        info = search.get_info()
        yr_links=[]
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
            for link in links:
                if '_'+item in link:
                    yr_links.append(link)
        links = yr_links
    
    if (skip!=None):
        links=_get_skipped_links(links,skip)
        
    if (rlzn != None):
        all_rlzn = _realizations(links)._all_realizations()
        new_links = _get_rlzn_links(rlzn,all_rlzn,links)
        unused_links=list(set(links)-set(new_links))
        links=new_links
    
    if (path == None):
        dir_path = _dir_path()._make_dir()
    else:
        dir_path = Path(path)
    
    if not os.path.isdir(dir_path):
        print('creating ', dir_path)
        os.makedirs(str(dir_path))
        
    os.chdir(dir_path) 
    n = 0
    m = 0
    manual = 0
    passed_urls=[]    
    for url in links:
        startTime = time.time()
        try:
            dl_cmip6(url, dir_path)
            n=n+1
            passed_urls.append(url)
        except TooSlowException:
            print("Removing file . . .\n")
            os.remove(url.split('/')[len(url.split('/'))-1])
            m=m+1
            startTime = time.time()
        except KeyboardInterrupt:
            print("\nInterrupted! Removing file . . .\n")
            os.remove(url.split('/')[len(url.split('/'))-1])
            break
        except urllib.error.HTTPError:
            m=m+1
            manual=manual+1
            print("\n"+color.RED+"<<401 Unauthorized: restricted access!!>>"+color.END+"\n")
            print(color.UNDERLINE+"From ESGF:"+color.END+" Before you can download this data, you have to join a data access control group \nsince acknowledgement of a policy is a condition for this data download.")
            print("\nRequires registration/manual download . . . :(")
            pass
        except:
            m=m+1
            os.remove(url.split('/')[len(url.split('/'))-1])
            pass
    print("\nFinished downloading.")
    print("\n\nDownloaded ",n," out of ",n+m," files.")
    if (m>0):
        print("\n\nRe-run the script for the missing files.")
    if (manual>0):
        print("\n\n",manual," files require an ESGF account/openID.")
        print("\nwget script created for these files!\nUse it with your openid/password >> 'wget_script -H'")
        with HidePrint():
            search.get_links(1)
        _manual_wget(passed_urls,unused_links)
