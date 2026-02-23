import streamlit as st

st.title("💰 Mini Investment Game")

st.write("Each player starts with ₹10,000")

# Company growth rates (after 2 years)
growth = {
    "A": 1.5,
    "B": 1.3,
    "C": 1.8,
    "D": 1.2,
    "E": 2.0
}
st.header("Enter player details")
p1_name=st.text_input("Enter player 1 name")
p2_name=st.text_input("Enter player 2 name")
st.header("Player 1 Investment")
p1_A = st.number_input("Amount in Company A", 0, 10000, 0)
p1_B = st.number_input("Amount in Company B", 0, 10000, 0)
p1_C = st.number_input("Amount in Company C", 0, 10000, 0)
p1_D = st.number_input("Amount in Company D", 0, 10000, 0)
p1_E = st.number_input("Amount in Company E", 0, 10000, 0)

st.header("Player 2 Investment")
p2_A = st.number_input("P2 Amount in Company A", 0, 10000, 0)
p2_B = st.number_input("P2 Amount in Company B", 0, 10000, 0)
p2_C = st.number_input("P2 Amount in Company C", 0, 10000, 0)
p2_D = st.number_input("P2 Amount in Company D", 0, 10000, 0)
p2_E = st.number_input("P2 Amount in Company E", 0, 10000, 0)

if st.button("Calculate Results"):

    p1_total = (
        p1_A * growth["A"] +
        p1_B * growth["B"] +
        p1_C * growth["C"] +
        p1_D * growth["D"] +
        p1_E * growth["E"]
    )

    p2_total = (
        p2_A * growth["A"] +
        p2_B * growth["B"] +
        p2_C * growth["C"] +
        p2_D * growth["D"] +
        p2_E * growth["E"]
    )

    st.subheader("📈 Final Amount After 2 Years")
    st.write("Player 1", p1_total)
    st.write("Player 2", p2_total)

    if p1_total > p2_total:
        st.success("🏆 Player 1 Wins!")
    elif p2_total > p1_total:
        st.success("🏆 Player 2 Wins!")
    else:
        st.info("It's a Tie!")