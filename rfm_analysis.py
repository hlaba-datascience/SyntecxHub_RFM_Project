import pandas as pd

# Load the dataset
file_path = "data/Online Retail.xlsx"
df = pd.read_excel(file_path)

# Display basic information
print("Original dataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicate transactions
df = df.drop_duplicates()

# Remove transactions with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove transactions with invalid quantities
df = df[df["Quantity"] > 0]

# Remove transactions with invalid prices
df = df[df["UnitPrice"] > 0]

# Create total transaction value
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Display results after cleaning
print("\nAfter cleaning:")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing values:")
print(df.isnull().sum())

print("\nCleaned data preview:")
print(df.head())

# -----------------------------
# RFM ANALYSIS
# -----------------------------

# Set the analysis date to one day after the last transaction
analysis_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Calculate RFM metrics for each customer
rfm = df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (analysis_date - x.max()).days),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("TotalPrice", "sum")
).reset_index()

# Display the RFM results
print("\nRFM Analysis:")
print(rfm.head())

print("\nNumber of customers:", len(rfm))

print("\nRFM summary:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe())

# -----------------------------
# RFM SCORING
# -----------------------------

# Score each customer from 1 to 5
# Recency: lower is better
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    5,
    labels=[5, 4, 3, 2, 1]
).astype(int)

# Frequency: higher is better
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

# Monetary: higher is better
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

# Calculate overall RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"] +
    rfm["F_Score"] +
    rfm["M_Score"]
)

print("\nRFM Scores:")
print(rfm.head(10))

print("\nRFM Score distribution:")
print(rfm["RFM_Score"].value_counts().sort_index())

# -----------------------------
# CUSTOMER SEGMENTATION
# -----------------------------

def segment_customer(row):
    score = row["RFM_Score"]

    if score >= 13:
        return "Champions"
    elif score >= 10:
        return "Loyal Customers"
    elif score >= 8:
        return "Potential Loyalists"
    elif score >= 6:
        return "At Risk"
    else:
        return "Need Attention"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)

# Display sample results
print("\nCustomer Segments:")
print(rfm.head(10))

# Count customers in each segment
print("\nSegment Distribution:")
print(rfm["Segment"].value_counts())

# Calculate segment-level business metrics
segment_summary = rfm.groupby("Segment").agg(
    Customers=("CustomerID", "count"),
    Avg_Recency=("Recency", "mean"),
    Avg_Frequency=("Frequency", "mean"),
    Avg_Monetary=("Monetary", "mean"),
    Total_Revenue=("Monetary", "sum")
).reset_index()

print("\nSegment Summary:")
print(segment_summary)

# -----------------------------
# EXPORT FINAL RFM DATA
# -----------------------------

# Save customer-level RFM analysis
rfm.to_csv("rfm_customer_segments.csv", index=False)

# Save segment summary
segment_summary.to_csv("rfm_segment_summary.csv", index=False)

print("\nFiles exported successfully:")
print("1. rfm_customer_segments.csv")
print("2. rfm_segment_summary.csv")