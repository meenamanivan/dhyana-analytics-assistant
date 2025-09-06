# DhyanaMD Analytics Assistant

This project is a prototype for an AI-powered analytics assistant that supports product decision-making in a health-tech context. It simulates data from a fictional platform, **DhyanaMD**, where doctors prescribe meditation and journaling as part of patient care.

The assistant is designed to analyze key product patterns around user retention, engagement, healing outcomes, and feature adoption. It uses **synthetic data**, **parameterized simulations**, and lays the foundation for a Retrieval-Augmented Generation (RAG) interface.

---

## Project Goals

- Demonstrate AI-native product analytics thinking  
- Simulate user behavior and product evolution over time  
- Enable natural-language analytics with LLM + code generation (future scope)  
- Showcase an end-to-end pipeline from synthetic data to insights  

---

## Key Features

- **Synthetic Dataset Generation**  
  Simulates platform growth from 2022–2025 with 65,000+ patients and 4,000 doctors  
  Includes traits like churn, healing, reengagement, and power usage  

- **Parameter-Driven Simulation**  
  Growth rates, program completion likelihood, healing probability, etc.  
  All configurable via CSV  

- **Planned AI Integration (RAG)**  
  A Retrieval-Augmented Generation layer to interpret natural language PM questions  
  Will retrieve relevant logic templates and generate analysis code  

---

## Folder Structure

dhyana-analytics-assistant/
├── data/
│   ├── dhyana_parameters.csv       # Simulation parameters
│   ├── synthetic_users.csv         # Generated users (doctors + patients)
│   └── synthetic_events.csv        # Simulated user behavior over time
├── scripts/
│   └── generate_data.py            # Main synthetic data generation script
├── .gitignore
├── README.md
└── requirements.txt

Coming Soon
	•	Streamlit-based dashboard for visual exploration
	•	LLM-powered assistant to answer product manager questions
	•	Use-case-specific charts and insights (e.g., funnel, cohort, segmentation)