Q & A
======

**What is the recommended use for the package?**

- Be more specific in your search for better result. Try to include -v, -m, -e, -f options in your search.

- If the user is interested to download 30 models, for 4 different variables, with 5 different experiments; it is suggested to chunk them out into...let's say, 30 models for 1 variable, and 1 experiment. 

- Users can always run a separate chunk (for a different variable/experiment) on different terminal tabs (maximum 4 connections are allowed through ESGF).

**Can I use a bash/loop script to automate the process?**

- Yes! This is why the CLI system works really well.

A simple bash script may look like this ::

        #!/bin/bash


        for i in CNRM-ESM2-1 HadGEM3-GC31-LL CESM2 GFDL-ESM4 INM-CM5-0 CESM2-WACCM-FV2 BCC-ESM1 INM-CM4-8 MRI-ESM2-0 NorESM2-LM NorESM2-MM GFDL-CM4 MIROC-ES2L MIROC

        do
                acccmip6 -o D -v mmrso4,mmrbc,mmroa,mmrdust,mmrss,mmrpm2p5 -f mon -e piControl -m $i -yr 50 -dir /download_dir/
        done

**What can I do when my download is stuck or slow?**

- The package has a built-in method that would skip to the next file if the current download speed is below 0.08 MB/s or the download is stuck (no response from the server) for more than 5 minutes. 
  
- Impatient users can use ``cntl+c`` to end the process and re-run the same command. It will skip over the already downloaded files.

- If there's one model or variable that is giving you a hard time, you can always skip that item using the ``-skip`` argument.

Download stuck or slow ::

        vas_Amon_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001-201412.nc is available!

        Downloading  5% |██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 10/195MB 0.08 MB/s
        download too slow! retrying...
        Removing file . . .

**During download, some files were skipped because of slow downloading speed. How can I retrieve those files?**

- You will get a message about how many files were downloaded (e.g. n out of m files). You can download those (m-n) files just by re-running the command.

**Is it possible to select a specific variant label? For instance, can I select only 'r1i1p1f1' out of 'r1i1p1f1', 'r1i1p1f2' and 'r1i1p2f1'?**

- Yes, the package is designed to download all available realizations with -rlzn option regardless of the variant. If you do not want to download a certain variant you can always use the 'skip' option.

- For instance, if you do not want the latter 2 variants in the example question, add ``-skip 1p2,1f2`` in your command line. 
 
- This is also usable for any other cases, such as, choosing the grid option. For instance, using ``-skip _gr_`` will only download available ``gn`` (native grid) data.

**Can I download or search data within a specific time period?** 

- Yes, using the ``-yr`` option. Checkout the extra arguments.

**Some files are not downloading after showing a 401 Unauthorized error! How can I download those files?**

- This is a common server issue found in CMIPs. ``acccmip6`` produces an error and skips over these files by producing ::

    <<401 Unauthorized: restricted access!!>>

    From ESGF: Before you can download this data, you have to join a data access control group 
    since acknowledgement of a policy is a condition for this data download.

    Requires registration/manual download . . . :(

- It stores all unresolved files to a wget script in the same download directory once the download finishes. 

- You can then use that script with your openid and password with -H option (e.g. ``./wget_script -H``).