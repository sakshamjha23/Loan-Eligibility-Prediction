import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("Housing.csv")

# =========================
# ENCODING
# =========================
binary_map = {'yes': 1, 'no': 0}
cols = ['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea']

for col in cols:
    df[col] = df[col].map(binary_map)

furnish_map = {'furnished':2,'semi-furnished':1,'unfurnished':0}
df['furnishingstatus'] = df['furnishingstatus'].map(furnish_map)

# =========================
# CREATE TARGET
# =========================
threshold = df['price'].median()
df['Loan_Status'] = df['price'].apply(lambda x: 1 if x > threshold else 0)

X = df.drop(['price','Loan_Status'], axis=1)
y = df['Loan_Status']

# =========================
# TRAIN MODEL
# =========================
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=300,max_depth=12,random_state=42)
model.fit(X_train,y_train)

# =========================
# STREAMLIT UI
# =========================
st.title("🏦 Loan Eligibility Prediction System")

st.write("Enter property details to check loan eligibility:")

area = st.number_input("Area", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)
stories = st.number_input("Stories", min_value=0)
parking = st.number_input("Parking", min_value=0)

mainroad = st.selectbox("Main Road", ["yes","no"])
guestroom = st.selectbox("Guest Room", ["yes","no"])
basement = st.selectbox("Basement", ["yes","no"])
hotwater = st.selectbox("Hot Water Heating", ["yes","no"])
ac = st.selectbox("Air Conditioning", ["yes","no"])
prefarea = st.selectbox("Preferred Area", ["yes","no"])

furnishing = st.selectbox(
    "Furnishing",
    ["furnished","semi-furnished","unfurnished"]
)

# =========================
# PREDICTION BUTTON
# =========================
if st.button("Check Eligibility"):

    input_data = pd.DataFrame({
        'area':[area],
        'bedrooms':[bedrooms],
        'bathrooms':[bathrooms],
        'stories':[stories],
        'mainroad':[binary_map[mainroad]],
        'guestroom':[binary_map[guestroom]],
        'basement':[binary_map[basement]],
        'hotwaterheating':[binary_map[hotwater]],
        'airconditioning':[binary_map[ac]],
        'parking':[parking],
        'prefarea':[binary_map[prefarea]],
        'furnishingstatus':[furnish_map[furnishing]]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved (Eligible)")
    else:
        st.error("❌ Loan Not Approved (Not Eligible)")