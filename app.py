import streamlit as st

st.title("あと何分かかんのこれ？")

# input
a = st.number_input("前に何人並んでる？",0)
b = st.number_input("今の1分間で何人うしろに並んだ？",0)

# process
try:
  c = a / b

# output
# st.title("計算結果")
  st.caption("たぶん")
  st.text(c)
  st.caption("分後ぐらいに順番がまわってくるでしょう。知らんけど。")

except ValueError:
  print('整数を入力してください')

except ZeroDivisionError:
  print('0を入力しないでください')

