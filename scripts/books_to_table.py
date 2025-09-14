import pandas as pd

df = pd.read_csv("books.csv")
df = df[["Title", "Authors", "Date Added"]]

md_table = df.to_markdown(index=False)

with open ("books.md", "w") as f:
    f.write(md_table)

