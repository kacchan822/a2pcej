a2pcej
======

|Code Climate| |Issue Count| |Coveralls|

**a2pcej**, convert Alphabet to Phonetic Code in English and Japanease.

This module convert each alphabet letters to phonetic code, and also
convert each alphabet letterts to katakana.

Functions
~~~~~~~~~

conv\_al(letters, delimiter='-', upper\_sign='(CAPS)', num=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

letters is string.

.. code:: python

    def conv_al(letters, delimiter='-', sign='(CAPS)', num=False):
        return <unicode>

conv\_ak(letters, delimiter='・', upper\_sign='（大文字）', num=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

letters is string.

.. code:: python

    def conv_ak(letters, delimiter='・', sign='（大文字）', num=False):
        return <unicode>

Simple example of usage as below... (on Python3.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, import module.

.. code:: python

    Import module.
    >>> from a2pcej import *

Convert 'exsamples' to Ponetic code in English.

.. code:: python

    >>> conv_al('examples')
    'Echo-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra'

Convert 'exsamples' to Ponetic code in Japanese Katakana.

.. code:: python

    >>> conv_ak('examples')
    'イー・エクス・エイ・エム・ピー・エル・イー・エス'

| Non alphabet letters are not convert (default).
| Upper case lattters has (CAPS) or (大文字) sign (default).

.. code:: python

    >>> conv_al('Examples002')
    'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-0-0-2'
    >>> conv_ak('Examples002')
    'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・0・0・2'

You can change delimiter and Upper case letters sign.

.. code:: python

    >>> conv_al('Examples003', delimiter=', ', sign='(CAPITAL)')
    'Echo(CAPITAL), Xray, Alfa, Mike, Papa, Lima, Echo, Sierra, 0, 0, 3,'
    >>> conv_ak('Examples003', delimiter='／', sign='(大)')
    'イー(大)／エクス／エイ／エム／ピー／エル／イー／エス／0／0／3'

If you would like to convert numbers to phonetic code, set ``num=True``.

.. code:: python

    >>> conv_al('Examples004', num=True)
    'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-zero-zero-four'
    >>> conv_ak('Examples004', num=True)
    'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・ゼロ・ゼロ・ヨン'

.. |Code Climate| image:: https://codeclimate.com/github/kacchan822/a2pcej/badges/gpa.svg
   :target: https://codeclimate.com/github/kacchan822/a2pcej
.. |Issue Count| image:: https://codeclimate.com/github/kacchan822/a2pcej/badges/issue_count.svg
   :target: https://codeclimate.com/github/kacchan822/a2pcej
.. |Coveralls| image:: https://coveralls.io/repos/github/kacchan822/a2pcej/badge.svg?branch=master
   :target: https://coveralls.io/github/kacchan822/a2pcej?branch=master
