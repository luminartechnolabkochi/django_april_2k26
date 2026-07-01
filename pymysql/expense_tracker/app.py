import streamlit as st
import mysql.connector


# ===========================================
# PAGE CONFIGURATION
# ===========================================

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)


# ===========================================
# DATABASE CONNECTION
# ===========================================

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password@123",
        database="fund_db"
    )


# ===========================================
# GET ALL EXPENSES
# ===========================================

def get_all_expenses():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM transaction
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records




def get_expense_by_id(expense_id):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT *
        FROM `transaction`
        WHERE id=%s
    """

    cursor.execute(query, (expense_id,))

    expense = cursor.fetchone()

    cursor.close()
    conn.close()

    return expense


# ===========================================
# UPDATE EXPENSE
# ===========================================

def update_expense(
    expense_id,
    title,
    amount,
    owner,
    category,
    payment_method,
    created_at
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
        UPDATE `transaction`

        SET

            title=%s,
            amount=%s,
            owner=%s,
            category=%s,
            payment_method=%s,
            created_at=%s

        WHERE id=%s
    """

    values = (
        title,
        amount,
        owner,
        category,
        payment_method,
        created_at,
        expense_id
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()


# ===========================================
# DELETE EXPENSE
# ===========================================

def delete_expense(expense_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM `transaction` WHERE id=%s",
        (expense_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

# ===========================================
# DASHBOARD
# ===========================================

st.title("💰 Expense Tracker")

st.write("---")


# ===========================================
# ADD EXPENSE
# ===========================================

def add_expense(title, amount, owner, category, payment_method, created_at):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
        INSERT INTO `transaction`
        (
            title,
            amount,
            owner,
            category,
            payment_method,
            created_at
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
    """

    values = (
        title,
        amount,
        owner,
        category,
        payment_method,
        created_at
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

menu = st.sidebar.radio(

    "Select Menu",

    [

        "Dashboard",

        "Add Expense",

        "View Expense",

        "Edit Expense",

        "Delete Expense"

    ]

)

if menu == "Dashboard":

    st.title("💰 Expense Dashboard")

    expenses = get_all_expenses()

    if expenses:

        st.dataframe(
            expenses,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No Expenses Found.")

elif menu == "Add Expense":

    st.title("➕ Add Expense")

    with st.form("expense_form"):

        title = st.text_input("Title")

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            format="%.2f"
        )

        owner = st.text_input("Owner")

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Travel",
                "Shopping",
                "Rent",
                "Medical",
                "Education",
                "Entertainment",
                "Utility",
                "Other"
            ]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Cash",
                "UPI",
                "Credit Card",
                "Debit Card",
                "Net Banking"
            ]
        )

        created_at = st.date_input("Expense Date")

        submit = st.form_submit_button("Save Expense")

    if submit:

        print("hereee")

        if title == "" or owner == "":

            st.error("Please fill all required fields.")

        else:

            add_expense(
                title,
                amount,
                owner,
                category,
                payment_method,
                created_at
            )

            st.success("Expense Added Successfully.")

            st.rerun()


elif menu == "View Expense":

    st.title("👁 View Expense")

    expense_id = st.number_input(
        "Enter Expense ID",
        min_value=1,
        step=1
    )

    if st.button("View"):

        expense = get_expense_by_id(expense_id)

        if expense:

            st.write("### Expense Details")

            st.write("ID :", expense["id"])
            st.write("Title :", expense["title"])
            st.write("Amount :", expense["amount"])
            st.write("Owner :", expense["owner"])
            st.write("Category :", expense["category"])
            st.write("Payment :", expense["payment_method"])
            st.write("Created :", expense["created_at"])

        else:

            st.error("Expense Not Found.")

elif menu == "Edit Expense":

    st.title("✏ Edit Expense")

    expense_id = st.number_input(
        "Expense ID",
        min_value=1,
        step=1,
        key="edit_id"
    )

    if st.button("Load Expense"):

        st.session_state.expense = get_expense_by_id(expense_id)

    if "expense" in st.session_state:

        e = st.session_state.expense

        if e:

            with st.form("update_form"):

                title = st.text_input("Title", e["title"])

                amount = st.number_input(
                    "Amount",
                    value=float(e["amount"])
                )

                owner = st.text_input(
                    "Owner",
                    e["owner"]
                )

                category = st.text_input(
                    "Category",
                    e["category"]
                )

                payment = st.text_input(
                    "Payment Method",
                    e["payment_method"]
                )

                created = st.date_input(
                    "Created Date",
                    e["created_at"]
                )

                update = st.form_submit_button(
                    "Update Expense"
                )

            if update:

                update_expense(

                    expense_id,

                    title,

                    amount,

                    owner,

                    category,

                    payment,

                    created

                )

                st.success(
                    "Expense Updated Successfully."
                )

                del st.session_state.expense
