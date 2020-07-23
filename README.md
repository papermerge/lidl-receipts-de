Lidl Receipts (Germany) 
=======================

![Lidl Receipt](./img/lidl-receipt.png)

Papermerge metadata plugin for lidl receipts  used in Germany.

This plugin returns 3 metadata labels/keys named as follows:

* shop
* price
* date

On the main app you need to keep in mind that:

* shop - has free text format
* price - is of type money (as per main app), with
    format "dd,cc". Example: 38,95
* date - is of type date (as per main app), with
    format "dd.mm.yy". Example: 21.12.19 - 21st of December 2019

## Installation

    pip install papermerge-meta-plugin-lidl-receipts-de

Notice that for configuration you will use plugin name WITHOUT prefix (i.e.
without papermerge-meta-plugin- part).
Also, for importing this module you need to use name WITHOUT prefix:

    import lidl_receipts_de

Usually you don't need to import plugin directly, main app does it for you.

In papermerge.conf add "lidl_receipts_de.Lidl" entry to METADATA_PLUGINS:

    METADATA_PLUGINS = [
        "lidl_receipts_de.Lidl", ...
    ]

In case you want to map returned metadata to differently named keys:


    METADATA_PLUGIN_MAPS = {
        "lidl_receipts_de.Lidl": {
            "shop": "Firma",
            "price": "Betrag",
            "date": "Datum",
        },
    }



## Prepare Development Environment & Run Tests
    
1. virtualenv .venv -p /usr/bin/python3.8  # provide virtualenv path to 3.8 interpreter
2. source .venv/bin/activate  # activate .venv virtual environment
3. pip install -r requirements.txt # install dependencies
4. python setup.py develop  # provide a link to dev version of hocron
5. python test/run.py

