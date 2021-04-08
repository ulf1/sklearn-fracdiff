[![PyPI version](https://badge.fury.io/py/sklearn-fracdiff.svg)](https://badge.fury.io/py/sklearn-fracdiff)

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
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`

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
