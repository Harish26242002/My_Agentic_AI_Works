📊 Agentic AI Data Analyzer

A Multi-Agent AI Framework that allows users to upload CSV or Excel datasets and automatically generate AI-powered PDF reports with insights.

The system uses multiple specialized agents to process data, analyze results using an LLM, and generate structured reports.

🚀 Features

🤖 Multi-Agent Architecture

📂 CSV / Excel file upload

🧠 AI-powered data analysis

📄 Automatic PDF report generation

🖥 Streamlit UI for interaction

⚡ FastAPI backend support

🔄 Agent orchestration workflow

🧠 Architecture

The system follows an Agentic AI pipeline.

User Uploads File
        │
        ▼
FileAgent
(load CSV/XLSX using Pandas)
        │
        ▼
AnalysisAgent
(AI analyzes dataset using LLM)
        │
        ▼
PDFAgent
(generate structured PDF report)
        │
        ▼
Downloadable PDF Report

Agents are coordinated by the OrchestratorAgent.

🗂 Project Structure
Agentic_AI/
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── file_agent.py
│   ├── analysis_agent.py
│   ├── pdf_agent.py
│   └── orchestrator.py
│
├── uploads/           # uploaded datasets
├── pdf_outputs/       # generated reports
│
├── streamlit_app.py   # Streamlit UI
├── main.py            # FastAPI backend
│
├── requirements.txt
├── .env.example
└── README.md
⚙️ Installation

Clone or navigate to the project directory.

Install dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file.

Example:

OPENAI_API_KEY=your_openai_key
MODEL_NAME=gpt-4o-mini
▶️ Running the Application
Run Streamlit UI
streamlit run streamlit_app.py

Open:

http://localhost:8501
Optional: Run FastAPI Backend
uvicorn main:app --reload

API available at:

http://localhost:8000
📂 Usage

Open the Streamlit UI

Upload a CSV or Excel file

Click Generate Report

The AI analyzes the dataset

Download the generated PDF report

📊 Example Dataset

Example CSV file:

name,sales,region
John,1000,US
Sarah,1500,EU
Mike,900,Asia
Anna,2000,US

The system will generate a PDF summary with insights.

🛠 Technologies Used

LangChain

LangGraph

FastAPI

Streamlit

Pandas

FPDF

OpenAI API

💡 Future Improvements

Possible upgrades:

📈 Automatic charts in PDF reports

🧠 LangGraph-based agent workflow

📊 Advanced data visualization

🌐 Full web dashboard

☁ Cloud deployment

📄 License

This project is provided for educational and development purposes.
