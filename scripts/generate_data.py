import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Load parameters from CSV
def load_parameters(filepath='../data/dhyana_parameters.csv'):
    df = pd.read_csv(filepath)
    params = dict(zip(df['Parameter'], df['Value']))
    return params

# Load the parameters
params = load_parameters()

# Print one to confirm
print(f"Monthly patient growth rate: {params['monthly_patient_growth_rate']}")

# Set date range
start_date = datetime(2022, 4, 1)
end_date = datetime(2025, 6, 30)

# Base values
initial_patients = 20
initial_doctors = 10

# Prepare lists
doctors = []
patients = []

# ID counters
doctor_id_counter = 1
patient_id_counter = 1

# Time loop (month by month)
current_date = start_date
while current_date <= end_date and len(patients) < 65000:
    # How many new doctors this month?
    num_doctors = int(initial_doctors * (1 + params['monthly_doctor_growth_rate']))
    for _ in range(num_doctors):
        doctor_id = f"DOC{doctor_id_counter:04d}"
        doctors.append({
            "user_id": doctor_id,
            "user_type": "doctor",
            "signup_date": current_date.strftime("%Y-%m-%d")
        })
        doctor_id_counter += 1

        if len(doctors) >= 4000:
            break
    initial_doctors += num_doctors

    # How many new patients this month?
    num_patients = int(initial_patients * (1 + params['monthly_patient_growth_rate']))
    for _ in range(num_patients):
    # Decide traits using probabilities
        churned = random.random() < params['early_churn_rate']
        completed = not churned and random.random() < params['program_completion_rate']
        healed = completed and random.random() < params['healed_user_rate']
        power_user = completed and random.random() < params['power_user_rate']
        reengaged = churned and random.random() < params['reengagement_rate']

        patient_id = f"PAT{patient_id_counter:05d}"
        assigned_doctor = random.choice(doctors)['user_id'] if doctors else None
        patients.append({
            "user_id": patient_id,
            "user_type": "patient",
            "signup_date": current_date.strftime("%Y-%m-%d"),
            "assigned_doctor": assigned_doctor,
            "churned_early": churned,
            "completed": completed,
            "healed": healed,
            "power_user": power_user,
            "reengaged": reengaged
            })
        patient_id_counter += 1

    initial_patients += num_patients

    # Move to next month
    current_date += timedelta(days=30)

# After the while loop ends
print(f"Generated {len(patients)} patients and {len(doctors)} doctors.")
print("Sample patient with traits:", patients[0])

events = []
event_id_counter = 1

for patient in patients:
    uid = patient['user_id']
    signup = datetime.strptime(patient['signup_date'], "%Y-%m-%d")
    churned = patient['churned_early']
    completed = patient['completed']
    healed = patient['healed']
    power = patient['power_user']
    reengaged = patient['reengaged']

    # Event: account_created
    events.append({
        "event_id": event_id_counter,
        "user_id": uid,
        "event_type": "account_created",
        "timestamp": signup.strftime("%Y-%m-%d")
    })
    event_id_counter += 1

    # Event: program_started
    program_start = signup + timedelta(days=random.randint(1, 3))
    events.append({
        "event_id": event_id_counter,
        "user_id": uid,
        "event_type": "program_started",
        "timestamp": program_start.strftime("%Y-%m-%d")
    })
    event_id_counter += 1

    # Skip if churned early
    if churned:
        events.append({
            "event_id": event_id_counter,
            "user_id": uid,
            "event_type": "program_abandoned",
            "timestamp": (program_start + timedelta(days=random.randint(7, 14))).strftime("%Y-%m-%d")
        })
        event_id_counter += 1
        continue

    # Set how many weeks of activity
    duration_weeks = 16 if power else 10
    for week in range(duration_weeks):
        session_date = program_start + timedelta(weeks=week)
        # 70% chance they meditated this week
        if random.random() < 0.7:
            events.append({
                "event_id": event_id_counter,
                "user_id": uid,
                "event_type": "meditation_session_completed",
                "timestamp": session_date.strftime("%Y-%m-%d")
            })
            event_id_counter += 1
        # 50% chance they journaled this week
        if random.random() < 0.5:
            events.append({
                "event_id": event_id_counter,
                "user_id": uid,
                "event_type": "journal_entry_created",
                "timestamp": session_date.strftime("%Y-%m-%d")
            })
            event_id_counter += 1

    # Add halfway and completion milestones
    halfway = program_start + timedelta(weeks=duration_weeks // 2)
    complete = program_start + timedelta(weeks=duration_weeks)

    if completed:
        events.append({
            "event_id": event_id_counter,
            "user_id": uid,
            "event_type": "program_halfway_completed",
            "timestamp": halfway.strftime("%Y-%m-%d")
        })
        event_id_counter += 1

        events.append({
            "event_id": event_id_counter,
            "user_id": uid,
            "event_type": "program_completed",
            "timestamp": complete.strftime("%Y-%m-%d")
        })
        event_id_counter += 1

    if healed:
        # drop-off naturally, no further action
        continue

    if reengaged:
        # resume some events 4–8 weeks later
        reengage_start = complete + timedelta(weeks=random.randint(4, 8))
        for i in range(2):
            events.append({
                "event_id": event_id_counter,
                "user_id": uid,
                "event_type": "journal_entry_created",
                "timestamp": (reengage_start + timedelta(weeks=i)).strftime("%Y-%m-%d")
            })
            event_id_counter += 1

print(f"Generated {len(events)} total events.")
print("Sample event:", events[0])

# Convert lists to DataFrames
df_users = pd.DataFrame(patients + doctors)
df_events = pd.DataFrame(events)

# Save to CSVs
df_users.to_csv("../data/synthetic_users.csv", index=False)
df_events.to_csv("../data/synthetic_events.csv", index=False)

print("Saved synthetic_users.csv and synthetic_events.csv to /data")
