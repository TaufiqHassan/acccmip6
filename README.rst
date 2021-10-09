===============================
Access Cmip6
===============================

.. image:: https://img.shields.io/travis/TaufiqHassan/acccmip6.svg
        :target: https://travis-ci.org/TaufiqHassan/acccmip6

.. image:: https://img.shields.io/pypi/v/acccmip6.svg
        :target: https://pypi.python.org/pypi/acccmip6

.. image:: https://readthedocs.org/projects/acccmip6/badge
        :target: https://acccmip6.readthedocs.org
        
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3723878.svg
   :target: https://doi.org/10.5281/zenodo.3723878


``acccmip6`` package can access CMIP6 database in real-time.
``acccmip6`` 包可以实时访问CMIP6数据集.

* GitHub repo: https://github.com/TaufiqHassan/acccmip6
* Documentation: https://acccmip6.readthedocs.org.

Features 功能
--------

- Real-time search and download from continuously updating CMIP6 database
	实时搜索下载持续更新的CMIP6数据
- Find data for any specific items (e.g. model, experiment, variable, frequency, realm)
	通过用户指定的选项（如model, experiment, variable, frequency, realm）获取数据
- Search and download any combination of the above items
	根据上述选项的任意组合搜索下载数据
- Find the total number of available files and realizations
	确定可获得的文件和文件组（有的试验数据是分为多个文件储存的）的总数量
- Validate your search items
	检验你的搜索选项
- Get suggestions if necessary
	必要时提供建议
- Access definition of the experiments
	获取试验的定义
- Skips already existing files

Installation 安装
------------

Install is as simple as typing -
安装只需要输入-
``pip install acccmip6``

Requires python v3.5 or up and pip. Mac users can use ``brew install python3`` and ``python get-pip.py`` from terminal. Windows users can use `Windows Subsystem`_.

.. _`Windows Subsystem`: https://docs.microsoft.com/en-us/windows/wsl/install-win10

需要python3.5以上环境和pip。Mac用户在终端可以使用``brew install python3`` 和 ``python get-pip.py``。Windows用户可以使用子系统`Windows Subsystem`_.

.. _`Windows Subsystem`: https://docs.microsoft.com/en-us/windows/wsl/install-win10

Installation demo

.. image:: docs/installation_demo.gif

You may also install the package via conda - 

``conda install -c thassan acccmip6``

Usage
-----

``acccmip6`` searches the live CMIP6 database and spits out currently available models, experiments and variables that satisfies your search criteria. It will also output the number of available files. 
``acccmip6`` also tries to be a good command-line interface (CLI). Run ``acccmip6 -h`` to see a help message with all the arguments you can pass.

Required Arguments
------------------

- ``-o`` : Takes output type. 'S' for searching the database or 'D' for downloading from the database.

Optional Arguments
------------------

- ``-m`` : Model names (multiple comma separated names are allowed)
- ``-e`` : Experiment names
- ``-f`` : CMIP6 output frequency (e.g. mon, day etc.)
- ``-v`` : Variable names
- ``-r`` : Realm name (e.g. atmos, ocean etc.)
- ``-rlzn`` : Select a specified realization
- ``-c`` : 'yes' to use checker when searching or downloading. This helps to find out whether the search items are currently available. If not, it will produce suggestions that matches closely to your search.
- ``-desc`` : 'yes' to get the description of the experiments searched for
- ``-dir`` : Download directory
- ``-skip`` : Skip any item (model/experiment/realizations) from your download
- ``-time`` : 'yes' to print out all available time periods
- ``-yr`` : Select data for a time period (number of years)

Demo
-----

Search CMIP6 database with ``acccmip6 -o S``

.. image:: docs/searching_demo.gif

Download CMIP6 data with ``acccmip6 -o D``

.. image:: docs/downloading_demo.gif

License
-------

This code is licensed under the `MIT License`_.

.. _`MIT License`: https://opensource.org/licenses/MIT
