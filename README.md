# Identity Risk Scoring System
 
 A security data science project that analyzes user access logs and assigns risk scores to detect anomalous behavior. 

 ## What It Does
- Scores each login session from 0-100 based on risk indicators
- Flags High and Critical sessions for SOC analyst review
- Uses Isolation Forest machine learning to catch what rules miss

## Risk Indicators
- Off-hours login activity
- Failed authentication attempts
- Logins from unknown locations
- Sensitive resource access
- Privilege escalation attempts
- MFA bypass events

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn (Isolation Forest)
- Matplotlib, Seaborn
- Jupyter Notebook