# RFM Customer Segmentation & Retention Strategy

## Project Overview

This project evaluates transactional customer behavior using **RFM (Recency, Frequency, Monetary) analysis** on an international e-commerce dataset.

The objective is to understand customer purchasing behavior, identify different customer lifecycle segments, highlight retention opportunities, and develop targeted business strategies that can support customer engagement and revenue growth.

The end-to-end workflow combines **Python** for data cleaning, transformation and RFM scoring with **Power BI** for interactive dashboard reporting and business insight generation.

---

## Business Questions

* Who are the highest-value customers?
* Which customers show signs of reduced engagement or potential churn?
* Which customer groups have opportunities for increased engagement and loyalty?
* How can customer segments be matched with appropriate retention strategies?
* How can customer transaction data be converted into actionable business insights?

---

## Dataset

The project uses the **Online Retail** transactional dataset containing e-commerce purchase records.

Key attributes include:

* `InvoiceNo` — Transaction identifier
* `StockCode` — Unique product identifier
* `Description` — Product description
* `Quantity` — Number of units purchased
* `InvoiceDate` — Transaction date and time
* `UnitPrice` — Product price in GBP (£)
* `CustomerID` — Unique customer identifier
* `Country` — Customer country

---

## Data Preparation & Cleaning

Data preprocessing was performed in Python using **pandas**.

The cleaning process included:

* Removing duplicate transaction records
* Removing transactions without a `CustomerID`
* Excluding cancelled transactions
* Removing invalid or negative quantities
* Removing invalid or zero-priced transactions
* Creating a `TotalPrice` feature using:

`TotalPrice = Quantity × UnitPrice`

After cleaning, the dataset contained:

**392,692 valid transactions**

The analysis was performed across:

**4,338 unique customers**

---

## RFM Methodology

RFM analysis was used to evaluate customer purchasing behavior across three dimensions.

### Recency

Measures how recently a customer made a purchase.

A lower recency value indicates a more recent purchase.

### Frequency

Measures how frequently a customer made purchases.

A higher frequency indicates more repeat purchasing activity.

### Monetary

Measures the total amount spent by a customer.

A higher monetary value indicates greater customer value based on historical spending.

Customer-level RFM scores were calculated and used to classify customers into behavioral segments.

---

## Customer Segments

The analysis identifies customer groups including:

### Champions

Customers demonstrating strong recent purchasing activity, frequency and monetary value.

### Loyal Customers

Customers with established purchasing relationships and consistent engagement.

### Potential Loyalists

Customers showing characteristics that provide an opportunity to increase purchasing frequency and strengthen loyalty.

### At Risk

Customers with previous purchasing activity but longer periods since their last purchase, making them candidates for re-engagement.

### Need Attention

Customers whose engagement may require timely intervention to prevent further inactivity.

---

## Key Performance Findings

* **4,338 customers** were analyzed.
* **392,692 valid transactions** remained after data cleaning.
* Approximately **£8.90 million** in transaction revenue was analyzed.
* Average customer monetary value was approximately **£2,048.69**.
* **464 customers** were classified as Champions.
* The customer base contains multiple behavioral segments with different retention and engagement requirements.
* At Risk and Need Attention customers represent an important retention opportunity because of their longer periods since their most recent purchases.
* Potential Loyalists provide an opportunity to increase purchase frequency through targeted engagement and personalised offers.

These findings form the basis for the business recommendations presented in the Power BI dashboard.

---

## Strategic Business Recommendations

| Customer Segment        | Objective                   | Recommended Action                                                                                                 |
| ----------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Champions**           | Retain high-value customers | Strengthen loyalty through exclusive offers, early access, personalised communication and recognition programmes.  |
| **Loyal Customers**     | Increase customer value     | Use personalised product recommendations, cross-selling and loyalty incentives to encourage continued purchasing.  |
| **Potential Loyalists** | Increase purchase frequency | Use targeted promotions, personalised recommendations and follow-up campaigns to encourage repeat purchases.       |
| **At Risk**             | Reactivate customers        | Launch targeted re-engagement campaigns using personalised offers, reminders and relevant product recommendations. |
| **Need Attention**      | Prevent further inactivity  | Use timely communication, targeted incentives and customer feedback initiatives to encourage customers to return.  |

---

## Dashboard

The Power BI dashboard presents the results of the RFM analysis through interactive visualisations and KPI reporting.

The dashboard includes:

* Total Customers
* Total Revenue
* Average Customer Value
* Champions
* Customer segmentation
* RFM-based customer insights
* Business recommendations
* Customer retention opportunities

The dashboard is designed to translate technical analysis into information that can support business decision-making.

---

## Technical Workflow

The project follows an end-to-end analytical workflow:

```text
Raw Transaction Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Customer-Level Aggregation
        ↓
RFM Calculation
        ↓
Customer Segmentation
        ↓
Python Analysis
        ↓
Power BI Dashboard
        ↓
Business Insights & Recommendations
```

---

## Technology Stack

### Python

Used for:

* Data cleaning
* Data validation
* Feature engineering
* Customer-level aggregation
* RFM calculation
* Customer segmentation
* CSV output

Main libraries include:

* pandas
* numpy
* datetime

### Power BI

Used for:

* Data modelling
* KPI development
* DAX measures
* Interactive visualisation
* Customer segmentation analysis
* Business insights
* Strategic recommendations

### Excel

Used for initial dataset inspection and data understanding.

### VS Code

Used as the development environment for the Python analysis.

---

## Project Structure

The project contains the following key files:

```text
SyntecxHub_RFM_Project/
│
├── rfm_analysis.py
├── rfm_customer_segments.csv
├── rfm_segment_summary.csv
├── README.md
└── Power BI Dashboard
```

---

## Business Value

This project demonstrates how customer transaction data can be transformed into actionable business intelligence.

RFM segmentation allows businesses to move beyond simply reporting historical sales and instead understand **who their customers are, how recently they purchased, how frequently they purchase, and how much they spend**.

The resulting customer segments can be used to support:

* Customer retention
* Customer reactivation
* Loyalty programmes
* Personalised marketing
* Cross-selling
* Customer engagement
* Revenue-focused decision-making

---

## Conclusion

This project demonstrates an end-to-end approach to customer analytics using **Python, RFM segmentation and Power BI**.

The analysis transforms raw transactional data into customer-level behavioral insights by applying data cleaning, feature engineering, RFM scoring and customer segmentation.

The Power BI dashboard then communicates these findings through KPIs, visual analysis and targeted business recommendations.

Overall, the project demonstrates how a data analyst can combine **technical data preparation, analytical modelling, visualisation and business thinking** to turn customer transaction data into practical insights that can support retention, engagement and revenue-focused decision-making.
