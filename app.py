def main():
    st.title("Monthly Expenses Tracker")
    
    # Sidebar
    st.sidebar.title("Summary")
    net_monthly = st.sidebar.number_input("Net Monthly Take-Home:", value=0.00, step=0.01)
    total_expenses = 0

    # Basics Section
    st.header("Basics")

    rent_mortgage = st.number_input("Rent/Mortgage:", value=0.00, step=0.01)
    total_expenses += rent_mortgage

    st.subheader("Food")
    groceries = st.number_input("Groceries:", value=0.00, step=0.01)
    eating_out = st.number_input("Eating Out:", value=0.00, step=0.01)
    total_expenses += groceries + eating_out

    st.subheader("Essentials")
    power = st.number_input("Power:", value=0.00, step=0.01)
    water = st.number_input("Water:", value=0.00, step=0.01)
    heat = st.number_input("Heat:", value=0.00, step=0.01)
    toiletries = st.number_input("Toiletries:", value=0.00, step=0.01)
    other_consumables = st.number_input("Other Consumables:", value=0.00, step=0.01)
    total_expenses += power + water + heat + toiletries + other_consumables

    st.subheader("Monthly Expenses")
    car_payments = st.number_input("Car Payments:", value=0.00, step=0.01)
    cell_phone = st.number_input("Cell Phone:", value=0.00, step=0.01)
    internet = st.number_input("Internet:", value=0.00, step=0.01)
    media_streaming = st.number_input("Media/Streaming:", value=0.00, step=0.01)
    other_subscriptions = st.number_input("Other Subscriptions:", value=0.00, step=0.01)
    total_expenses += car_payments + cell_phone + internet + media_streaming + other_subscriptions

    st.subheader("Outstanding Debts")
    student_loan = st.number_input("Student Loan:", value=0.00, step=0.01)
    credit_card = st.number_input("Credit Card:", value=0.00, step=0.01)
    line_of_credit = st.number_input("Line of Credit:", value=0.00, step=0.01)
    other_loans = st.number_input("Other Loans:", value=0.00, step=0.01)
    total_expenses += student_loan + credit_card + line_of_credit + other_loans

    # Display Summary on Sidebar
    st.sidebar.text(f"Total Expenses: ${total_expenses:,.2f}")
    remaining_balance = net_monthly - total_expenses
    st.sidebar.text(f"Remaining Balance: ${remaining_balance:,.2f}")

if __name__ == "__main__":
    main()
