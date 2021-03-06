# Data Exploration with Matplotlib and D3.js

[![Build Status](https://travis-ci.org/epigos/data-explorer.png)](https://travis-ci.org/epigos/data-explorer)
[![PyPI version](https://badge.fury.io/py/dexplorer.svg)](https://badge.fury.io/py/dexplorer)

This is a small library built with Tornado, Matplotlib and Pandas to summarize and visualize any datasource in the browser.

Currently supports `Python 3.x`

Demo
------------

![Demo](dexplorer/static/img/demo.png)


Installation
------------

To install, simply:

    $ pip install dexplorer

Usage
-----

Starting Data Explorer:

    from dexplorer import DataExplorer

    dte = DataExplorer()
    dte.read_csv('example.csv')  #  connect csv data source
    dte.start()  #  starts a new server on port 9011 by default;

Basically this is how it works;

1. Data is loaded using the `Pandas` library
2. The server start with websocket support to the browser
3. Descriptive summary (Descriptive Statistics) of columns is generated and sent through the socket and rendered in the browser.
4. Distribution of values (`Boxplot` and `Barplot`) in each columns is then generated using `Matplotlib` and sent to the browser as `json`.
5. `D3.js` is then used to render the `json` plot in the browser


Documentation
-----------------

Documentation can be found [here]()


Running the Tests
-----------------

To run tests

    python -m tornado.testing tests.functests
