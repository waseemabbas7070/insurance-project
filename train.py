from src.dataspliter import Spliting
from pipelien.model import Models
import joblib as j
from sklearn.metrics import accuracy_score

spliter = Spliting()
x_train, x_test, y_train, y_test = spliter.split()

models = Models()
grid = models.model_svc()

print('Starting Training')

grid.fit(x_test, y_test)

best_model = grid.best_params_

print('Got the Best Model')

predict = grid.predict(x_test)

acc = accuracy_score(y_test, predict)
print(acc)

j.dump(best_model, 'models/model.pkl')
print('Model Saved')