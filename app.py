import streamlit as st
import pandas as pd
import pickle

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Customer Prediction App",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================
@st.cache_resource
def load_model():
    with open("final_model_rf.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# =====================================================
# SIDEBAR MENU
# =====================================================
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio(
    "Pilih Mode Prediksi",
    ["Single Prediction", "Bulk Prediction"]
)

# =====================================================
# SINGLE PREDICTION (SIMPLIFIED & SAFE)
# =====================================================
if menu == "Single Prediction":
    st.title("🔍 Single Customer Prediction")
    st.caption("Mode simulasi – field disederhanakan, sisanya otomatis")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 30)

        housing = st.selectbox(
            "Housing Loan (KPR)",
            ["no", "yes", "unknown"]
        )

        loan = st.selectbox(
            "Personal Loan",
            ["no", "yes", "unknown"]
        )

    with col2:
        job = st.selectbox(
            "Job",
            [
                "admin.",
                "blue-collar",
                "entrepreneur",
                "housemaid",
                "management",
                "retired",
                "self-employed",
                "services",
                "student",
                "technician",
                "unemployed",
                "unknown"
            ]
        )

        marital = st.selectbox(
            "Marital Status",
            ["single", "married", "divorced", "unknown"]
        )

        education = st.selectbox(
            "Education",
            [
                "basic.4y",
                "basic.6y",
                "basic.9y",
                "high.school",
                "professional.course",
                "university.degree",
                "unknown"
            ]
        )

    # -------------------------------------------------
    # BASE INPUT
    # -------------------------------------------------
    input_df = pd.DataFrame([{
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "housing": housing,
        "loan": loan
    }])

    # -------------------------------------------------
    # AUTO-FILL REQUIRED MODEL FEATURES
    # -------------------------------------------------
    input_df["balance"] = 0.0
    input_df["duration"] = 100
    input_df["campaign"] = 1
    input_df["previous"] = 0
    input_df["poutcome"] = "unknown"
    input_df["month"] = "may"
    input_df["day_of_week"] = "mon"
    input_df["euribor3m"] = 4.0

    input_df["default"] = "no"
    input_df["contact"] = "cellular"

    input_df["cons.price.idx"] = 93.5
    input_df["cons.conf.idx"] = -40.0

    input_df["campaign_capped"] = 1
    input_df["is_previously_contacted"] = 0

    st.subheader("Input Data (Final ke Model)")
    st.dataframe(input_df, use_container_width=True)

    if st.button("Predict"):
        try:
            prediction = model.predict(input_df)
            probability = model.predict_proba(input_df)

            st.success(f"Prediction Result: **{prediction[0]}**")
            st.metric("Probability YES", f"{probability[0][1]:.2%}")

        except Exception as e:
            st.error("❌ Error saat prediksi")
            st.code(str(e))

# =====================================================
# BULK PREDICTION (REAL USE CASE)
# =====================================================
else:
    st.title("📂 Bulk Customer Prediction")
    st.caption("Upload CSV / Excel dengan kolom sesuai data training")

    uploaded_file = st.file_uploader(
        "Upload File",
        type=["csv", "xlsx"]
    )

    if uploaded_file:
        df = (
            pd.read_csv(uploaded_file)
            if uploaded_file.name.endswith(".csv")
            else pd.read_excel(uploaded_file)
        )

        st.subheader("Preview Data")
        st.dataframe(df.head(), use_container_width=True)

        if st.button("Run Prediction"):
            try:
                preds = model.predict(df)
                probas = model.predict_proba(df)

                df["prediction"] = preds
                df["probability_yes (%)"] = (probas[:, 1] * 100).round(2)
                df["probability_no (%)"] = (probas[:, 0] * 100).round(2)

                st.success("✅ Prediction selesai")
                st.dataframe(df, use_container_width=True)

                st.download_button(
                    "⬇️ Download Result",
                    df.to_csv(index=False).encode("utf-8"),
                    "prediction_result.csv",
                    "text/csv"
                )

            except Exception as e:
                st.error("❌ Error saat prediksi")
                st.code(str(e))
