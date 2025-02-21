
import pandas as pd
from lab4 import calc_mean

#test 1
def test_1_calc_mean():
    df = pd.DataFrame([7,9,10,12,3])
    df = df.rename(columns={0: "Month Number"})
    assert calc_mean(df) == "8.2"

#test 2
def test_2_calc_mean():
    df = pd.DataFrame([4,3,11])
    df = df.rename(columns={0: "Month Number"})
    assert calc_mean(df) == "6.0"

#test 3
def test_3_calc_mean():
    df = pd.DataFrame([3,5,9,10,12,2,3,4])
    df = df.rename(columns={0: "Month Number"})
    assert calc_mean(df) == "6.0"

#python -m pytest test.py
#try again 1
