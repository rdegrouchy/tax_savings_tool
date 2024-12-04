import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Tax-Advantaged Savings Impact Tool")
st.write("""
This tool calculates how changes in employee participation and contributions to tax-advantaged savings accounts
(such as 401(k) or HSA) impact federal taxes for employees and payroll taxes for employers.
""")

# Sidebar Inputs
st.sidebar.header("Input Parameters")
num_employees = st.sidebar.number_input("Number of Employees", value=100, step=10)
avg_income = st.sidebar.number_input("Average Annual Income ($)", value=50000, step=1000)
participation_rate = st.sidebar.slider("Participation Rate (%)", 0, 100, 50) / 100
contribution_rate = st.sidebar.slider("Contribution Rate (%)", 0, 15, 5) / 100

# Tax Constants
marginal_tax_rate = 0.22  # Federal marginal tax rate (example)
fica_rate = 0.0765        # Employer payroll tax rate

# Calculations
participants = int(num_employees * participation_rate)
total_contributions = participants * avg_income * contribution_rate
reduced_taxable_income = avg_income - (avg_income * contribution_rate)

employee_tax_savings = participants * (avg_income * marginal_tax_rate - reduced_taxable_income * marginal_tax_rate)
employer_tax_savings = participants * (avg_income * fica_rate - reduced_taxable_income * fica_rate)

# Results
st.write(f"### Results for {num_employees} Employees:")
st.write(f"- **Total Employee Tax Savings**: ${employee_tax_savings:,.2f}")
st.write(f"- **Total Employer Payroll Tax Savings**: ${employer_tax_savings:,.2f}")
st.write(f"- **Total Contributions to Tax-Advantaged Accounts**: ${total_contributions:,.2f}")

# Visualization
st.write("### Visualization of Savings by Contribution Rate")
fig, ax = plt.subplots()
contribution_rates = np.linspace(0, 0.15, 100)
savings = [
    (
        cr,
        participants * avg_income * marginal_tax_rate * cr,
        participants * avg_income * fica_rate * cr,
    )
    for cr in contribution_rates
]

df = pd.DataFrame(
    savings, columns=["Contribution Rate", "Employee Tax Savings", "Employer Tax Savings"]
)
ax.plot(df["Contribution Rate"], df["Employee Tax Savings"], label="Employee Tax Savings")
ax.plot(df["Contribution Rate"], df["Employer Tax Savings"], label="Employer Tax Savings")
ax.set_xlabel("Contribution Rate")
ax.set_ylabel("Savings ($)")
ax.legend()
st.pyplot(fig)

st.write("""
Use the sliders on the left to adjust participation and contribution rates and see the impact
on employee and employer tax savings.
""")
