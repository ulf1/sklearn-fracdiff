[![PyPI version](https://badge.fury.io/py/sklearn-fracdiff.svg)](https://badge.fury.io/py/sklearn-fracdiff)
[![sklearn-fracdiff](https://snyk.io/advisor/python/sklearn-fracdiff/badge.svg)](https://snyk.io/advisor/python/sklearn-fracdiff)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ulf1/sklearn-fracdiff.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/sklearn-fracdiff/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ulf1/sklearn-fracdiff.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/sklearn-fracdiff/context:python)
[![deepcode](https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6InVsZjEiLCJyZXBvMSI6InNrbGVhcm4tZnJhY2RpZmYiLCJpbmNsdWRlTGludCI6ZmFsc2UsImF1dGhvcklkIjoyOTQ1MiwiaWF0IjoxNjE5NTQwNDUwfQ.KgIRPr_d9Lea36sOqfnkKHr-KOtkhiuZN3JwqV3JCQA)](https://www.deepcode.ai/app/gh/ulf1/sklearn-fracdiff/_/dashboard?utm_content=gh%2Fulf1%2Fsklearn-fracdiff)

# sklearn-fracdiff


## Usage
```python
from sklearn_fracdiff import FracDiff
obj = FracDiff(order=0.7)
obj.fit(X)
Z = obj.transform(X)
```

Check the [examples](http://github.com/ulf1/sklearn-fracdiff/examples) folder for notebooks.


## Appendix

## Installation
The `sklearn-fracdiff` [git repo](http://github.com/ulf1/sklearn-fracdiff) is available as [PyPi package](https://pypi.org/project/sklearn-fracdiff)

```
pip install sklearn-fracdiff
pip install git+ssh://git@github.com/ulf1/sklearn-fracdiff.git
```

### Install a virtual environment

```
python3.6 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)

### Python commands

* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `pytest`

Publish

```sh
pandoc README.md --from markdown --to rst -s -o README.rst
python setup.py sdist 
twine upload -r pypi dist/*
```

### Clean up 

```
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .venv
```

### Support
Please [open an issue](https://github.com/ulf1/sklearn-fracdiff/issues/new) for support.


### Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/sklearn-fracdiff/compare/).
