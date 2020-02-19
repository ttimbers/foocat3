## foocat3 

![](https://github.com/ttimbers/foocat3/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/ttimbers/foocat/branch/master/graph/badge.svg)](https://codecov.io/gh/ttimbers/foocat3) ![Release](https://github.com/ttimbers/foocat3/workflows/Release/badge.svg)

Python package that eases the pain concatenating Pandas categoricals!

### Installation:

```
pip install -i https://test.pypi.org/simple/ foocat3
```

### Features
- TODO

### Dependencies

- TODO

### Usage
```
>>> import pandas as pd
>>> a = pd.Categorical(["character", "hits", "your", "eyeballs"])
>>> b = pd.Categorical(["but", "integer", "where it", "counts"])
>>> cat.catbind(a, b)
```
```
[character, hits, your, eyeballs, but, integer, where it, counts]
Categories (8, object): [but, character, counts, eyeballs, hits, integer, where it, your]
```

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
