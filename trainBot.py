### pandas is for creating manipulating dataframes, sklearn is a machine learning library
###also instqal scikit-learn
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


class computer:

    def __init__(self):
        #for the .csv line below, right click on the csv file in your IDE and copy the absolute path
        training_data = pd.read_csv('/Users/kevinha/PycharmProjects/pongWithMachineLearning/data.csv')

        ### adjust paddle velocity, in trainData.py the velocity is saved a frame late
        ###for i in range(0, len(training_data) - 1):
            ###training_data.loc[i][5] = training_data.loc[i + 1][5]

        ### filter out when paddle is stationary
        ##training_data=training_data[training_data['dir']!=0]


        print(training_data)

        ### split training and testing datasets
        testing_data = training_data['playerY']
        training_data= training_data.drop(['playerY'],axis=1)
        training_data = training_data.drop(['dir'], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(training_data, testing_data)

        ### train Random Forest Model(average of decision trees)
        self.model = RandomForestRegressor(n_estimators=100, min_samples_split=2, min_samples_leaf=2)
        self.model.fit(X_train.values, y_train.values)

        ### test model
        predictions = self.model.predict(X_test)
        print("Mean Squared Error for ")

        ### print mean squared error
        print(mean_squared_error(y_test, predictions))
        print("Predicted vs Actual Values")

        ###print sample predictions
        df = pd.DataFrame({'Actual': y_test, 'Predictions': predictions})
        print(df)



    ### use model to predict your movements given ball data
    def move(self,input):
        predictedVelo=self.model.predict(input)[0]
        return predictedVelo

temp= computer()


