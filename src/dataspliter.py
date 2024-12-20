from .datatransform import Transform
from sklearn.model_selection import train_test_split

transform = Transform()
x,y = transform.transformation()

class Spliting:
    def __init__(self):
        pass
    def split(self, x=x, y=y):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
        return x_train, x_test, y_train, y_test