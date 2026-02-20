# Customer Churn Prediction for Maji Mazuri Stores
# Small synthetic dataset (50 rows) + Random Forest + Plotly visualizations

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ------------------------------
# 1. Create fictional dataset (150 customers)
# ------------------------------

np.random.seed(42)

n = 150

data = {
    'CustomerID': range(1001, 1001 + n),
    'Age': np.random.randint(18, 70, n),
    'MonthlySpending_KES': np.random.normal(4500, 2200, n).clip(800, 14000).round(0),
    'Tenure_Months': np.random.randint(1, 60, n),
    'Num_Complaints_Last6M': np.random.poisson(0.7, n).clip(0, 5),
    'Loyalty_Points': np.random.randint(0, 3200, n),
    'Last_Purchase_Days_Ago': np.random.exponential(45, n).clip(1, 365).astype(int),
    'Has_MajiCard': np.random.choice([0, 1], n, p=[0.65, 0.35]),
    'Region': np.random.choice(['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Other'], n, p=[0.40, 0.18, 0.12, 0.15, 0.15]),
    'Churn': np.zeros(n, dtype=int)   # to be filled
}

df = pd.DataFrame(data)

# Simple realistic churn rule (for synthetic data)
df['Churn'] = (
    (df['Last_Purchase_Days_Ago'] > 90) |
    (df['Num_Complaints_Last6M'] >= 3) |
    (df['Tenure_Months'] < 6) & (df['MonthlySpending_KES'] < 2000) |
    (df['Loyalty_Points'] < 300) & (df['Last_Purchase_Days_Ago'] > 60)
).astype(int) + np.random.binomial(1, 0.08, n)   # add some noise

df['Churn'] = df['Churn'].clip(0, 1)

print("Dataset created:")
print(df['Churn'].value_counts(normalize=True).mul(100).round(1).astype(str) + " %")
print()

# ------------------------------
# 2. Prepare data
# ------------------------------

# Features
X = df.drop(columns=['CustomerID', 'Churn'])

# Target
y = df['Churn']

# One-hot encode categorical column
X = pd.get_dummies(X, columns=['Region'], drop_first=True)

# Train-test split (small dataset → we use 70/30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

print(f"Training set: {len(X_train)} rows | Test set: {len(X_test)} rows\n")

# ------------------------------
# 3. Train Random Forest
# ------------------------------

rf = RandomForestClassifier(
    n_estimators=120,
    max_depth=6,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    class_weight='balanced'
)

rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)
y_prob = rf.predict_proba(X_test)[:, 1]

# Performance
acc = accuracy_score(y_test, y_pred)
print("Random Forest Performance on test set")
print(f"Accuracy:  {acc:.1%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=2))
print()

# ------------------------------
# 4. Visualizations with Plotly
# ------------------------------

# A. Feature Importance
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

fig1 = px.bar(
    importances.head(10),
    x='importance',
    y='feature',
    orientation='h',
    title='Top Features for Predicting Churn – Maji Mazuri Stores',
    labels={'importance': 'Importance', 'feature': ''},
    color='importance',
    color_continuous_scale='Teal'
)
fig1.update_layout(height=480, width=780, showlegend=False)
fig1.show()

# B. Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
cm_labels = ['Stay', 'Churn']

fig2 = go.Figure(data=go.Heatmap(
    z=cm,
    x=cm_labels,
    y=cm_labels,
    text=cm,
    texttemplate="%{text}",
    colorscale='RdBu_r',
    showscale=True
))
fig2.update_layout(
    title='Confusion Matrix – Maji Mazuri Stores Churn Prediction',
    xaxis_title="Predicted",
    yaxis_title="Actual",
    width=520,
    height=520
)
fig2.show()

# C. Churn Probability Distribution
fig3 = px.histogram(
    x=y_prob,
    nbins=20,
    title='Distribution of Predicted Churn Probabilities',
    labels={'value': 'Predicted Churn Probability', 'count': 'Number of Customers'},
    color_discrete_sequence=['#2ca02c'],
    opacity=0.75
)
fig3.add_vline(x=0.5, line_dash="dash", line_color="red", annotation_text="Decision threshold 0.5")
fig3.update_layout(height=420, width=780, bargap=0.1)
fig3.show()

# D. Quick scatter – Last Purchase Days vs Monthly Spending (colored by predicted churn prob)
test_df = X_test.copy()
test_df['Churn_Probability'] = y_prob
test_df['Actual_Churn'] = y_test.values

fig4 = px.scatter(
    test_df,
    x='Last_Purchase_Days_Ago',
    y='MonthlySpending_KES',
    color='Churn_Probability',
    size='Churn_Probability',
    hover_data=['Actual_Churn'],
    title='Test Customers: Last Purchase vs Spending (color = predicted churn risk)',
    color_continuous_scale='YlOrRd',
    labels={'Last_Purchase_Days_Ago': 'Days since last purchase', 'MonthlySpending_KES': 'Monthly Spending (KES)'}
)
fig4.update_layout(height=520, width=820)
fig4.show()

print("\nVisualizations generated. End of analysis.")