import pandas as pd

skills = pd.read_csv("data/archive/job_skills.csv")
jobs = pd.read_csv("data/archive/linkedin_job_postings.csv")

# Join to get job context
df = skills.merge(jobs, on="job_link")

data_keywords = ["data", "analyst", "data engineer", "data scientist", "ml", "machine learning", "software engineer", "developer"]
exclude_keywords = ["electrical", "mechanical", "civil", "chemical"]
mask = df["job_title"].str.lower().apply(
    lambda t: any(kw in t for kw in data_keywords) and not any(ex in t for ex in exclude_keywords)
)   
df = df[mask]
print(f"Data-related postings: {len(df)}")

# Extract skills
df["skills_list"] = df["job_skills"].str.split(", ")
df_long = df.explode("skills_list")
df_long["skills_list"] = df_long["skills_list"].str.strip().str.lower()
skill_counts = df_long["skills_list"].value_counts()

# Gap report
my_skills = {"python", "sql", "pandas", "tableau"}
market_top = set(skill_counts.head(20).index)
missing = market_top - my_skills

print(f"\nTop 20 data-role skills you're missing: {sorted(missing)}")
print(f"\nTop 20 overall (data roles):")
print(skill_counts.head(20))   
