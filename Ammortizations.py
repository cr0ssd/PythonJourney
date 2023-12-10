def constant_amortization_schedule(principal, annual_interest_rate, num_payments):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = principal / num_payments
    schedule = []

    for month in range(1, num_payments + 1):
        interest_payment = principal * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        principal -= principal_payment
        schedule.append((month, monthly_payment, principal_payment, interest_payment, principal))

    return schedule

def display_amortization_schedule(schedule):
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Month", "Payment", "Principal Payment", "Interest Payment", "Remaining Principal"))
    for entry in schedule:
        month, payment, principal_payment, interest_payment, remaining_principal = entry
        print("{:<10} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f}".format(month, payment, principal_payment, interest_payment, remaining_principal))

if __name__ == "__main__":
    principal = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    num_payments = int(input("Enter the number of monthly payments: "))

    amortization_schedule = constant_amortization_schedule(principal, annual_interest_rate, num_payments)
    display_amortization_schedule(amortization_schedule)
