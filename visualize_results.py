#!/usr/bin/env python3
"""
Visualize AI Coach POC Results
Generates charts and analysis from coaching interaction logs.
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import sys
from pathlib import Path

def load_coaching_interactions(filepath='outputs/coaching_interactions.jsonl'):
    """Load coaching interaction logs."""
    interactions = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                interactions.append(json.loads(line))
    except FileNotFoundError:
        print(f"❌ No interactions found at {filepath}")
        print("   Run the main program first to generate data.")
        sys.exit(1)
    
    return pd.DataFrame(interactions)

def plot_acceptance_rates(df):
    """Plot nudge acceptance rates by persona and type."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # By persona
    persona_acceptance = df.groupby('persona').apply(
        lambda x: (x['outcome'].apply(lambda o: o['accepted']).sum() / len(x)) * 100
    )
    persona_acceptance.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.axhline(y=65, color='r', linestyle='--', label='Target (65%)')
    ax1.set_title('Acceptance Rate by Persona')
    ax1.set_ylabel('Acceptance Rate (%)')
    ax1.set_xlabel('Persona Type')
    ax1.legend()
    ax1.set_ylim(0, 100)
    
    # By nudge type
    nudge_acceptance = df.groupby(df['nudge'].apply(lambda x: x['nudge_type'])).apply(
        lambda x: (x['outcome'].apply(lambda o: o['accepted']).sum() / len(x)) * 100
    )
    nudge_acceptance.plot(kind='bar', ax=ax2, color='lightgreen')
    ax2.axhline(y=65, color='r', linestyle='--', label='Target (65%)')
    ax2.set_title('Acceptance Rate by Nudge Type')
    ax2.set_ylabel('Acceptance Rate (%)')
    ax2.set_xlabel('Nudge Type')
    ax2.legend()
    ax2.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.savefig('outputs/acceptance_rates.png', dpi=300)
    print("📊 Saved acceptance rates chart to outputs/acceptance_rates.png")

def plot_productivity_impact(df):
    """Plot productivity and satisfaction impacts."""
    # Filter accepted nudges
    accepted_df = df[df['outcome'].apply(lambda x: x['accepted'])]
    
    if len(accepted_df) == 0:
        print("⚠️  No accepted nudges to analyze")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Extract impacts
    productivity_impacts = accepted_df['outcome'].apply(lambda x: x['productivity_impact'] * 100)
    satisfaction_impacts = accepted_df['outcome'].apply(lambda x: x['satisfaction_impact'] * 100)
    
    # Create box plots
    data = pd.DataFrame({
        'Productivity Lift (%)': productivity_impacts,
        'Satisfaction Lift (%)': satisfaction_impacts
    })
    
    data.boxplot(ax=ax)
    ax.axhline(y=12, color='r', linestyle='--', label='Productivity Target (12%)')
    ax.set_title('Impact Distribution for Accepted Nudges')
    ax.set_ylabel('Percentage Lift')
    ax.legend()
    
    # Add mean values
    for i, col in enumerate(data.columns):
        mean_val = data[col].mean()
        ax.text(i+1, mean_val, f'μ={mean_val:.1f}%', 
                horizontalalignment='center', color='blue', weight='bold')
    
    plt.tight_layout()
    plt.savefig('outputs/productivity_impact.png', dpi=300)
    print("📊 Saved productivity impact chart to outputs/productivity_impact.png")

def plot_effectiveness_timeline(df):
    """Plot effectiveness score over time."""
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    
    # Add hour of day
    df['hour'] = df['timestamp'].dt.hour
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot effectiveness score over time
    ax.plot(range(len(df)), df['effectiveness_score'], alpha=0.6, label='Individual Scores')
    
    # Add rolling average
    window_size = min(20, len(df) // 4)
    if window_size > 1:
        rolling_avg = df['effectiveness_score'].rolling(window=window_size).mean()
        ax.plot(range(len(df)), rolling_avg, color='red', linewidth=2, 
                label=f'{window_size}-nudge Rolling Average')
    
    ax.set_xlabel('Nudge Sequence')
    ax.set_ylabel('Effectiveness Score')
    ax.set_title('Coaching Effectiveness Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/effectiveness_timeline.png', dpi=300)
    print("📊 Saved effectiveness timeline to outputs/effectiveness_timeline.png")

def generate_summary_report(df):
    """Generate a text summary report."""
    total_nudges = len(df)
    accepted_nudges = df['outcome'].apply(lambda x: x['accepted']).sum()
    acceptance_rate = (accepted_nudges / total_nudges) * 100 if total_nudges > 0 else 0
    
    # Calculate average impacts for accepted nudges
    accepted_df = df[df['outcome'].apply(lambda x: x['accepted'])]
    avg_productivity = 0
    avg_satisfaction = 0
    
    if len(accepted_df) > 0:
        avg_productivity = accepted_df['outcome'].apply(
            lambda x: x['productivity_impact']
        ).mean() * 100
        avg_satisfaction = accepted_df['outcome'].apply(
            lambda x: x['satisfaction_impact']
        ).mean() * 100
    
    # Calculate ROI
    total_productivity_lift = accepted_df['outcome'].apply(
        lambda x: x['productivity_impact']
    ).sum() if len(accepted_df) > 0 else 0
    
    simulated_roi = total_productivity_lift * 50 * 40 * 83 * 13
    
    report = f"""
AI COACH POC RESULTS SUMMARY
============================

Total Nudges Generated: {total_nudges}
Nudges Accepted: {accepted_nudges}
Overall Acceptance Rate: {acceptance_rate:.1f}% {'✅' if acceptance_rate > 65 else '❌'} (Target: >65%)

Average Productivity Lift: {avg_productivity:.1f}% {'✅' if avg_productivity > 12 else '❌'} (Target: >12%)
Average Satisfaction Lift: {avg_satisfaction:.1f}%

Simulated Quarterly ROI: ${simulated_roi:,.0f}

NUDGE TYPE DISTRIBUTION
----------------------
"""
    
    # Add nudge type breakdown
    nudge_types = df['nudge'].apply(lambda x: x['nudge_type']).value_counts()
    for ntype, count in nudge_types.items():
        report += f"{ntype}: {count} ({count/total_nudges*100:.1f}%)\n"
    
    report += "\nPERSONA BREAKDOWN\n"
    report += "-----------------\n"
    
    # Add persona breakdown
    personas = df['persona'].value_counts()
    for persona, count in personas.items():
        persona_df = df[df['persona'] == persona]
        persona_acceptance = persona_df['outcome'].apply(
            lambda x: x['accepted']
        ).sum() / len(persona_df) * 100
        report += f"{persona}: {count} nudges, {persona_acceptance:.1f}% acceptance\n"
    
    # Save report
    with open('outputs/summary_report.txt', 'w') as f:
        f.write(report)
    
    print("📄 Summary Report:")
    print(report)
    print("\n📄 Full report saved to outputs/summary_report.txt")

def main():
    """Main visualization function."""
    print("📊 AI Coach Results Visualizer")
    print("==============================\n")
    
    # Load data
    df = load_coaching_interactions()
    print(f"✅ Loaded {len(df)} coaching interactions\n")
    
    # Generate visualizations
    if len(df) > 0:
        plot_acceptance_rates(df)
        plot_productivity_impact(df)
        plot_effectiveness_timeline(df)
        generate_summary_report(df)
        
        print("\n✨ All visualizations complete!")
        print("   Check the outputs/ directory for:")
        print("   - acceptance_rates.png")
        print("   - productivity_impact.png")
        print("   - effectiveness_timeline.png")
        print("   - summary_report.txt")
    else:
        print("❌ No data to visualize. Run the main program first.")

if __name__ == "__main__":
    # Set style
    sns.set_style("whitegrid")
    plt.rcParams['figure.dpi'] = 100
    
    main()