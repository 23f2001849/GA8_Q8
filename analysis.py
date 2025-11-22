import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Analyst Email: 23f2001849@ds.study.iitm.ac.in

def main():
    # 1. Define the Dataset
    data = {
        'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
        'MRR_Growth': [1.34, 8.94, 9.63, 8.24]
    }
    df = pd.DataFrame(data)

    # 2. Calculate Statistics
    current_avg = df['MRR_Growth'].mean()
    target = 15.0
    
    print(f"Analysis Report")
    print(f"---------------")
    print(f"Current Average MRR Growth: {current_avg:.2f}")
    print(f"Industry Target: {target}")
    print(f"Gap to Target: {target - current_avg:.2f}")

    # 3. Generate Visualization
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")

    # Plot Actual Performance
    plt.plot(df['Quarter'], df['MRR_Growth'], marker='o', linewidth=2.5, label='Actual Growth', color='#2c3e50')
    
    # Plot Industry Target
    plt.axhline(y=target, color='#e74c3c', linestyle='--', linewidth=2, label=f'Industry Target ({target})')
    
    # Add Average Line
    plt.axhline(y=current_avg, color='#27ae60', linestyle=':', linewidth=2, label=f'2024 Avg ({current_avg:.2f})')

    # Formatting
    plt.title('2024 SaaS MRR Growth vs Industry Target', fontsize=14, pad=20)
    plt.ylabel('MRR Growth (%)', fontsize=12)
    plt.xlabel('Quarter (2024)', fontsize=12)
    plt.ylim(0, 18)
    plt.legend(loc='upper left')
    
    # Annotate values
    for x, y in zip(df['Quarter'], df['MRR_Growth']):
        plt.text(x, y + 0.5, f'{y}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('mrr_growth_chart.png', dpi=150)
    print("Chart saved as 'mrr_growth_chart.png'")

if __name__ == "__main__":
    main()