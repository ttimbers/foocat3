import pytest

from foocat3 import foocat3

import pandas as pd

def test_catbind():
  a = pd.Categorical(["character", "hits", "your", "eyeballs"])
  b = pd.Categorical(["but", "integer", "where it", "counts"])
  assert ((foocat3.catbind(a, b)).codes == [1, 4, 7, 3, 0, 5, 6, 2]).all()
  assert ((foocat3.catbind(a, b)).categories == ["but", "character", "counts", "eyeballs", "hits", "integer", "where it", "your"]).all()
