a2pcej
======
[![Code Climate](https://codeclimate.com/github/kacchan822/a2pcej/badges/gpa.svg)](https://codeclimate.com/github/kacchan822/a2pcej)
[![Issue Count](https://codeclimate.com/github/kacchan822/a2pcej/badges/issue_count.svg)](https://codeclimate.com/github/kacchan822/a2pcej)
[![Coverage Status](https://coveralls.io/repos/github/kacchan822/a2pcej/badge.svg?branch=master)](https://coveralls.io/github/kacchan822/a2pcej?branch=master)


__a2pcej__, convert Alphabet to Phonetic Code in English and Japanease.

This module convert each alphabet letters to phonetic code,
and also convert each alphabet letterts to katakana.


### Functions
#### conv_al(letters, delimiter='-', upper_sign='(CAPS)', num=False)
letters is string.

```python
def conv_al(letters, delimiter='-', sign='(CAPS)', num=False):
    return <unicode>
```
#### conv_ak(letters, delimiter='・', upper_sign='（大文字）', num=False)
letters is string.
```python
def conv_ak(letters, delimiter='・', sign='（大文字）', num=False):
    return <unicode>
```

### Simple example of usage as below... (on Python3.5)
First of all, import module.
```python
Import module.
>>> from a2pcej import *
```
Convert 'examples' to Ponetic code in English.
```python
>>> conv_al('examples')
'Echo-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra'
```

Convert 'examples' to Ponetic code in Japanese Katakana.
```python
>>> conv_ak('examples')
'イー・エクス・エイ・エム・ピー・エル・イー・エス'
```

Non alphabet letters are not convert (default).  
Upper case lattters has (CAPS) or (大文字) sign (default).
```python
>>> conv_al('Examples002')
'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-0-0-2'
>>> conv_ak('Examples002')
'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・0・0・2'
```

You can change delimiter and Upper case letters sign.
```python
>>> conv_al('Examples003', delimiter=', ', sign='(CAPITAL)')
'Echo(CAPITAL), Xray, Alfa, Mike, Papa, Lima, Echo, Sierra, 0, 0, 3'
>>> conv_ak('Examples003', delimiter='／', sign='(大)')
'イー(大)／エクス／エイ／エム／ピー／エル／イー／エス／0／0／3'
```

If you would like to convert numbers to phonetic code, set `num=True`.
```python
>>> conv_al('Examples004', num=True)
'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-zero-zero-four'
>>> conv_ak('Examples004', num=True)
'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・ゼロ・ゼロ・ヨン'
```
