# Python script to demonstrate Random Forest Algorithm to predict customer churn for a
# fictional store (Maji Mazuri Traders)

# Import the required modules
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix

# 1. Create a Random dataset (150 Customers)

np.random.seed(42)

data = pd.DataFrame({
    'Age':np.random.randint(18,70,150),
    'Monthly_Spend':np.random.randint(1500,45000,150),
    'Visits_Per_Month':np.random.randint(4,30,150),
    'Membership_Years':np.random.randint(0,15,150),
    'Used_Discount':np.random.randint(0,2,150) # 0 -> NO, 1 -> Yes
})

# Display the first 10 rows
print(f"First 10 rows:\n{data.head(10)}")

# Create churn label
data["Churn"] = (
    (data["Monthly_Spend" ]< 10000) &
    (data["Visits_Per_Month" ] < 9)
).astype(int)

# 2. Prepare data
X = data.drop("Churn",axis=1)
y = data["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=42)

# 3. Train the Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Model Accuracy: {accuracy:.2f}")

# 5. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

fig_cm = px.imshow(
    cm,text_auto=True,labels=dict(X="Predicted",y="Actual",color='Count'),
    x=["No Churn","Churn"],
    y=["No Churn","Churn"],
    title="Confusion Matrix - Customer Churn"
)
fig_cm.show()

# 7. Churn distribution visualisation
fig_churn = px.pie(
    data,
    names="Churn",
    title="Overall Customer Churn distribution",
    labels={"Churn":"Churn status"},
)

fig_churn.update_traces(textinfo='percent+label')
fig_churn.show()
