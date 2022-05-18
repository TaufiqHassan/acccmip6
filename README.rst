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

Features
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
	跳过已经存在的文件
	
Installation
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

也可以通过conda进行安装 - 

``conda install -c thassan acccmip6``

Usage
-----

``acccmip6`` searches the live CMIP6 database and spits out currently available models, experiments and variables that satisfies your search criteria. It will also output the number of available files. 
``acccmip6`` also tries to be a good command-line interface (CLI). Run ``acccmip6 -h`` to see a help message with all the arguments you can pass.

根据用户提供的模型、试验、变量等条件即时搜索CMIP6数据集。提供良好的命令行交互。可以查看所有参数的帮助信息。

Required Arguments
------------------

- ``-o`` : Takes output type. 'S' for searching the database or 'D' for downloading from the database.

- ``-o`` : 输出类型。 'S' 用于搜索。'D' 用于下载。

Optional Arguments
------------------

- ``-m`` : Model names (multiple comma separated names are allowed) 模型名
- ``-e`` : Experiment names 试验民
- ``-f`` : CMIP6 output frequency (e.g. mon, day etc.) CMIP6时间分辨率
- ``-v`` : Variable names 变量名
- ``-r`` : Realm name (e.g. atmos, ocean etc.) Realm名
- ``-rlzn`` : Select a specified realization 指定realization
- ``-c`` : 'yes' to use checker when searching or downloading. This helps to find out whether the search items are currently available. If not, it will produce suggestions that matches closely to your search.  'yes'检查搜索或下载的选项是否可用。如果不可用，提供尽可能接近的建议。
- ``-desc`` : 'yes' to get the description of the experiments searched for 'yes'获取试验描述
- ``-dir`` : Download directory 指定下载目录
- ``-skip`` : Skip any item (model/experiment/realizations) from your download 下载中跳过
- ``-time`` : 'yes' to print out all available time periods 'yes'显示可用的时间段
- ``-yr`` : Select data for a time period (number of years) 指定时间

Demo
-----

Search CMIP6 database with ``acccmip6 -o S``
使用 ``acccmip6 -o S``搜索CMIP6数据

.. image:: docs/searching_demo.gif

Download CMIP6 data with ``acccmip6 -o D``
使用 ``acccmip6 -o D``搜索CMIP6数据

.. image:: docs/downloading_demo.gif

License
-------

This code is licensed under the `MIT License`_.

.. _`MIT License`: https://opensource.org/licenses/MIT
