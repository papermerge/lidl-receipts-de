Lidl Receipts (Germany) 
=======================

Papermerge metadata plugin for lidl receipts  used in Germany

## Installation

    pip install lidl-receipts-de

In papermerge.conf add "lidl_receipts_de" entry to PAPERMERGE_METADATA_PLUGINS:

    PAPERMERGE_METADATA_PLUGINS=["lidl_receipts_de", ...]


## Prepare Development Environment & Run Tests
    
    1. virtualenv .venv -p /usr/bin/python3.8  # provide virtualenv path to 3.8 interpreter
    2. source .venv/bin/activate  # activate .venv virtual environment
    3. pip install -r requirements.txt # install dependencies
    4. python setup.py develop  # provide a link to dev version of hocron
    5. python test/run.py

