#!/usr/bin/env python3
 
import os
import subprocess
 
def dask_setup(service):
    # Start Jupyter, adjust to your paths and environment.
    # As a reminder, subprocess.Popen works like this ["/path/to/executable", "--arg", "value", "--keywordarg=keywordvalue"]
    #os.environ["JUPYTER_ALLOW_INSECURE_WRITES"] = "true"
    proc = subprocess.Popen(["/opt/conda/bin/jupyter lab", "--config=/opt/conda/etc/jupyter/jupyter_notebook_config.py"])
    service.jlab_proc = proc

def dask_teardown(service):
    try:
        proc = service.jlab_proc
        proc.terminate()
    except Exception:
        pass
