import pandas as pd

df = pd.read_csv("employees.csv")

high_salary = df[df["salary"] > 60000]

print(high_salary)
