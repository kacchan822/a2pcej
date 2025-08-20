a2pcej
======
[![Code Climate](https://codeclimate.com/github/kacchan822/a2pcej/badges/gpa.svg)](https://codeclimate.com/github/kacchan822/a2pcej)
[![Issue Count](https://codeclimate.com/github/kacchan822/a2pcej/badges/issue_count.svg)](https://codeclimate.com/github/kacchan822/a2pcej)
[![Coverage Status](https://coveralls.io/repos/github/kacchan822/a2pcej/badge.svg?branch=master)](https://coveralls.io/github/kacchan822/a2pcej?branch=master)
[![Latest Version](https://img.shields.io/pypi/v/a2pcej.svg)](https://pypi.python.org/pypi/a2pcej)


__a2pcej__, convert Alphabet to Phonetic Code in English and Japanese.

This module convert each alphabet letters to phonetic code,
and also convert each alphabet letters to katakana.


### Functions
#### conv_al(letters, delimiter='-', upper_sign='(CAPS)', num=False)
letters is string.

```python
def conv_al(letters, delimiter='-', sign='(CAPS)', num=False):
    return str
```
#### conv_ak(letters, delimiter='・', upper_sign='（大文字）', num=False)
letters is string.
```python
def conv_ak(letters, delimiter='・', sign='（大文字）', num=False):
    return str
```

### Simple example of usage

First of all, import module.
```python
>>> from a2pcej import *
```
Convert 'examples' to Phonetic code in English.
```python
>>> conv_al('examples')
'Echo-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra'
```

Convert 'examples' to Phonetic code in Japanese Katakana.
```python
>>> conv_ak('examples')
'イー・エクス・エイ・エム・ピー・エル・イー・エス'
```

Non alphabet letters are not convert (default).  
Upper case letters has (CAPS) or (大文字) sign (default).
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

## Development and Release

### Setting up for development

```bash
# Clone the repository
git clone https://github.com/kacchan822/a2pcej.git
cd a2pcej

# Install in development mode
pip install -e .[dev]

# Run tests
pytest tests/ -v

# Format code
black .
isort .

# Lint code
flake8 .
```

### Release Process

This project uses automated releases via GitHub Actions. To create a new release:

1. Update the version information and commit your changes
2. Create and push a tag:
   ```bash
   git tag v1.0.0  # Replace with your version
   git push origin v1.0.0
   ```
3. GitHub Actions will automatically:
   - Run tests across multiple Python versions
   - Build the package
   - Publish to PyPI

### GitHub Actions Setup

To enable automatic PyPI publishing, you need to set up authentication:

#### Option 1: PyPI API Token (Traditional)
1. Create an API token on PyPI
2. Add it as `PYPI_API_TOKEN` in GitHub repository secrets

#### Option 2: Trusted Publishing (Recommended)
1. Configure Trusted Publishing on PyPI for this repository
2. No secrets needed - uses OpenID Connect (OIDC)

For more details, see the [PyPI documentation on Trusted Publishing](https://docs.pypi.org/trusted-publishers/).
