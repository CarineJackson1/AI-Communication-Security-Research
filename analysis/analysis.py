import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Resolve data path relative to this script file so cwd doesn't matter
HERE = Path(__file__).resolve().parent
DATA_PATH = (HERE.parent / 'data' / 'testing_results.csv')

# Load testing results
df = pd.read_csv(DATA_PATH)

# Analysis Example 1: Response Quality by AI Tool
print("Average Response Quality by AI Tool:")
print(df.groupby('AI_Tool')['Response_Quality'].mean().sort_values(ascending=False))

# Analysis Example 2: Safety Maintained
print("\nSafety Maintained Across Tests:")
print(df['Safety_Maintained'].value_counts())

# Analysis Example 3: Jailbreak Risk by Communication Pattern
print("\nJailbreak Risk by Communication Pattern:")
print(df.groupby('Communication_Pattern')['Jailbreak_Risk'].value_counts())

# Visualization Example: Heatmap
pivot = df.pivot_table(
    values='Response_Quality', 
    index='Communication_Pattern', 
    columns='AI_Tool', 
    aggfunc='mean'
)

sns.heatmap(pivot, annot=True, cmap='RdYlGn', vmin=1, vmax=5)
plt.title('Response Quality: AI Tools × Communication Patterns')
plt.tight_layout()
# Save visualization next to this script
OUT_PATH = HERE / 'quality_heatmap.png'
plt.savefig(OUT_PATH, dpi=300)
plt.close()

print("\nAnalysis complete. Check visualizations in this folder.")
