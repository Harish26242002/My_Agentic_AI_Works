# 📊 Agentic AI Data Analyzer

A **Multi-Agent AI Framework** that allows users to upload **CSV or Excel datasets** and automatically generate **AI-powered PDF reports** with insights.

The system uses multiple specialized AI agents to process data, analyze results using a Large Language Model (LLM), and generate structured reports.

---

# 🚀 Features

* 🤖 **Multi-Agent Architecture**
* 📂 **CSV / Excel file upload**
* 🧠 **AI-powered data analysis**
* 📄 **Automatic PDF report generation**
* 🖥 **Streamlit UI for interaction**
* ⚡ **FastAPI backend support**
* 🔄 **Agent orchestration workflow**
* 📊 **Dataset preview and visualization**

---

# 🧠 Architecture

The system follows an **Agentic AI pipeline** where multiple agents collaborate to process and analyze data.

User Uploads File
↓
FileAgent (Loads CSV/XLSX using Pandas)
↓
AnalysisAgent (AI analyzes dataset using LLM)
↓
PDFAgent (Generates structured PDF report)
↓
Downloadable PDF Report

The workflow is coordinated by the **OrchestratorAgent**.

---

# 🗂 Project Structure

Agentic_AI/

agents/
  **init**.py
  base_agent.py
  file_agent.py
  analysis_agent.py
  pdf_agent.py
  orchestrator.py

uploads/  # uploaded datasets
pdf_outputs/  # generated reports

streamlit_app.py  # Streamlit UI
main.py  # FastAPI backend

requirements.txt
.env.example
README.md

---

# ⚙️ Installation

Clone or navigate to the project directory.

Install dependencies:

pip install -r requirements.txt

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

OPENAI_API_KEY=your_openai_key
MODEL_NAME=gpt-4o-mini

---

# ▶️ Running the Application

### Run Streamlit UI

streamlit run streamlit_app.py

Open in browser:

http://localhost:8501

---

### Optional: Run FastAPI Backend

uvicorn main:app --reload

API available at:

http://localhost:8000

---

# 📂 Usage

1. Open the **Streamlit UI**
2. Upload a **CSV or Excel file**
3. Preview dataset and visualizations
4. Click **Generate AI Report**
5. Download the generated **PDF report**

---

# 📊 Example Dataset

Example CSV file:

name,sales,region
John,1000,US
Sarah,1500,EU
Mike,900,Asia
Anna,2000,US

The system will generate a **PDF summary with insights and analysis**.

---

# 🛠 Technologies Used

* LangChain – LLM application framework
* LangGraph – multi-agent workflow orchestration
* FastAPI – backend API framework
* Streamlit – interactive UI
* Pandas – data processing
* FPDF – PDF generation
* OpenAI API – large language model

---

# 💡 Future Improvements

Possible upgrades:

* 📈 Automatic charts inside generated PDF reports
* 🧠 Advanced LangGraph agent workflow
* 📊 More advanced data visualizations
* 🌐 Full web dashboard with authentication
* ☁ Cloud deployment support

---

# 📄 License

This project is provided for **educational and development purposes**.
