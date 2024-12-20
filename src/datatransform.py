from .datacleaning import Clean
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

clean = Clean()
data_clean = clean.cleaning()
class Transform:
    def __init__(self):
        pass
    def transformation(self, data=data_clean):
       X = data.drop(['diagnosis'], axis=1)
       Y = data['diagnosis'] 

    #    Scaling
       scaler = StandardScaler()
       scaler.fit(X)
       X = scaler.transform(X)

    #    Encoding
       encoder = LabelEncoder()
       encoder.fit(Y)
       Y = encoder.transform(Y)
       return X,Y