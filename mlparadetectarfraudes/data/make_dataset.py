# Improved synthetic data generation with realistic patterns
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
np.random.seed(42)
n_samples = 50000  # Larger dataset

# Base transaction data
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(n_samples)]

# Generate synthetic transaction data with realistic fraud patterns
data = pd.DataFrame({
    # Transaction timestamp (random dates within 2023)
    'transaction_datetime': dates,

    # Transaction amount (exponential distribution)
    # - 80% normal transactions (mean ~$50)
    # - 20% potential frauds (mean ~$500)
    'amount': np.concatenate([
        np.random.exponential(scale=50, size=int(n_samples*0.8)),  # Normal transactions
        np.random.exponential(scale=500, size=int(n_samples*0.2))  # Potential frauds
    ]),

    # User demographics
    'user_age': np.random.randint(18, 75, size=n_samples),  # Age between 18-75
    'user_income': np.random.normal(50000, 15000, n_samples).astype(int),  # Annual income (~N(50k,15k))

    # Device information
    'device_type': np.random.choice(['mobile','desktop','tablet'], n_samples, p=[0.6, 0.35, 0.05]),  # 60% mobile
    'os_type': np.random.choice(['iOS','Android','Windows','MacOS'], n_samples),  # Random OS
    'browser': np.random.choice(['Chrome','Safari','Firefox','Edge'], n_samples),  # Browser used

    # Geographic information
    'country': np.random.choice(['UK','US','MX','ARS','BR'], n_samples, p=[0.3, 0.4, 0.1, 0.1, 0.1]),  # 40% US
    'city_size': np.random.choice(['Metro','Urban','Suburban','Rural'], n_samples, p=[0.45, 0.3, 0.2, 0.05]),  # 40% metro

    # Transaction characteristics
    'num_products': np.random.poisson(2, n_samples) + 1,  # 1-6 products (Poisson + 1)

    # User history
    'repeat_customer': np.random.choice([0,1], n_samples, p=[0.3, 0.7]),  # 70% are repeat customers
    'account_age_days': np.random.poisson(365, n_samples),  # Account age (~1 year average)
    'previous_chargebacks': np.random.poisson(0.1, n_samples),  # Most have 0 chargebacks

    # NEW: User status (2% are deceased)
    'is_dead_user': np.random.choice([0,1], n_samples, p=[0.9998, 0.0002])  # 2% deceased users
})

# Create time-based features
data['transaction_hour'] = data['transaction_datetime'].dt.hour  # Hour of day (0-23)
data['transaction_day'] = data['transaction_datetime'].dt.dayofweek  # Day of week (0-6)
data['transaction_month'] = data['transaction_datetime'].dt.month  # Month (1-12)
data['is_night'] = ((data['transaction_hour'] >= 22) | (data['transaction_hour'] <= 6)).astype(int)  # 10pm-6am
data['is_weekend'] = (data['transaction_day'] >= 5).astype(int)  # Saturday/Sunday

# Updated fraud probability with clear pattern explanations
fraud_prob = (
    0.001 +  # Base fraud rate (0.1%)

    # Risk factors with weights:
    (data['amount'] > 300) * 0.03 +  # Large transactions 3% risk boost
    (data['is_night'] == 1) * 0.02 +  # Night transactions 2% risk boost
    (data['country'].isin(['MX', 'ARS'])) * 0.01 +  # Risky countries 1% boost
    (data['device_type'] == 'mobile') * 0.005 +  # Mobile slightly riskier
    (data['account_age_days'] < 30) * 0.02 +  # New accounts 2% boost
    (data['previous_chargebacks'] > 0) * 0.05 +  # Past chargebacks 5% boost

    # NEW: Deceased users - all transactions are fraud (overrides other factors)
    (data['is_dead_user'] == 1) * 0.99  # 99% probability (effectively 100% when thresholded)
)

# Cap probabilities between 0-100% and generate labels
fraud_prob = np.clip(fraud_prob, 0, 1)
data['is_fraud'] = np.random.binomial(1, fraud_prob) #Bernoulli

# Force all dead user transactions to be fraud (per business rule)
data.loc[data['is_dead_user'] == 1, 'is_fraud'] = 1

# Feature engineering
data['amount_to_income_ratio'] = data['amount'] / (data['user_income'] / 12)  # Monthly income ratio
data['avg_product_price'] = data['amount'] / data['num_products']
data['high_value_transaction'] = (data['amount'] > 500).astype(int)
data['new_customer'] = (data['account_age_days'] < 90).astype(int)
data['unusual_device_combo'] = ((data['device_type'] == 'mobile') & (data['os_type'] == 'Windows')).astype(int)

# Drop original datetime column

#data.drop('transaction_datetime', axis=1, inplace=True)