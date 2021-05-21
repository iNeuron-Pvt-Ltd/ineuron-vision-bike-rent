import pandas as pd
from pandas.io.json import json_normalize

class user_input:
    def __init__(self, df):
        try:
            self.df = pd.DataFrame(json_normalize(df))
        except Exception as e:
            print('Error Occured : ',e)

    def get_user_input(self, df):
        return df