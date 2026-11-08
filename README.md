# 🎯 Job Acceptance Prediction System
### *Predictive HR Analytics & Candidate Placement Decision Modeling*

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Database](https://img.shields.io/badge/MySQL-8.0%2B-4479A1.svg?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

---

## 📌 Executive Summary

In contemporary talent acquisition, recruitment and placement teams process thousands of candidate profiles encompassing academic history, skill sets, professional experience, interview performance, and job market dynamics. However, **extending an offer does not guarantee acceptance**—candidate dropouts severely increase cost-per-hire, prolong vacancy times, and disrupt hiring pipelines.

The **Job Acceptance Prediction System** is an end-to-end Machine Learning and HR Analytics solution that predicts whether a candidate will **Accept (Placed / 1)** or **Reject (Not Placed / 0)** a job offer. By identifying the root drivers of candidate decisions and scoring acceptance probability in real time, this system empowers HR managers to proactively counter offer reneging, optimize compensation structures, and streamline evaluation processes.

---

## 📑 Table of Contents

- [🎯 Job Acceptance Prediction System](#-job-acceptance-prediction-system)
  - [📌 Executive Summary](#-executive-summary)
  - [📑 Table of Contents](#-table-of-contents)
  - [🏢 Domain \& Key Skills Takeaways](#-domain--key-skills-takeaways)
  - [💼 Business Problem \& Use Cases](#-business-problem--use-cases)
  - [📊 Dataset Architecture \& Real-World Noise](#-dataset-architecture--real-world-noise)
  - [🛠️ Technical Architecture \& Project Workflow](#️-technical-architecture--project-workflow)
    - [Step 1: Data Collection \& Ingestion](#step-1-data-collection--ingestion)
    - [Step 2: Data Understanding \& Validation](#step-2-data-understanding--validation)
    - [Step 3: Data Cleaning \& Preprocessing](#step-3-data-cleaning--preprocessing)
    - [Step 4: Exploratory Data Analysis (EDA) \& Insights](#step-4-exploratory-data-analysis-eda--insights)
    - [Step 5: Feature Engineering](#step-5-feature-engineering)
    - [Step 6: MySQL Database Integration](#step-6-mysql-database-integration)
    - [Step 7: Machine Learning Classification](#step-7-machine-learning-classification)
  - [📈 Model Evaluation \& Benchmark Results](#-model-evaluation--benchmark-results)
    - [Model Performance Comparison](#model-performance-comparison)
    - [Key Decision Drivers (Feature Importance)](#key-decision-drivers-feature-importance)
  - [🖥️ Streamlit Interactive Dashboard](#️-streamlit-interactive-dashboard)
    - [Core Dashboard KPIs](#core-dashboard-kpis)
    - [Real-Time Inference Interface](#real-time-inference-interface)
  - [🗄️ Database Schema \& SQL Analytics](#️-database-schema--sql-analytics)
  - [📂 Project Organization \& Folder Structure](#-project-organization--folder-structure)
  - [🚀 Quick Start / Local Installation Guide](#-quick-start--local-installation-guide)
  - [📊 Project Evaluation Rubric](#-project-evaluation-rubric)
  - [👥 Project Governance \& Verification](#-project-governance--verification)

---

## 🏢 Domain & Key Skills Takeaways

- **Domains**:
  - Human Resource Analytics (HR Analytics) using Machine Learning
  - Predictive Modeling & Classification in Workforce Intelligence
  - Recruitment, Offer Dropout Mitigation & Placement Analytics
- **Skills Takeaways**:
  - **Data Engineering**: Data cleaning, handling missing and noisy real-world data, deduplication, schema normalization.
  - **Exploratory Data Analysis (EDA)**: Statistical hypothesis testing, bivariate/multivariate visualizations with Seaborn and Matplotlib.
  - **Feature Engineering**: Ratio engineering, domain composite indicators (Academic Index, Assessment Score, Risk Score, CTC Gap).
  - **Machine Learning**: Class-imbalance mitigation, model selection (Logistic Regression, Random Forest), evaluation metrics (ROC-AUC, Precision-Recall, F1).
  - **Application Development**: Building real-time interactive inference dashboards with Streamlit.
  - **Database Integration**: MySQL relational database design, query optimization, and SQLAlchemy connectivity.

---

## 💼 Business Problem & Use Cases

### The Problem
Traditional recruitment workflows suffer from blind spots after extending an offer:
- High candidate dropout rates lead to repeated interview rounds and wasted hiring resources.
- Misaligned salary expectations and unrecognized career risks result in late-stage offer rejections.
- HR managers lack probabilistic visibility into which candidates are at high risk of declining.

### Strategic Business Use Cases
- **Early Warning Offer Dropout System**: Predict candidate acceptance probability prior to rolling out an official offer letter.
- **Compensation & Expectation Alignment**: Analyze CTC gap percentages to offer competitive, acceptable remuneration packages.
- **Candidate Risk Profiling**: Detect high-risk indicators (employment gaps, high notice periods, layoff history) and trigger early HR intervention.
- **Hiring Cycle Optimization**: Reduce time-to-fill by prioritizing active, high-intent candidates.

---

## 📊 Dataset Architecture & Real-World Noise

The project leverages a comprehensive dataset comprising **50,000+ candidate records** designed to emulate real-world placement environments, containing intentional discrepancies:
- **Missing values** across numerical and categorical features.
- **Duplicate records** simulating multiple system entries.
- **Inconsistent categorical inputs** (e.g., casing anomalies in gender, internship experience).

### Feature Breakdown
| Category | Attributes |
| :--- | :--- |
| **Demographics** | `age_years`, `gender` |
| **Academic Performance** | `ssc_percentage`, `hsc_percentage`, `degree_percentage`, `degree_specialization` |
| **Evaluation Scores** | `technical_score`, `aptitude_score`, `communication_score` |
| **Skills & Experience** | `skills_match_percentage`, `certifications_count`, `internship_experience`, `years_of_experience`, `relevant_experience`, `career_switch_willingness` |
| **Market & Compensation** | `previous_ctc_lpa`, `expected_ctc_lpa`, `company_tier`, `competition_level`, `job_role_match`, `bond_requirement` |
| **Operational & Risk Factors** | `notice_period_days`, `layoff_history`, `employment_gap_months`, `relocation_willingness` |
| **Target Variable** | `status` (`Placed` [1] / `Not Placed` [0]) |

*Dataset Source:* [Google Drive Dataset Link](https://drive.google.com/file/d/1h7IY0sNyW7tDoI03nO4lohiYk04o0Hqd/view?usp=sharing)

---

## 🛠️ Technical Architecture & Project Workflow

```
[Raw Candidate Data] (50,000+ records)
          │
          ▼
[Step 1 & 2: Overview & Validation] ──► Schema inspection, missing value analysis, duplicate detection
          │
          ▼
[Step 3: Data Cleaning] ──────────────► Smart domain-guided imputations, casing standardization, deduplication
          │
          ▼
[Step 4: Exploratory Data Analysis] ──► Correlation analysis, target distribution, feature relationships
          │
          ▼
[Step 5: Feature Engineering] ────────► Academic Index, CTC Gap %, Risk Score, One-Hot/Label Encoding, Scaling
          │
    ┌─────┴─────────────────────────────────────┐
    ▼                                           ▼
[Step 6: MySQL Database]            [Step 7: Machine Learning Modeling]
 - Relational table creation         - Logistic Regression (Baseline)
 - Cleaned data ingestion            - Random Forest (Champion)
 - SQL analytical queries            - Class weighting & Hyperparameter tuning
    │                                           │
    └───────────────────┬───────────────────────┘
                        ▼
       [Deployment & Inference Interface]
        ├── Streamlit Web App (`dashboard/app.py`)
        └── Python Inference Engine (`models/use_model.py`)
```

### Step 1: Data Collection & Ingestion
- Ingested 50,124 raw candidate entries.
- Loaded into pandas DataFrame for structure verification.

### Step 2: Data Understanding & Validation
- Verified data types (continuous floats, discrete integers, categoricals).
- Analyzed target variable distribution: ~30.3% Placed vs ~69.7% Not Placed (indicates moderate class imbalance).

### Step 3: Data Cleaning & Preprocessing
- **Deduplication**: Identified and purged 124 exact duplicate records, leaving 50,000 unique candidate profiles.
- **Domain-Guided Imputation**:
  - Academic scores imputed by group medians based on `degree_specialization`.
  - Missing `job_role_match` inferred using candidate `skills_match_percentage` thresholds.
  - Notice periods imputed based on `years_of_experience` cohorts.
  - Employment gaps defaulted to `0` for freshers.
  - Layoff history imputed contextually based on extended career gaps.

### Step 4: Exploratory Data Analysis (EDA) & Insights
- **Skills Match vs Placement**: Candidates with skills match $>75\%$ exhibited significantly higher placement rates.
- **Job Role Match**: Matched candidates had a **35.2%** acceptance rate vs **15.2%** for mismatched candidates.
- **Interview Performance**: Technical score demonstrated the strongest individual correlation with final acceptance.
- **Competition Level**: Highly competitive job markets depressed acceptance rates down to **23.8%**.

### Step 5: Feature Engineering
Engineered high-signal composite indicators:
- **`academic_index`**: Weighted composite score $(0.25 \times \text{SSC} + 0.35 \times \text{HSC} + 0.40 \times \text{Degree})$.
- **`overall_assessment`**: Weighted evaluation $(0.40 \times \text{Technical} + 0.30 \times \text{Aptitude} + 0.30 \times \text{Communication})$.
- **`ctc_gap` & `ctc_gap_percentage`**: Absolute and percentage difference between expected and previous CTC.
- **`risk_score`**: Composite dropout risk derived from layoff history, employment gap $> 12$ months, and notice period $> 60$ days.
- **`skills_tech_ratio`** & **`exp_salary_ratio`**: Interaction ratios capturing skill depth and market value expectation.
- Categorical features transformed using **One-Hot Encoding** and numerical features normalized via **StandardScaler**.

### Step 6: MySQL Database Integration
- Designed an enterprise relational schema (`job_acceptance_data`) in MySQL.
- Ingested cleaned analytical datasets using **SQLAlchemy** for scalable reporting and analytical querying.

### Step 7: Machine Learning Classification
- Target variable mapped: `Placed` $\rightarrow 1$ (Accept Offer), `Not Placed` $\rightarrow 0$ (Reject Offer).
- Implemented **Stratified 80/20 Train-Test Split**.
- Handled class imbalance using **Balanced Class Weighting** (`class_weight='balanced'`).
- Trained and evaluated candidate classifiers: **Logistic Regression** and **Random Forest Classifier**.

---

## 📈 Model Evaluation & Benchmark Results

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** (Baseline) | 85.88% | 71.75% | **87.97%** | 79.04% | 0.9431 |
| **Random Forest Classifier** (Selected Champion) | **88.91%** | **79.91%** | 84.65% | **82.21%** | **0.9554** |

> **Champion Selection**: While Logistic Regression achieved strong recall, the **Random Forest Classifier** yielded superior overall accuracy (88.91%), higher precision (79.91%), a balanced F1-score (82.21%), and an outstanding **ROC-AUC of 0.9554**, demonstrating strong discriminative ability across decision thresholds.

### Key Decision Drivers (Feature Importance)

The top 10 most influential features driving offer acceptance in the Random Forest model:

| Rank | Feature | Importance Score | Business Interpretation |
| :---: | :--- | :---: | :--- |
| 1 | `technical_score` | **15.38%** | Candidate technical competency during evaluations |
| 2 | `exp_salary_ratio` | **10.76%** | Alignment between experience level and compensation demands |
| 3 | `interview_score` | **10.04%** | Weighted composite interview evaluation |
| 4 | `total_score` | **7.66%** | Comprehensive candidate merit profile |
| 5 | `years_of_experience` | **6.38%** | Total professional tenure |
| 6 | `overall_assessment` | **5.90%** | Combined technical, aptitude, and communication index |
| 7 | `skills_match_percentage`| **5.22%** | Degree of alignment with required job description skills |
| 8 | `job_role_match` | **4.79%** | Direct alignment between past domain and prospective role |
| 9 | `skills_tech_ratio` | **3.72%** | Verification of theoretical vs applied technical capability |
| 10 | `ctc_gap` | **3.31%** | Salary hike expectation delta |

---

## 🖥️ Streamlit Interactive Dashboard

An intuitive, interactive web application designed for HR recruiters and talent acquisition leaders.

### Core Dashboard KPIs
- 👥 **Total Candidates**: Real-time volume of evaluated candidates.
- 📈 **Placement Rate (%)**: Historical placement benchmark.
- 🎯 **Job Acceptance Rate (%)**: Percentage of offers accepted.
- 🧠 **Average Interview Score**: Aggregate evaluation metric.
- 📊 **Average Skills Match %**: Talent alignment index.
- ⚠️ **Offer Dropout Rate**: Tracked dropouts to trigger pipeline interventions.
- 🚨 **High-Risk Candidate Percentage**: Proportion of candidates flagged for reneging risks.

### Real-Time Inference Interface
Recruiters can adjust candidate profiles via the interactive sidebar:
1. **Academic & Skills**: Skills Match %, Academic Index, Overall Assessment.
2. **Interview Performance**: Technical, Aptitude, Communication scores.
3. **Compensation & Risk**: CTC Gap %, Composite Risk Score.

**Instant Output**:
- **Acceptance Decision**: `✅ WILL ACCEPT OFFER` or `❌ LIKELY TO REJECT`.
- **Metrics**: Acceptance Probability (%) & Model Confidence (%).
- **Visual Probability Breakdown**: Progress bars illustrating Accept vs Reject odds.
- **Actionable HR Recommendations**:
  - *Low Risk*: Proceed immediately with offer rollout, initiate expedited onboarding.
  - *High Risk*: Revisit compensation package, verify role expectations, conduct recruiter check-in.

---

## 🗄️ Database Schema & SQL Analytics

The repository includes a ready-to-run MySQL script: [`Db/sql_database_setup.sql`](Db/sql_database_setup.sql).

### Key SQL Analytical Queries Included:
```sql
-- 1. Overall Placement & Offer Acceptance Distribution
SELECT
    placement_status,
    COUNT(*) AS total_candidates,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM job_acceptance_data), 2) AS percentage
FROM job_acceptance_data
GROUP BY placement_status;

-- 2. Average Placement Probability by Experience Cohort
SELECT
    CASE
        WHEN years_of_experience = 0 THEN 'Fresher'
        WHEN years_of_experience BETWEEN 1 AND 3 THEN 'Junior'
        WHEN years_of_experience BETWEEN 4 AND 7 THEN 'Mid'
        ELSE 'Senior'
    END AS experience_level,
    ROUND(AVG(placement_probability_score), 2) AS avg_probability
FROM job_acceptance_data
GROUP BY experience_level;
```

---

## 📂 Project Organization & Folder Structure

```
Job_Acceptance_Prediction_System/
│
├── dashboard/
│   ├── app.py                     # Streamlit web application
│   └── requirements.txt           # Dashboard dependencies
│
├── Db/
│   └── sql_database_setup.sql     # MySQL schema, table creation & analytical queries
│
├── models/
│   ├── use_model.py               # Standalone programmatic inference engine
│   ├── best_model.pkl             # Serialized Random Forest classifier
│   └── model_features.pkl         # Serialized feature column list
│
├── notebooks/
│   ├── 01_data_overview.ipynb     # Phase 1: Data overview & preliminary analysis
│   ├── 02_data_cleaning.ipynb     # Phase 2: Missing values, duplicates & noise handling
│   ├── 03_eda_hr_insights.ipynb   # Phase 3: Exploratory data analysis & HR insights
│   ├── 04_feature_engineering.ipynb # Phase 4: Feature extraction, scaling & encoding
│   ├── 05_ml_modeling.ipynb       # Phase 5: Model training, evaluation & serialization
│   └── HR_Job_Placement_Dataset.csv # Raw dataset (50,000+ candidate records)
│
├── .gitignore                     # Git ignore rules for Python, data, checkpoints & OS files
├── requirements.txt               # Complete project dependencies
└── README.md                      # Comprehensive project documentation
```

---

## 🚀 Quick Start / Local Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/bsasidharan15/job-predict.git
cd job-predict
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Jupyter Notebooks (Sequential Execution)
To retrain or review the analytical pipeline, open the notebooks in order:
```bash
jupyter notebook notebooks/
```
1. `01_data_overview.ipynb`
2. `02_data_cleaning.ipynb`
3. `03_eda_hr_insights.ipynb`
4. `04_feature_engineering.ipynb`
5. `05_ml_modeling.ipynb` *(Generates `best_model.pkl` and `model_features.pkl`)*

### 5. Launch the Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```
Open your browser at `http://localhost:8501`.

### 6. Run Programmatic Model Inference
You can test the trained model directly through Python:
```bash
python models/use_model.py
```

### 7. Setup MySQL Database (Optional)
Execute the script in MySQL workbench or command line:
```bash
mysql -u your_username -p < Db/sql_database_setup.sql
```

---

## 📊 Project Evaluation Rubric

| Component | Weight | Key Criteria Assessed |
| :--- | :---: | :--- |
| **Data Cleaning & EDA Accuracy** | **25%** | Logical consistency checks, handling missing values with domain heuristics, duplicate identification, and statistical rigor in EDA. |
| **Machine Learning** | **45%** | Appropriate classifier selection, class imbalance mitigation, ROC-AUC performance ($0.955$), feature importance interpretability, and business relevance. |
| **Visualization & Dashboard** | **10%** | Interactivity, intuitive layout, clear KPI cards, dynamic probability gauge, and actionable HR recommendations in Streamlit. |
| **Documentation & Communication** | **10%** | Comprehensive documentation, clear problem-to-solution mapping, structured code comments, and professional presentation. |
| **Project Organization & Reproducibility** | **10%** | Clean folder hierarchy, reusable scripts, `.gitignore` discipline, and deterministic pipeline execution. |

---