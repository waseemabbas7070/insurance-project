from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV


class Models:
    def __init__(self):
        pass
    def model_svc(self):
        parameters = {
            'C': [ 1, 10, 100, 1000],
            'kernel': ['rbf', 'poly', 'sigmoid', 'linear'],
            'gamma': ['scale'],
        }

        sv = SVC()
        grid = GridSearchCV(estimator=sv, param_grid=parameters,scoring='accuracy' ,cv=5)
        return grid