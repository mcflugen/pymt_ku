=======
pymt_ku
=======


.. image:: https://img.shields.io/badge/CSDMS-BMI-green.svg
        :target: https://github.com/csdms/pymt
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_ku-green.svg
        :target: https://anaconda.org/conda-forge/pymt_ku

.. image:: https://img.shields.io/travis/mcflugen/pymt_ku.svg
        :target: https://travis-ci.org/mcflugen/pymt_ku

.. image:: https://readthedocs.org/projects/pymt_ku/badge/?version=latest
        :target: https://pymt_ku.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT plugin for Ku


* Free software: MIT license
* Documentation: https://ku.readthedocs.io.


---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3.6
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

------------------
Installing pymt_ku
------------------

Once `pymt` is installed, the dependencies of `pymt_ku` can
be installed with:

.. code::

  conda install permamodel

To install `pymt_ku`,

.. code::

  conda install pymt_ku
