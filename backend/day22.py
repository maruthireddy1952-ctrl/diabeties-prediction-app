from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error,precision_score
import joblib
from sklearn.model_selection import KFold;
data=load_diabetes()
X=data.data
scaler=MinMaxScaler(X)
y=data.target


kfold=KFold(n_splits=5)
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.6,random_state=42)

model=LinearRegression()
for train_index,test_index in kfold.split(X,y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    model.fit(X_train,y_train)

    y_pred=model.predict(X_test)
   

joblib.dump(model,"diabetes.pkl")
