import streamlit as st
import random

st.title("💰 Risk It or Rich It")

st.write("Each player has ₹10,000 as vitual money")

st.header("Enter player details")
p1_name=st.text_input("Enter player 1 name")
p2_name=st.text_input("Enter player 2 name")
st.header("Player 1 Investment")
p1_A = st.number_input("Amount in Company - Profit Prasadam Co.", 0, 10000, 0)
p1_B = st.number_input("Amount in Company - Risky Rasgulla Ventures", 0, 10000, 0)
p1_C = st.number_input("Amount in Company - Bullrun Babes Pvt Ltd.", 0, 10000, 0)

st.header("Player 2 Investment")
p2_A = st.number_input("P2 Amount in Company - Profit Prasadam Co.", 0, 10000, 0)
p2_B = st.number_input("P2 Amount in Company - Risky Rasgulla Ventures", 0, 10000, 0)
p2_C = st.number_input("P2 Amount in Company - Bullrun Babes Pvt Ltd.", 0, 10000, 0)

if st.button("Calculate Results"):
    # Randomized growth rates (2-year multipliers)
    growth = {
        "A": random.uniform(1.4, 1.6),  # Stable
        "B": random.choice([0.8, 1.9]),  # High risk
        "C": 1.8 if random.random() < 0.8 else 1.1,  # Mostly strong, small crash chance
    }
    risk = {
        "A":0.2,
        "B":0.7,
        "C":0.1
    }

    p1_total = (
        p1_A * growth["A"] +
        p1_B * growth["B"] +
        p1_C * growth["C"] 
    )

    p2_total = (
        p2_A * growth["A"] +
        p2_B * growth["B"] +
        p2_C * growth["C"] 
    )
    p1_risk=(
        ((p1_A*risk["A"]+p1_B*risk["B"]+p1_C*risk["C"])/10000)*100
    )
    p2_risk=(
        ((p2_A*risk["A"]+p2_B*risk["B"]+p2_C*risk["C"])/10000)*100
    )
    if (p1_A + p1_B + p1_C) > 10000:
        st.error("Player 1 invested more than ₹10,000!")
        st.stop()

    if (p2_A + p2_B + p2_C) > 10000:
        st.error("Player 2 invested more than ₹10,000!")
        st.stop()
    st.subheader("📊 Company Growth Multipliers (After 2 Years)")
    for company, rate in growth.items():
        st.write(f"Company {company}: {rate:.2f}x")
    st.subheader("📈 Final Amount After 2 Years")
    st.write("Player 1", p1_total)
    st.write("Player 2", p2_total)
    st.subheader("Average Risk:")
    st.write("Player 1","Risk:",p1_risk," %")
    st.write("Player 2","Risk:",p2_risk," %")
    if p1_total > p2_total:
        st.success("🏆 Player 1 Wins!")
    elif p2_total > p1_total:
        st.success("🏆 Player 2 Wins!")
    else:

        st.info("It's a Tie!")









