import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Tax-Advantaged Savings Impact Tool")
st.write("""
This tool calculates how changes in employee participation and contributions to tax-advantaged savings accounts
(such as FSAs) impact federal taxes for employees and payroll taxes for employers.
""")

# Sidebar Inputs
st.sidebar.header("Input Parameters")
num_employees = st.sidebar.number_input("Number of Employees", value=100, step=10)
avg_income = st.sidebar.number_input("Average Annual Income ($)", value=50000, step=1000)
participation_rate = st.sidebar.slider("Participation Rate (%)", 0, 100, 50) / 100

# Fixed Contribution Amount per Employee
fsa_contribution = st.sidebar.number_input("FSA Contribution per Employee ($)", value=3000, step=100)

# Tax Constants
marginal_tax_rate = 0.22  # Federal marginal tax rate (example)
fica_rate = 0.0765        # Employer payroll tax rate

# Calculations
participants = int(num_employees * participation_rate)
total_contributions = participants * fsa_contribution
reduced_taxable_income = avg_income - fsa_contribution

# Employee Tax Savings
employee_tax_savings = participants * fsa_contribution * marginal_tax_rate

# Employer Tax Savings
employer_tax_savings = participants * fsa_contribution * fica_rate

# Results
st.write(f"### Results for {num_employees} Employees:")
st.write(f"- **Total Employee Tax Savings**: ${employee_tax_savings:,.2f}")
st.write(f"- **Total Employer Payroll Tax Savings**: ${employer_tax_savings:,.2f}")
st.write(f"- **Total Contributions to FSAs**: ${total_contributions:,.2f}")

# Visualization
st.write("### Visualization of Savings by Contribution Amount")
fig, ax = plt.subplots()

# Simulate Savings for Different Contribution Amounts
contribution_amounts = np.arange(0, 4000, 100)  # Contribution amounts up to $4000
savings = [
    (
        amount,
        participants * amount * marginal_tax_rate,
        participants * amount * fica_rate,
    )
    for amount in contribution_amounts
]

df = pd.DataFrame(
    savings, columns=["Contribution Amount", "Employee Tax Savings", "Employer Tax Savings"]
)
ax.plot(df["Contribution Amount"], df["Employee Tax Savings"], label="Employee Tax Savings")
ax.plot(df["Contribution Amount"], df["Employer Tax Savings"], label="Employer Tax Savings")
ax.set_xlabel("Contribution Amount ($)")
ax.set_ylabel("Savings ($)")
ax.legend()
st.pyplot(fig)

st.write("""
Use the sliders on the left to adjust participation and contribution amounts to see their impact
on employee and employer tax savings.
""")

