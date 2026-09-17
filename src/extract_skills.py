import pandas as pd

df = pd.read_csv("data/archive/job_skills.csv")

# Split into lists (no strip here)
df["skills_list"] = df["job_skills"].str.split(", ")

# Explode first, then strip the individual strings
df_long = df.explode("skills_list")
df_long["skills_list"] = df_long["skills_list"].str.strip().str.lower()   

skill_counts = df_long["skills_list"].value_counts()

target_stack = ["python", "sql", "airflow", "snowflake", "dbt", "pandas", "tableau"]   
gap = skill_counts.reindex(target_stack, fill_value=0)

print("=== Target Stack Frequency ===")
print(gap.sort_values(ascending=False))
print(f"\nTotal unique skills found: {len(skill_counts)}")
print(f"\nTop 10 skills overall:")
print(skill_counts.head(10))   
