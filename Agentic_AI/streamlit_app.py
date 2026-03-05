import streamlit as st
import os
import pandas as pd
from agents.orchestrator import OrchestratorAgent

# Page configuration
st.set_page_config(
    page_title="Agentic AI Data Analyzer",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("🤖 Agentic AI")
st.sidebar.markdown("""
Upload a dataset and generate **AI-powered insights**.

Supported formats:
- CSV
- Excel (.xlsx)

This app uses multiple AI agents to analyze data and generate reports.
""")

# Main Title
st.title("📊 Agentic AI Data Analyzer")

st.markdown(
"""
Upload a **CSV or Excel dataset** to automatically generate an **AI-powered PDF report**.
"""
)

# File uploader
uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Create uploads folder
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    # Save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded successfully: {uploaded_file.name}")

    # Load dataframe
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    # Dataset preview
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # Dataset info
    st.subheader("📊 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Number of Rows", df.shape[0])

    with col2:
        st.metric("Number of Columns", df.shape[1])

    # Visualization
    st.subheader("📈 Data Visualization")

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:
        st.bar_chart(df[numeric_columns])
    else:
        st.warning("No numeric columns available for visualization")

    # Generate report
    if st.button("🚀 Generate AI Report"):

        with st.spinner("AI agents are analyzing the dataset and generating report..."):

            orchestrator = OrchestratorAgent()

            pdf_path = orchestrator.run_file_pipeline(file_path)

        st.success("Report generated successfully!")

        # Download button
        with open(pdf_path, "rb") as file:
            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name=os.path.basename(pdf_path),
                mime="application/pdf"
            )

        st.info(f"PDF saved at: {pdf_path}")

# Footer
st.markdown("---")

st.markdown(
"""
Built with **LangChain, LangGraph, Streamlit, and Agentic AI architecture**
"""
)
