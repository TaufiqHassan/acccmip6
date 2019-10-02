Q & A
======

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
