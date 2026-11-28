
# ============================================================
# PROJECT TITLE: RAILWAY_GUAGES
# Project: Railway Gauges Data Analysis
# Description: Analysis of Broad, Metre and Narrow Gauge
# ============================================================

#=============================================================

# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# =============================================================================
# SCENARIO 1: BASIC DATA LOADING & CLEANING
# =============================================================================
'''�� Tasks:
1. Load the dataset into a Pandas DataFrame.
2. Display the first 5 rows and column names.
3. Check for missing values and replace them with 0.
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.'''

#===============================================================================

print("\n========================================")
print("SCENARIO 1: BASIC DATA LOADING & CLEANING")
print("=========================================")

# Load the CSV file
df = pd.read_csv("railway_gauges.csv")

# Define gauge columns
gauge_columns = [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge",
    "Total"
]

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Replace missing values with 0
df[gauge_columns] = df[gauge_columns].fillna(0)

# Convert gauge columns into numeric data types
for column in gauge_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)

# Check data types
print("\nUpdated Data Types:")
print(df.dtypes)

# Final dataset
print("\nCleaned Dataset:")
print(df.head())


# ============================================================
# SCENARIO 2: SIMPLE VISUALIZATION
# TOTAL RAILWAY TRACK GROWTH
# ============================================================
'''�� Tasks:
1. Extract Year and Total columns.
2. Plot a line graph showing Total tracks over years.
3. Add:
○ Title
○ X and Y labels
4. Identify whether the trend is increasing or decreasing'''
#==============================================================

print("\n======================================")
print("SCENARIO 2: SIMPLE VISUALIZATION")
print("======================================")

# Extract Year and Total columns
total_tracks = df[["Year", "Total"]].copy()

# Display extracted data
print("\nYear and Total Tracks:")
print(total_tracks)

# Plot line graph
plt.figure(figsize=(10, 4))

plt.plot(
    total_tracks["Year"],
    total_tracks["Total"],
    marker="o",
    linestyle="-",
    label="Total Railway Tracks"
)

# Add title and labels
plt.title("Total Railway Track Growth Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Railway Tracks")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)

plt.tight_layout()

# Save graph
plt.savefig("graphs/scenario_2_total_growth.png")

# Display graph
plt.show()

# Identify trend
first_value = total_tracks["Total"].iloc[0]
last_value = total_tracks["Total"].iloc[-1]

if last_value > first_value:
    print("\n Railway network is increasing.")

elif last_value < first_value:
    print("\n Railway network is decreasing.")

else:
    print("\n Railway network remains unchanged.")

print("Starting Total:", first_value)
print("Ending Total:", last_value)


# ============================================================
# SCENARIO 3: FILTERING + BAR CHART
# MODERN RAILWAY EXPANSION
# ============================================================
'''�� Tasks:
1. Filter the dataset for years after 2000.
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
3. Plot a grouped bar chart comparing all three gauges.
4. Add legend and proper labels.
5. Identify which gauge dominates in recent years.'''
#=============================================================

print("\n======================================")
print("SCENARIO 3: FILTERING + BAR CHART")
print("======================================")

# Extract starting year from Year column
df["Start_Year"] = (
    df["Year"].astype(str).str[:4].astype(int)
)

# Filter data for years after 2000
modern_data = df[df["Start_Year"] > 2000].copy()

# Select required gauge columns
modern_gauges = modern_data[
    ["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]
]

print("\nRailway Data After 2000:")
print(modern_gauges)

# Create grouped bar chart
modern_gauges.set_index("Year").plot(
    kind="bar",
    figsize=(12, 5),
    width=0.8
)

# Add title and labels
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Railway Track Measurement")

plt.xticks(rotation=45)

plt.legend(title="Gauge Types")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save graph
plt.savefig("graphs/scenario_3_gauge_comparison.png")

# Display graph
plt.show()

# Calculate average gauge values
gauge_averages = modern_gauges[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].mean()

print("\nAverage Gauge Values After 2000:")
print(gauge_averages)

# Identify dominant gauge
dominant_gauge = gauge_averages.idxmax()
print("\nDominant Gauge After 2000:", dominant_gauge)



# ============================================================
# SCENARIO 4: FEATURE ENGINEERING + PIE CHART
# GAUGE CONTRIBUTION ANALYSIS
# ============================================================
'''�� Tasks:
1. Calculate total sum of each gauge across all years.
2. Create a new structure (Series/DataFrame) for totals.
3. Plot a pie chart showing percentage contribution.
4. Add percentage labels (autopct).
5. Interpret which gauge contributes the most.'''
#=============================================================
print("\n======================================")
print("SCENARIO 4: GAUGE CONTRIBUTION ANALYSIS")
print("======================================")

# Calculate total sum of each gauge
gauge_totals = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

# Create a Pandas Series
gauge_contribution = pd.Series(gauge_totals)

print("\nTotal Contribution of Each Gauge:")
print(gauge_contribution)

# Calculate percentage contribution
total_gauge_sum = gauge_contribution.sum()
gauge_percentage = (
    gauge_contribution / total_gauge_sum
) * 100

print("\nPercentage Contribution:")
print(gauge_percentage.round(2))

# Create pie chart
plt.figure(figsize=(9, 7))

plt.pie(
    gauge_contribution,
    labels=gauge_contribution.index,
    autopct="%1.2f%%",
    startangle=90,
    explode=(0.05, 0, 0)
)

plt.title("Percentage Contribution of Railway Gauges")
plt.tight_layout()

# Save graph
plt.savefig("graphs/scenario_4_gauge_contribution.png")

# Display graph
plt.show()

# Identify highest contributor
highest_gauge = gauge_contribution.idxmax()
highest_percentage = gauge_percentage.max()

print("\nHighest Contributing Gauge:", highest_gauge)
print("Percentage Contribution:", round(highest_percentage, 2), "%")


# ================================================================
# SCENARIO 5: ADVANCED ANALYSIS
# RAILWAY GAUGE TRENDS AND COMPOSITION
# =================================================================
'''�� Tasks:
1. Create new columns:
○ % Broad Gauge
○ % Metre Gauge
○ % Narrow Gauge
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks.
3. Plot:
○ Line graph for all gauges
○ Stacked bar chart showing composition
4. Highlight:
○ Years with highest growth
○ Decline in any gauge
5. Provide a final conclusion:
�� “Is the railway system shifting towards a single dominant gauge?'''

#=====================================================================
print("\n======================================")
print("SCENARIO 5: ADVANCED RAILWAY ANALYSIS")
print("======================================")

# ------------------------------------------------------------
# STEP 1: FEATURE ENGINEERING
# CALCULATE GAUGE PERCENTAGES
# ------------------------------------------------------------

# Calculate percentage of Broad Gauge

df["% Broad Gauge"] = (
    df["Broad Gauge"] / df["Total"]
) * 100

# Calculate percentage of Metre Gauge

df["% Metre Gauge"] = (
    df["Metre Gauge"] / df["Total"]
) * 100

# Calculate percentage of Narrow Gauge

df["% Narrow Gauge"] = (
    df["Narrow Gauge"] / df["Total"]
) * 100

print("\nGauge Percentage Contribution:")
print(
    df[
        ["Year", "% Broad Gauge",
         "% Metre Gauge", "% Narrow Gauge"]
    ].round(2)
)

# ------------------------------------------------------------
# STEP 2: YEARLY GROWTH USING NUMPY
# ------------------------------------------------------------

# Calculate difference between consecutive years

yearly_growth = np.diff(df["Total"].values)
yearly_growth = yearly_growth.astype(float)

# Add NaN for the first year because
# no previous year is available for comparison

df["Yearly Growth"] = np.insert(
    yearly_growth, 0, np.nan
)

print("\nYearly Growth of Total Railway Tracks:")
print(df[["Year", "Total", "Yearly Growth"]])

# Identify highest growth

highest_growth_index = df["Yearly Growth"].idxmax()

highest_growth_year = df.loc[
    highest_growth_index, "Year"
]

highest_growth_value = df.loc[
    highest_growth_index, "Yearly Growth"
]

print("\nHighest Growth Year:", highest_growth_year)

print("Highest Growth Value:", highest_growth_value)

# ------------------------------------------------------------
# STEP 3: LINE GRAPH FOR ALL GAUGE TYPES
# ------------------------------------------------------------

plt.figure(figsize=(12, 5))

plt.plot(
    df["Year"],
    df["Broad Gauge"],
    marker="o",
    label="Broad Gauge"
)

plt.plot(
    df["Year"],
    df["Metre Gauge"],
    marker="o",
    label="Metre Gauge"
)

plt.plot(
    df["Year"],
    df["Narrow Gauge"],
    marker="o",
    label="Narrow Gauge"
)

plt.title("Railway Gauge Trends Over the Years")

plt.xlabel("Year")

plt.ylabel("Gauge Measurement")

plt.xticks(rotation=90)

plt.legend()

plt.grid(True)

plt.tight_layout()

# Save line graph

plt.savefig("graphs/scenario_5_gauge_trends.png")

plt.show()

# ------------------------------------------------------------
# STEP 4: STACKED BAR CHART
# ------------------------------------------------------------

plt.figure(figsize=(12, 5))

plt.bar(
    df["Year"],
    df["Broad Gauge"],
    label="Broad Gauge"
)

plt.bar(
    df["Year"],
    df["Metre Gauge"],
    bottom=df["Broad Gauge"],
    label="Metre Gauge"
)

plt.bar(
    df["Year"],
    df["Narrow Gauge"],
    bottom=(
        df["Broad Gauge"] + df["Metre Gauge"]
    ),
    label="Narrow Gauge"
)

plt.title("Railway Gauge Composition Over the Years")

plt.xlabel("Year")

plt.ylabel("Gauge Measurement")

plt.xticks(rotation=90)

plt.legend()

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save stacked bar chart

plt.savefig("graphs/scenario_5_stacked_composition.png")

plt.show()

# ------------------------------------------------------------
# STEP 5: IDENTIFY GAUGES WITH DECLINING TRENDS
# ------------------------------------------------------------

print("\nGauge Trend Analysis:")

for column in [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge"
]:

    starting_value = df[column].iloc[0]

    ending_value = df[column].iloc[-1]

    change = ending_value - starting_value

    print("\nGauge:", column)

    print("Starting Value:", starting_value)

    print("Ending Value:", ending_value)
    print("Overall Change:", change)

    if change > 0:
        print("Trend: Increasing")

    elif change < 0:
        print("Trend: Decreasing")

    else:
        print("Trend: No Change")

# ------------------------------------------------------------
# STEP 6: FINAL CONCLUSION
# ------------------------------------------------------------

print("\n======================================")
print("FINAL PROJECT CONCLUSION")
print("======================================")

# Compare gauge percentages in first and last years
first_broad = df["% Broad Gauge"].iloc[0]

last_broad = df["% Broad Gauge"].iloc[-1]

first_metre = df["% Metre Gauge"].iloc[0]

last_metre = df["% Metre Gauge"].iloc[-1]

first_narrow = df["% Narrow Gauge"].iloc[0]

last_narrow = df["% Narrow Gauge"].iloc[-1]

print("\nBroad Gauge Percentage Change:",
      round(last_broad - first_broad, 2), "%")
print("Metre Gauge Percentage Change:",
      round(last_metre - first_metre, 2), "%")
print("Narrow Gauge Percentage Change:",
      round(last_narrow - first_narrow, 2), "%")

if last_broad > first_broad:
    print(
        "\nConclusion: The railway system shows "
        "a shift towards Broad Gauge dominance."
    )

else:
    print(
        "\nConclusion: Broad Gauge percentage "
        "has not increased over the analyzed period."
    )

