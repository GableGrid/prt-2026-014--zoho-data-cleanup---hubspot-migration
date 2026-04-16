import pandas as pd
from datetime import datetime

# Load files
zoho = pd.read_csv('zoho_export.csv')
zb = pd.read_csv('zerobounce_result.csv')

# Merge
df = zoho.merge(zb[['email', 'status']], on='email', how='left')

# Apply rules
invalid = df['status'].isin(['invalid', 'do_not_mail', 'spamtrap', 'abuse'])

# Clinical Exception
clients_invalid = (invalid) & (df['Contact Type'] == 'Active Client')
df.loc[clients_invalid, 'Email'] = ''   # remove email but keep record

# Prospect Rule
prospects_invalid = (invalid) & (df['Contact Type'] == 'Prospect')
df = df[~prospects_invalid]   # delete rows

# Unsubscribe maintain
df.loc[df['Opt_out'] == True, 'Marketing_Eligible'] = False

# Scoring
df['Appointment_Recency_Points'] = 0
df.loc[df['Last_Appointment_Date'] >= '2026-03-17', 'Appointment_Recency_Points'] = 100  # last 30 days (adjust date)
df.loc[(df['Last_Appointment_Date'] < '2026-03-17') & 
       (df['Last_Appointment_Date'] >= '2026-02-15'), 'Appointment_Recency_Points'] = 70

df['Final_Score'] = (df['Zoho_Engagement_Score'] * 0.6) + (df['Appointment_Recency_Points'] * 0.4)

# Top 1000
top_1000 = df[df['Marketing_Eligible'] != False].nlargest(1000, 'Final_Score')

top_1000.to_csv('Top_1000_Marketing_Contacts.csv', index=False)
print("Done! Top 1000 saved.")