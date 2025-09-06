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

## 📊 Example Outputs

### `synthetic_users.csv`

| user_id | user_type | signup_date | assigned_doctor | churned_early | completed | healed | power_user | reengaged |
|---------|-----------|-------------|------------------|----------------|-----------|--------|-------------|------------|
| PAT00001 | patient | 2022-04-15 | DOC0001 | True | False | False | False | False |
| PAT00002 | patient | 2022-04-15 | DOC0002 | False | True | True | False | False |
| DOC0001 | doctor | 2022-04-12 | — | — | — | — | — | — |

### `synthetic_events.csv`

| event_id | user_id | timestamp           | event_type      | session_length |
|----------|---------|---------------------|------------------|----------------|
| E001     | PAT00001 | 2022-04-16T09:23:00 | journal_entry    | 5 mins         |
| E002     | PAT00001 | 2022-04-18T07:00:00 | meditation       | 10 mins        |
| E003     | PAT00002 | 2022-04-18T09:45:00 | completed_program| —              |

---

```

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

```

**Coming Soon**

- Streamlit-based dashboard for visual exploration  
- LLM-powered assistant to answer product manager questions  
- Use-case-specific charts and insights (e.g., funnel, cohort, segmentation)