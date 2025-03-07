import pandas as pd
import function_ijaz

df=pd.DataFrame(['Religion/Religious Practice','Gender', 'Sexual Orientation','Hate Crime','Race/Color','Disability])

def test_removal_of_colour(df):
        expected_output = ['Religion/Religious Practice', 'Gender', 'Sexual Orientation', 'Hate Crime', 'Race', 'Disability']
        new_df=function_ijaz(df)
        assert
        
        return 