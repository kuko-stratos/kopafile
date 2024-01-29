import streamlit as st

st.title("あと何分かかんのこれ？")

# input
a = st.number_input("前に何人並んでる？")
b = st.number_input("今の1分間で何人うしろに並んだ？")

# process
c = a / b

# output
# st.title("計算結果")
st.caption("たぶん")
st.text(c)
st.caption("分後ぐらいに順番がまわってくるでしょう。知らんけど。")