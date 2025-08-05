#!/usr/bin/env python3
"""
Massive Dataset Generation for AI Learning
Generates 500,000+ data points for advanced AI coach evolution.
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
from pathlib import Path
import random
import logging
from synthetic_data_generator import SyntheticDataGenerator
import asyncio
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MassiveDatasetGenerator:
    """Optimized generator for creating large-scale datasets efficiently."""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.base_generator = SyntheticDataGenerator(output_dir)
        
    def generate_massive_dataset(self, target_records: int = 500000, batch_size: int = 10000):
        """Generate massive dataset in batches to avoid memory issues."""
        
        print(f"🏭 MASSIVE DATASET GENERATION")
        print(f"Target Records: {target_records:,}")
        print(f"Batch Size: {batch_size:,}")
        print("=" * 60)
        
        # Calculate parameters
        num_users = min(1000, target_records // 100)  # 1 user per 100 records, max 1000 users
        days_needed = max(30, target_records // (num_users * 50))  # Ensure enough days for target
        
        print(f"📊 Dataset Parameters:")
        print(f"   Users: {num_users}")
        print(f"   Days: {days_needed}")
        print(f"   Expected Records: ~{num_users * days_needed * 50:,}")
        print()
        
        # Generate user profiles once
        logger.info(f"Generating {num_users} user profiles...")
        user_profiles = self.base_generator.generate_user_profiles(num_users)
        
        # Save user profiles
        profiles_data = [
            {
                'user_id': int(profile.user_id),
                'persona_type': str(profile.persona_type),
                'productivity_baseline': float(profile.productivity_baseline),
                'focus_tendency': float(profile.focus_tendency),
                'interruption_tolerance': float(profile.interruption_tolerance),
                'tool_proficiency': {k: float(v) for k, v in profile.tool_proficiency.items()},
                'work_schedule': {k: (int(v) if isinstance(v, (int, np.integer)) else v) for k, v in profile.work_schedule.items()},
                'behavioral_patterns': {k: (float(v) if isinstance(v, (float, np.floating)) else v) for k, v in profile.behavioral_patterns.items()}
            }
            for profile in user_profiles
        ]
        
        with open(self.output_dir / 'massive_user_profiles.json', 'w') as f:
            json.dump(profiles_data, f, indent=2)
        
        logger.info(f"✅ Generated {len(user_profiles)} user profiles")
        
        # Generate telemetry data in batches
        all_telemetry = []
        total_generated = 0
        batch_num = 0
        
        print(f"🔄 Generating telemetry data in batches...")
        
        # Calculate batches needed
        records_per_batch = batch_size
        num_batches = (target_records + records_per_batch - 1) // records_per_batch
        
        for batch_idx in range(num_batches):
            batch_num += 1
            batch_start_day = batch_idx * (days_needed // num_batches)
            batch_days = min(days_needed // num_batches + 5, days_needed - batch_start_day)
            
            if batch_days <= 0:
                break
            
            logger.info(f"Batch {batch_num}/{num_batches}: Generating {batch_days} days of data...")
            
            # Generate batch
            batch_data = []
            for day in range(batch_days):
                date = datetime.now() - timedelta(days=batch_start_day + day)
                
                for profile in user_profiles:
                    # Generate multiple records per day per user
                    work_start = profile.work_schedule['start_hour']
                    work_end = profile.work_schedule['end_hour']
                    
                    # Sample every 15 minutes during work hours
                    for hour in range(work_start, work_end + 1):
                        for minute in [0, 15, 30, 45]:
                            # Skip some periods (breaks, meetings)
                            if random.random() < 0.15:  # 15% chance of no data
                                continue
                            
                            timestamp = date.replace(hour=hour, minute=minute, second=0, microsecond=0)
                            record = self.base_generator._generate_telemetry_point(profile, timestamp)
                            batch_data.append(record)
                            
                            if len(batch_data) >= records_per_batch:
                                break
                        if len(batch_data) >= records_per_batch:
                            break
                    if len(batch_data) >= records_per_batch:
                        break
                if len(batch_data) >= records_per_batch:
                    break
            
            # Add batch to overall data
            all_telemetry.extend(batch_data)
            total_generated = len(all_telemetry)
            
            # Save intermediate results
            if batch_num % 5 == 0 or total_generated >= target_records:
                logger.info(f"Saving intermediate results... ({total_generated:,} records)")
                df_temp = pd.DataFrame(all_telemetry)
                df_temp.to_csv(self.output_dir / f'massive_telemetry_batch_{batch_num}.csv', index=False)
            
            logger.info(f"Batch {batch_num} complete. Total records: {total_generated:,}")
            
            if total_generated >= target_records:
                break
        
        # Create final consolidated dataset
        logger.info("Creating final consolidated dataset...")
        df_final = pd.DataFrame(all_telemetry)
        
        # Add realistic anomalies
        logger.info("Adding realistic anomalies and variations...")
        df_final = self.base_generator.add_realistic_anomalies(df_final)
        
        # Save final dataset
        final_path = self.output_dir / 'massive_synthetic_telemetry.csv'
        df_final.to_csv(final_path, index=False)
        
        # Generate massive interaction dataset
        logger.info("Generating coaching interactions...")
        interactions = []
        
        # Generate more interactions for learning
        num_interactions = min(50000, total_generated // 10)  # 1 interaction per 10 telemetry records
        
        for i in range(num_interactions):
            profile = random.choice(user_profiles)
            interaction = self.base_generator._generate_interaction(profile)
            interactions.append(interaction)
            
            if (i + 1) % 10000 == 0:
                logger.info(f"Generated {i + 1:,} interactions...")
        
        # Save interactions
        interactions_path = self.output_dir / 'massive_synthetic_interactions.jsonl'
        with open(interactions_path, 'w') as f:
            for interaction in interactions:
                f.write(json.dumps(interaction) + '\n')
        
        # Create summary report
        persona_counts = {}
        for profile in user_profiles:
            persona_counts[profile.persona_type] = persona_counts.get(profile.persona_type, 0) + 1
        
        acceptance_rate = sum(1 for i in interactions if i.get('outcome', {}).get('accepted', False)) / len(interactions)
        
        summary = {
            'generation_timestamp': datetime.now().isoformat(),
            'target_records': target_records,
            'actual_records': len(df_final),
            'num_users': len(user_profiles),
            'num_interactions': len(interactions),
            'acceptance_rate': acceptance_rate,
            'persona_distribution': persona_counts,
            'files_generated': {
                'telemetry': str(final_path),
                'interactions': str(interactions_path),
                'user_profiles': str(self.output_dir / 'massive_user_profiles.json')
            },
            'data_quality_metrics': {
                'avg_focus_duration': float(df_final['focus_session_duration'].mean()),
                'avg_cognitive_load': float(df_final['cognitive_load_score'].mean()),
                'avg_productivity_score': float(df_final['value_score'].mean())
            }
        }
        
        with open(self.output_dir / 'massive_dataset_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n🎉 MASSIVE DATASET GENERATION COMPLETE!")
        print(f"📊 Final Statistics:")
        print(f"   Telemetry Records: {len(df_final):,}")
        print(f"   Coaching Interactions: {len(interactions):,}")
        print(f"   Unique Users: {len(user_profiles):,}")
        print(f"   Acceptance Rate: {acceptance_rate:.1%}")
        print(f"   Data Size: ~{len(df_final) * 25 / 1024 / 1024:.1f} MB")
        print(f"\n📁 Files Generated:")
        print(f"   • {final_path}")
        print(f"   • {interactions_path}")
        print(f"   • massive_user_profiles.json")
        print(f"   • massive_dataset_summary.json")
        
        return {
            'telemetry_records': len(df_final),
            'interactions': len(interactions),
            'users': len(user_profiles),
            'acceptance_rate': acceptance_rate,
            'files': summary['files_generated']
        }

async def main():
    """Main entry point for massive dataset generation."""
    
    target_records = 500000
    if len(sys.argv) > 1:
        try:
            target_records = int(sys.argv[1])
        except ValueError:
            print("Usage: python generate_massive_dataset.py [target_records]")
            return
    
    generator = MassiveDatasetGenerator()
    
    print(f"🚀 Starting massive dataset generation...")
    print(f"Target: {target_records:,} records")
    print(f"This may take 10-30 minutes depending on system performance...")
    print()
    
    start_time = datetime.now()
    
    try:
        results = generator.generate_massive_dataset(target_records)
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        print(f"\n⏱️  Generation completed in: {duration}")
        print(f"🏆 Records per second: {results['telemetry_records'] / duration.total_seconds():.0f}")
        print(f"\n✅ Ready for AI learning and evolution!")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Generation interrupted by user")
    except Exception as e:
        print(f"\n❌ Generation failed: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())