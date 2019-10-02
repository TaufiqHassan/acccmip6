===============================
Access Cmip6
===============================

.. image:: https://img.shields.io/travis/TaufiqHassan/acccmip6.svg
        :target: https://travis-ci.org/TaufiqHassan/acccmip6

.. image:: https://img.shields.io/pypi/v/acccmip6.svg
        :target: https://pypi.python.org/pypi/acccmip6

.. image:: https://readthedocs.org/projects/acccmip6/badge
        :target: https://acccmip6.readthedocs.org


``acccmip6`` package can access CMIP6 database in real-time.

* GitHub repo: https://github.com/TaufiqHassan/acccmip6
* Documentation: https://acccmip6.readthedocs.org.

Features
--------

- Real-time search and download from continuously updating CMIP6 database
- Find data for any specific items (e.g. model, experiment, variable, frequency, realm)
- Search and download any combination of the above items
- Find the total number of available files and realizations
- Validate your search items
- Get suggestions if necessary
- Access definition of the experiments
- Skips already existing files

Installation
------------

Install is as simple as typing -

``pip install acccmip6``

Requires python v3.5 or up and pip. Mac users can use ``brew install python3`` and ``python get-pip.py`` from terminal. Windows users can use `Windows Subsystem`_.

.. _`Windows Subsystem`: https://docs.microsoft.com/en-us/windows/wsl/install-win10

Installation demo

.. image:: docs/installation_demo.gif


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
