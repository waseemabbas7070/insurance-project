from  .dataloading import Loader
import pandas as pd

PATH = r'artifacts\breast cancer.csv'
loader = Loader()
data = loader.data_loader(PATH)
class Clean:
    def __init__(self):
        pass
    def cleaning(self,data=data):
        data = data.drop(["id","Unnamed: 32"], axis=1)
        data.drop_duplicates(inplace=True)
        data = data.dropna()

        data.to_csv('./artifacts/clean_data.csv')
        return data