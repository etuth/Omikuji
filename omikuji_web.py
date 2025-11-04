import random
import streamlit as st

st.set_page_config(page_title="おみくじアプリ", page_icon="🎴", layout="centered")

st.title("✨ おみくじアプリ ✨")
st.write("ボタンを押して今日の運勢を占ってみよう！")

if st.button("おみくじを引く 🎴"):
    results = [
        ("🌸 大吉 🌸", "最高の一日！思い切って挑戦してみよう！"),
        ("🌞 中吉 🌞", "なかなか良い流れ。感謝の気持ちを忘れずに！"),
        ("🍀 小吉 🍀", "少しずつ運が上向き。焦らず進もう。"),
        ("🌙 吉 🌙", "穏やかな運勢。リラックスして過ごして吉。"),
        ("🌧️ 凶 🌧️", "無理せず休息をとろう。きっと回復するよ。"),
    ]
    title, message = random.choice(results)
    st.subheader(title)
    st.info(message)
else:
    st.write("↓ 下のボタンを押してね ↓")
