.. acccmip6 documentation master file, created by
   sphinx-quickstart on Sat Sep 21 15:52:39 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

acccmip6 documentation
======================

acccmip6 allows user to access the 6th Coupled Model Intercomparison Project (`CMIP6`_) database in real-time. CMIP6 is still updating its database (as of Sep. 2019) and new data for different Tier experiments are still to come. It's a hassle to go through their servers and put search terms manually everytime to find out whether your desired data is uploaded yet or not! Instead, use ``acccmip6``, to get what you need in seconds. This is written in python and does not require any python programming experience. It outputs what models, experiments, variables and realizations are currently available.

Features
--------

- Real-time search and download from continuously updating CMIP6 database
- Find data for any specific items (e.g. model, experiment, variable, frequency, realm)
- Search and download any combination of the above items
- Monitor each download process
- Find the total number of available files and realizations
- Accepts inputs in multiple formats including lists
- Validate your search items
- Get suggestions if necessary
- Access definition of the experiments
- Supports python 3.5 and above
- Skips already existing files

Useful links
------------

- Source code is available on `GitHub`_.
- A `quickstart guide`_ is available with multiple demos.
- `Overview`_ of the CMIP6 experimental design and organization.


User guide
----------

.. toctree::
   :maxdepth: 2

   guide/quickstart
   guide/install
   guide/search
   guide/module_search
   guide/download
   guide/q_and_a.rst
   guide/authors.rst
   guide/license


.. _`CMIP6`: https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6
.. _`GitHub`: https://github.com/TaufiqHassan/acccmip6
.. _`quickstart guide`: https://github.com/TaufiqHassan/acccmip6/blob/master/README.rst
.. _`Overview`: https://www.geosci-model-dev.net/9/1937/2016/gmd-9-1937-2016.html

