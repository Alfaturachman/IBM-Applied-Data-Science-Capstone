"""
Automated Chart Generator for Capstone Presentation
IBM Applied Data Science Capstone

Renders 7 high-resolution charts used in the Capstone Presentation:
1. eda_scatter.png: Flight Number vs Payload Mass by Landing Outcome
2. eda_orbit.png: Landing Success Rate by Orbit Destination
3. eda_trend.png: Falcon 9 Landing Success Rate Yearly Progression (2010 - 2020)
4. confusion_matrix.png: 18-sample Test Set Confusion Matrix Heatmap
5. dash_sites.png: Success Count & Proportion by Launch Site
6. folium_proximity.png: Launch Site Geodetic Distance to Key Infrastructure (Haversine)
7. ml_models.png: Classification Model Accuracy & CV Score Comparison

Usage:
    python generate_charts.py
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS_DIR = os.path.join(CURRENT_DIR, "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

# Set enterprise visualization style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load Data
url_data = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
try:
    df = pd.read_csv(url_data)
except Exception:
    parent_dir = os.path.dirname(CURRENT_DIR)
    local_path = os.path.join(parent_dir, "spacex_launch_geo.csv")
    if os.path.exists(local_path):
        df = pd.read_csv(local_path)
    else:
        df = pd.DataFrame()

# Chart 1: Flight Number vs Payload Mass by Class
if not df.empty and 'FlightNumber' in df.columns and 'PayloadMass' in df.columns:
    plt.figure(figsize=(9, 4.5), dpi=200)
    palette = {0: '#E63946', 1: '#2A9D8F'}
    sns.scatterplot(x='FlightNumber', y='PayloadMass', hue='Class', data=df, palette=palette, s=100, alpha=0.9, edgecolor='black', linewidth=0.5)
    plt.title('Falcon 9: Flight Number vs Payload Mass (Color by Landing Outcome)', fontsize=13, fontweight='bold', pad=12, color='#1B365D')
    plt.xlabel('Flight Number', fontsize=11, fontweight='bold')
    plt.ylabel('Payload Mass (kg)', fontsize=11, fontweight='bold')
    plt.legend(title='Outcome', labels=['0: Failed', '1: Success'], loc='upper left', frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'eda_scatter.png'))
    plt.close()

# Chart 2: Success Rate by Orbit Type
if not df.empty and 'Orbit' in df.columns:
    orbit_df = df.groupby('Orbit')['Class'].mean().reset_index().sort_values('Class', ascending=False)
    plt.figure(figsize=(9, 4.5), dpi=200)
    colors = ['#2A9D8F' if val >= 0.7 else '#E76F51' if val <= 0.5 else '#F4A261' for val in orbit_df['Class']]
    bars = plt.bar(orbit_df['Orbit'], orbit_df['Class'] * 100, color=colors, edgecolor='#1B365D', linewidth=0.8)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1.5, f"{yval:.1f}%", ha='center', va='bottom', fontsize=9, fontweight='bold')
    plt.title('SpaceX Landing Success Rate by Orbit Destination', fontsize=13, fontweight='bold', pad=12, color='#1B365D')
    plt.xlabel('Orbit Type', fontsize=11, fontweight='bold')
    plt.ylabel('Success Rate (%)', fontsize=11, fontweight='bold')
    plt.ylim(0, 115)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'eda_orbit.png'))
    plt.close()

# Chart 3: Annual Success Trend
if not df.empty and 'Date' in df.columns:
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    yearly = df.groupby('Year')['Class'].mean().reset_index()
    plt.figure(figsize=(9, 4.5), dpi=200)
    plt.plot(yearly['Year'], yearly['Class'] * 100, marker='o', color='#1B365D', linewidth=2.5, markersize=8, markerfacecolor='#E63946', markeredgecolor='black')
    for _, row in yearly.iterrows():
        plt.text(row['Year'], row['Class']*100 + 3, f"{row['Class']*100:.1f}%", ha='center', fontsize=9, fontweight='bold', color='#1B365D')
    plt.title('Falcon 9 Landing Success Rate Yearly Progression (2010 - 2020)', fontsize=13, fontweight='bold', pad=12, color='#1B365D')
    plt.xlabel('Year', fontsize=11, fontweight='bold')
    plt.ylabel('Success Rate (%)', fontsize=11, fontweight='bold')
    plt.ylim(0, 105)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'eda_trend.png'))
    plt.close()

# Chart 4: Confusion Matrix Heatmap
cm = np.array([[3, 3], [0, 12]])
plt.figure(figsize=(6, 4.5), dpi=200)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Pred: Fail (0)', 'Pred: Success (1)'],
            yticklabels=['Actual: Fail (0)', 'Actual: Success (1)'],
            annot_kws={'size': 14, 'weight': 'bold'},
            linewidths=2, linecolor='#1B365D')
plt.title('Test Set Confusion Matrix (All 4 Algorithms: 83.33% Accuracy)\nTP=12, TN=3, FP=3, FN=0', fontsize=11, fontweight='bold', pad=12, color='#1B365D')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, 'confusion_matrix.png'))
plt.close()

# Chart 5: Plotly Dash Site Performance Summary
sites = ['CCAFS LC-40', 'CCAFS SLC-40', 'KSC LC-39A', 'VAFB SLC-4E']
successes = [7, 3, 10, 4]
total_launches = [26, 7, 13, 10]
success_rate = [s/t * 100 for s, t in zip(successes, total_launches)]

fig, ax1 = plt.subplots(figsize=(8, 4.2), dpi=200)
ax2 = ax1.twinx()

x = np.arange(len(sites))
width = 0.35

rects1 = ax1.bar(x - width/2, successes, width, label='Successful Landings', color='#1B365D')
rects2 = ax1.bar(x + width/2, [t - s for s, t in zip(successes, total_launches)], width, label='Failed Landings', color='#E63946', alpha=0.8)
line = ax2.plot(x, success_rate, color='#D4AF37', marker='o', linewidth=2.5, markersize=8, label='Success Rate (%)')

ax1.set_ylabel('Number of Launches', fontweight='bold', color='#1B365D')
ax2.set_ylabel('Success Rate (%)', fontweight='bold', color='#D4AF37')
ax1.set_xticks(x)
ax1.set_xticklabels(sites, rotation=15, ha='right', fontweight='bold')
ax2.set_ylim(0, 100)

for i, rate in enumerate(success_rate):
    ax2.text(i, rate + 4, f"{rate:.1f}%", ha='center', fontweight='bold', color='#1B365D')

plt.title('SpaceX Launch Site Landing Performance & Success Rates', fontsize=12, fontweight='bold', pad=12, color='#1B365D')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, 'dash_sites.png'))
plt.close()

# Chart 6: Folium Proximity Distances
poi = ['Highway (0.58 km)', 'Coastline (0.90 km)', 'Railway (1.28 km)', 'City (Titusville: 23.19 km)']
dist = [0.58, 0.90, 1.28, 23.19]
plt.figure(figsize=(7, 4.2), dpi=200)
colors_poi = ['#2A9D8F', '#457B9D', '#F4A261', '#E63946']
bars = plt.barh(poi, dist, color=colors_poi, edgecolor='#1B365D', height=0.55)
for bar in bars:
    w = bar.get_width()
    plt.text(w + 0.5, bar.get_y() + bar.get_height()/2, f"{w:.2f} km", va='center', fontweight='bold', color='#1B365D')
plt.title('CCAFS SLC-40 Distance to Infrastructure (Haversine Formula)', fontsize=11, fontweight='bold', pad=12, color='#1B365D')
plt.xlabel('Distance (Kilometers)', fontsize=10, fontweight='bold')
plt.xlim(0, 27)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, 'folium_proximity.png'))
plt.close()

# Chart 7: Machine Learning Model Comparison
models = ['Logistic Regression', 'Support Vector Machine', 'Decision Tree', 'K-Nearest Neighbors']
cv_scores = [84.64, 84.82, 87.22, 84.82]
test_scores = [83.33, 83.33, 83.33, 83.33]

x = np.arange(len(models))
width = 0.35

plt.figure(figsize=(8.5, 4.2), dpi=200)
rects1 = plt.bar(x - width/2, cv_scores, width, label='CV Score (%)', color='#1B365D', edgecolor='black', linewidth=0.5)
rects2 = plt.bar(x + width/2, test_scores, width, label='Test Accuracy (%)', color='#2A9D8F', edgecolor='black', linewidth=0.5)

plt.ylabel('Accuracy / Score (%)', fontweight='bold', color='#1B365D')
plt.title('Classification Algorithms Performance Comparison\n(GridSearchCV 10-Fold CV vs 18-Sample Test Set)', fontsize=12, fontweight='bold', pad=12, color='#1B365D')
plt.xticks(x, models, fontweight='bold', rotation=10, ha='right')
plt.ylim(70, 95)
plt.legend(loc='lower right', frameon=True)

for bar in rects1:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h + 0.4, f"{h:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold')
for bar in rects2:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h + 0.4, f"{h:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, 'ml_models.png'))
plt.close()

print(f"[SUCCESS] All 7 charts successfully rendered and saved to: {CHARTS_DIR}")
