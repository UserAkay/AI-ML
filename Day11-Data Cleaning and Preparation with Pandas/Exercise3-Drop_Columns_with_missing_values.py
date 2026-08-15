import pandas as pd

def drop_high_missing_columns(df, threshold=0.5):
    """
    Drop columns with more than `threshold` fraction of missing values.
    """
    missing_frac = df.isnull().mean()
    cols_to_drop = missing_frac[missing_frac > threshold].index
    print(f"Dropping {len(cols_to_drop)} columns: {list(cols_to_drop)}")
    return df.drop(columns=cols_to_drop)

if __name__ == "__main__":
    df = pd.read_csv("your_file.csv")
    cleaned_df = drop_high_missing_columns(df, threshold=0.5)
    cleaned_df.to_csv("cleaned_file.csv", index=False)
    print(f"Original shape: {df.shape}, Cleaned shape: {cleaned_df.shape}")