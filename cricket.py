import pandas as pd

df =  pd.read_csv("data.csv")

print("==== columns ====")
print(df.head())

print("\n datasheet info")
print(df.info())

print("\n==== team-wise total runs====")
print(df.groupby("batting_team")["total_runs"].sum())

print("\n team-wise Highest score")
print(df.groupby("batting_team")["total_runs"].max())


print("\n team-wise Lowest score")
print(df.groupby("batting_team")["total_runs"].min())

print("\n team-wise number of players")
print(df.groupby("batting_team").size())

print("\n runs aggregation")
print(df.groupby("batting_team")["total_runs"].agg(["sum", "mean", "max", "min", "count"]))

print("\n custom aggregation")
result = df.groupby("batting_team").agg(
    total_runs=("total_runs", "sum"),
    average_runs=("total_runs", "mean"),
    Highest_runs=("total_runs", "max"),
    total_wickets=("total_runs", "sum"),
)
print(result)