import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/archive/job_skills.csv")
df["skills_list"] = df["job_skills"].str.split(", ")
df_long = df.explode("skills_list")
df_long["skills_list"] = df_long["skills_list"].str.strip().str.lower()
skill_counts = df_long["skills_list"].value_counts()

target_stack = ["python", "sql", "tableau", "snowflake", "dbt", "airflow", "pandas"]
gap = skill_counts.reindex(target_stack).sort_values()

plt.figure(figsize=(8, 4))
plt.barh(gap.index, gap.values, color="#4C72B0")
plt.xlabel("Number of job postings")
plt.title("Target Stack Frequency (1.3M LinkedIn Job Postings)")
plt.tight_layout()
plt.savefig("skill_gap_chart.png", dpi=150)
print("Chart saved as skill_gap_chart.png")   
