import pandas as pd

df = pd.read_csv("s3_bucket_files.csv")
df = df.drop("Size (bytes)", axis=1)
df = df.rename(columns={
    "Key": "File Name"
})
df["File Pattern"] = df['File Name'].str.split('_',n=1).str[1]
df["File Type"] = df["File Name"].str.split(".",n=1).str[1]
output_csv = 'output_files.csv'
df.to_csv(output_csv, index=False)