import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import accuracy_score
import joblib

# Load the data
data = pd.read_csv('C:/Users/DELL/OneDrive/Desktop/heart_disease_health_indicators_BRFSS2015.csv')

# Split the data into features and target
X = data.drop('HeartDiseaseorAttack', axis=1)
y = data['HeartDiseaseorAttack']

# Convert categorical features to numerical features
encoder = OneHotEncoder()
categorical_columns = X.select_dtypes(include='object').columns
X[categorical_columns] = encoder.fit_transform(data[categorical_columns]).toarray()

# Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Select the top 18 features
selector = SelectKBest(k=18)
X_selected = selector.fit_transform(X, y)

# Save selected features to a new Excel sheet
selected_features_df = pd.DataFrame(X_selected, columns=selector.get_support(indices=True))
selected_features_df.to_csv('C:/Users/DELL/OneDrive/Desktop/selected_features.csv', index=False)

# Split the data into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=42)

# Train a MLP classifier model
model = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=500, alpha=0.0001, solver='sgd',
                      verbose=10, random_state=42, tol=0.0001)
model.fit(X_train, y_train)

# # Compute accuracy on the validation set
# y_val_pred = model.predict(X_val)
# accuracy = accuracy_score(y_val, y_val_pred)
# print("Validation Accuracy:", accuracy)

# Compute accuracy on the testing set -> 0.9084
y_test_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_test_pred)
print("Testing Accuracy:", accuracy)

# Save the trained model using Joblib
joblib.dump(model, 'savedModels/MLP_model.joblib')
