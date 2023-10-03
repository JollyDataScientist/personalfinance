import streamlit as st

def main():
    st.title("Monthly Expenses Tracker")
    
    # Sidebar
    st.sidebar.title("Summary")
    net_monthly = st.sidebar.number_input("Net Monthly Take-Home:", value=0.00, step=0.01)
    total_expenses = 0

    # Basics Section
    st.header("Basics")
    basics_expenses = 0

    with st.expander("Rent/Mortgage"):
        col1, col2 = st.columns(2)
        rent_mortgage = col2.number_input("Rent/Mortgage:", value=0.00, step=0.01)
        basics_expenses += rent_mortgage

    with st.expander("Food"):
        col1, col2 = st.columns(2)
        groceries = col2.number_input("Groceries:", value=0.00, step=0.01)
        col3, col4 = st.columns(2)
        eating_out = col4.number_input("Eating Out:", value=0.00, step=0.01)
        basics_expenses += groceries + eating_out

with st.expander("Essentials"):
    col1, col2, col3 = st.columns([1,2,2])
    col1.write("Power:")
    power = col2.number_input("", value=0.00, step=0.01, key="power_input")
    col1.write("Water:")
    water = col2.number_input("", value=0.00, step=0.01, key="water_input")
    col1.write("Heat:")
    heat = col2.number_input("", value=0.00, step=0.01, key="heat_input")
    col1.write("Toiletries:")
    toiletries = col3.number_input("", value=0.00, step=0.01, key="toiletries_input")
    col1.write("Other Consumables:")
    other_consumables = col3.number_input("", value=0.00, step=0.01, key="other_consumables_input")

    basics_expenses += power + water + heat + toiletries + other_consumables


    total_expenses += basics_expenses
    st.sidebar.text(f"Basics: ${basics_expenses:,.2f}")
    
    # Continue with the rest of the sections...

    # Display Summary on Sidebar
    st.sidebar.text(f"Total Expenses: ${total_expenses:,.2f}")
    remaining_balance = net_monthly - total_expenses
    st.sidebar.text(f"Remaining Balance: ${remaining_balance:,.2f}")

if __name__ == "__main__":
    main()
