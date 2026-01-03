import streamlit as st
import pandas as pd
import pickle
from io import BytesIO

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
# SINGLE PREDICTION
# =====================================================
if menu == "Single Prediction":
    st.title("🔍 Single Customer Prediction")
    st.caption("Cek Potensi Nasabah – isi data nasabah secara manual")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 30)
        housing = st.selectbox("Housing Loan (KPR)", ["no", "yes", "unknown"])
        loan = st.selectbox("Personal Loan", ["no", "yes", "unknown"])
        default = st.selectbox("Credit Default", ["no", "yes", "unknown"])

    with col2:
        job = st.selectbox(
            "Job",
            [
                "admin.", "blue-collar", "entrepreneur", "housemaid",
                "management", "retired", "self-employed", "services",
                "student", "technician", "unemployed", "unknown"
            ]
        )
        marital = st.selectbox(
            "Marital Status",
            ["single", "married", "divorced", "unknown"]
        )
        education = st.selectbox(
            "Education",
            [
                "basic.4y", "basic.6y", "basic.9y",
                "high.school", "professional.course",
                "university.degree", "unknown"
            ]
        )
        contact = st.selectbox("Contact Type", ["cellular", "telephone"])

    # -----------------------------
    # DISPLAY INPUT (START FROM No)
    # -----------------------------
    display_df = pd.DataFrame([{
        "No": 1,
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "housing": housing,
        "loan": loan,
        "default": default,
        "contact": contact
    }])

    st.subheader("Input Data")
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    # -----------------------------
    # DATA KE MODEL
    # -----------------------------
    model_df = display_df.drop(columns=["No"]).copy()

    model_df["balance"] = 0
    model_df["duration"] = 100
    model_df["campaign"] = 1
    model_df["previous"] = 0
    model_df["poutcome"] = "unknown"
    model_df["month"] = "may"
    model_df["day_of_week"] = "mon"
    model_df["euribor3m"] = 4.0
    model_df["cons.price.idx"] = 93.5
    model_df["cons.conf.idx"] = -40.0
    model_df["campaign_capped"] = 1
    model_df["is_previously_contacted"] = 0

    # -----------------------------
    # OUTPUT (PROBABILITY ONLY)
    # -----------------------------
    if st.button("Predict"):
        proba = model.predict_proba(model_df)
        prob_yes = proba[0][1] * 100

        st.success("Prediction Result")
        st.metric(
            label="Probability YES",
            value=f"{prob_yes:.2f}%"
        )

# =====================================================
# BULK PREDICTION
# =====================================================
else:
    st.title("📂 Bulk Customer Prediction")
    st.caption("Upload File CSV / File Excel")

    uploaded_file = st.file_uploader(
        "Upload File",
        type=["csv", "xlsx"]
    )

    if uploaded_file:
        df_upload = (
            pd.read_csv(uploaded_file)
            if uploaded_file.name.endswith(".csv")
            else pd.read_excel(uploaded_file)
        )

        st.subheader("Preview Data (Upload)")
        st.dataframe(df_upload.head(), use_container_width=True, hide_index=True)

        # -----------------------------
        # VALIDASI KOLOM MINIMAL
        # -----------------------------
        required_cols = [
            "customer_name",
            "phone_number",
            "age",
            "job",
            "marital",
            "education",
            "default",
            "housing",
            "loan",
            "contact"
        ]

        missing_cols = set(required_cols) - set(df_upload.columns)
        if missing_cols:
            st.error(f"Kolom berikut WAJIB ada: {missing_cols}")
            st.stop()

        # -----------------------------
        # RUN PREDICTION (ONCE)
        # -----------------------------
        if st.button("Run Prediction"):
            df = df_upload.copy()
            df_model = df.copy()

            # AUTO-FILL KOLOM TEKNIS
            df_model["balance"] = 0
            df_model["duration"] = 100
            df_model["campaign"] = 1
            df_model["previous"] = 0
            df_model["poutcome"] = "unknown"
            df_model["month"] = "may"
            df_model["day_of_week"] = "mon"
            df_model["euribor3m"] = 4.0
            df_model["cons.price.idx"] = 93.5
            df_model["cons.conf.idx"] = -40.0
            df_model["campaign_capped"] = 1
            df_model["is_previously_contacted"] = 0

            feature_cols = [
                "age", "job", "marital", "education", "default",
                "housing", "loan", "contact",
                "balance", "duration", "campaign", "previous",
                "poutcome", "month", "day_of_week", "euribor3m",
                "cons.price.idx", "cons.conf.idx",
                "campaign_capped", "is_previously_contacted"
            ]

            X = df_model[feature_cols]

            preds = model.predict(X)
            probas = model.predict_proba(X)

            df["prediction"] = preds
            df["probability_yes (%)"] = (probas[:, 1] * 100).round(2)
            df["probability_no (%)"] = (probas[:, 0] * 100).round(2)

            df.insert(0, "No", range(1, len(df) + 1))

            st.session_state["bulk_result"] = df

        # -----------------------------
        # DISPLAY + DOWNLOAD
        # -----------------------------
        if "bulk_result" in st.session_state:
            result_df = st.session_state["bulk_result"]

            st.success("✅ Prediction selesai")
            st.dataframe(result_df, use_container_width=True, hide_index=True)

            st.subheader("Download Result")

            download_format = st.radio(
                "Pilih format file",
                ["CSV", "Excel"],
                horizontal=True
            )

            if download_format == "CSV":
                download_data = result_df.to_csv(index=False).encode("utf-8")
                file_name = "prediction_result.csv"
                mime_type = "text/csv"
            else:
                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    result_df.to_excel(
                        writer,
                        index=False,
                        sheet_name="Prediction Result"
                    )
                download_data = output.getvalue()
                file_name = "prediction_result.xlsx"
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            st.download_button(
                label="⬇️ Download",
                data=download_data,
                file_name=file_name,
                mime=mime_type
            )
