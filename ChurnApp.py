import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('churn_model.pkl')

def main():
    # Page configuration
    st.set_page_config(page_title="Customer Churn Prediction", page_icon="🔮", layout="wide")

    # Basic Styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🔮 Customer Churn Prediction Dashboard")

    # Read Data
    try:
        data = pd.read_excel('churn_dataset.xlsx')
        st.success('✅ Data Loaded Successfully!')
    except FileNotFoundError:
        st.error("❌ Data file 'churn_dataset.xlsx' not found! Please make sure it's in the project folder.")
        return

    # Sidebar Navigation
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "View Data", "Predict Churn"])

    if page == "Home":
        st.subheader("🏠 Welcome to the Customer Churn Prediction App")
        st.write("""
            - 📊 View customer data
            - 🔍 Predict who is likely to churn
            - 📥 Download the results
        """)
        try:
            st.image("churn1.png", use_container_width=True)
        except:
            st.warning("📷 Image file 'churn1.png' not found.")

    elif page == "View Data":
        st.subheader("📊 Preview of Customer Data")
        st.dataframe(data.style.highlight_max(axis=0))

    elif page == "Predict Churn":
        st.subheader("🎯 Churn Prediction Results")

        features = ['Age', 'Tenure', 'Sex']
        if all(col in data.columns for col in features):

            # Encoding 'Sex' column if it's in string format
            if data['Sex'].dtype == 'object':
                data['Sex'] = data['Sex'].map({'Male': 1, 'Female': 0})

            if st.button("🚀 Start Prediction"):
                X = data[features]
                predictions = model.predict(X)
                prediction_proba = model.predict_proba(X)

                result_df = data.copy()
                result_df['Prediction'] = ['💔 Will Churn' if p == 1 else '💚 Will Not Churn' for p in predictions]
                result_df['Churn Probability (%)'] = (prediction_proba[:, 1] * 100).round(2)

                st.success("✅ Prediction Completed!")
                st.dataframe(result_df)

                st.download_button(
                    label="📥 Download Predictions as CSV",
                    data=result_df.to_csv(index=False),
                    file_name="predictions.csv",
                    mime="text/csv"
                )

                st.balloons()
        else:
            st.error(f"❌ The data file must contain these columns: {features}")

if __name__ == '__main__':
    main()
