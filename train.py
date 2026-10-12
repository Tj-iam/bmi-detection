from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
df = pd.read_csv('bmi.csv')
df.info()
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
X = df[['Gender', 'Height', 'Weight']]
y = df['Index']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))


#Model Test
gender = 0  # 0 = Male, 1 = Female
height = 169 # in cm
weight = 114  # in kg
# Calculate BMI
bmi = weight / (height / 100) ** 2

sample = pd.DataFrame([[gender, height, weight]], columns=['Gender', 'Height', 'Weight'])
labels = ['Extremely Weak', 'Weak', 'Normal', 'Overweight ', 'Obesity ', 'Extreme Obesity ']
prediction = model.predict(sample)
print(labels[prediction[0]])
print(f"BMI: {bmi:.2f}")