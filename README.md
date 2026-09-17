# Skill Gap Analyzer

**Problem:** Job postings demand specific tools. This project analyzes 1.3M LinkedIn job postings to identify which technical skills are most in-demand, and highlights gaps relative to a target skill set.

## Data

Uses the [LinkedIn Jobs & Skills (2024)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024) dataset (~1.3M postings).

Download from Kaggle and place the three CSVs in `data/archive/`:
- `linkedin_job_postings.csv`
- `job_skills.csv`
- `job_summary.csv`

## How to Run

```bash
pip install -r requirements.txt

python3 src/extract_skills.py   # Target stack frequency
python3 src/gap_report.py       # Personal gap analysis
python3 src/visualize.py        # Generate bar chart   


Findings

Among 61.8K data-role postings, Python (11.9K) and SQL (13.8K) are the most in-demand technical skills. The highest-impact gaps are AWS (6.3K postings), Excel (5.6K), and data visualization (4.6K).

| Skill | Count | % of postings |
|-------|-------|---------------|
| Python | 25,168 | 1.9% |
| SQL | 22,035 | 1.7% |
| Tableau | 7,027 | 0.5% |
| Snowflake | 1,704 | 0.13% |
| dbt | 610 | 0.05% |
| Airflow | 601 | 0.05% |
| Pandas | 537 | 0.04% |

Key insight: dbt, Airflow, and Pandas appear in fewer than 0.05% of all postings — learning them puts you in a small, differentiated subset of candidates.

Limitations
Skills are extracted as free-text strings; no normalization beyond lowercasing (e.g., "problem solving" and "problemsolving" remain separate).
The data-role filter uses keyword matching on job titles, which may include false positives (e.g., "data entry clerk").
The dataset is a snapshot from January 2024 and may not reflect current market conditions.
