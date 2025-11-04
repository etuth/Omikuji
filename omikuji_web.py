import random
import streamlit as st

# -------------------------------
# 🌸 ページ設定
# -------------------------------
st.set_page_config(
    page_title="和風おみくじ（2026年・午年）",
    page_icon="🐴",
    layout="centered"
)

# -------------------------------
# 🌅 和風デザインCSS
# -------------------------------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1549887534-3db1bd59dcca?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #2b1b0e;
}

[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0.0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

h1 {
    color: #3b1e00;
    text-align: center;
    font-family: "Yu Mincho", "Hiragino Mincho ProN", serif;
    text-shadow: 1px 1px 3px #fff2cc;
}

h2, h3 {
    text-align: center;
    color: #4a2a0a;
    font-family: "Yu Mincho", "Hiragino Mincho ProN", serif;
}

div.stButton > button {
    background: linear-gradient(180deg, #ffefd5, #f4d47c);
    color: #3b1e00;
    border: 2px solid #d9a441;
    border-radius: 30px;
    padding: 0.8em 1.8em;
    font-size: 1.2em;
    font-weight: bold;
    font-family: "Hiragino Maru Gothic ProN", "Yu Gothic";
    box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    transition: 0.2s;
}

div.stButton > button:hover {
    background: linear-gradient(180deg, #fff4d6, #f9da78);
    transform: scale(1.05);
}

footer {
    color: #5a3d0a;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -------------------------------
# 🐴 タイトル
# -------------------------------
st.markdown("## 🐴 2026年・午年 和風おみくじ 🎴")
st.write("令和の運を占いましょう。馬のように勢いある一年に🐎✨")

# -------------------------------
# 🎍 おみくじ結果リスト
# -------------------------------
results = [
    ("🌸 大吉 🌸", "勢いよく前進できる一年！夢に向かって一直線。"),
    ("🌞 中吉 🌞", "小さな努力が大きな実を結ぶ。信念を持って進め！"),
    ("🍀 小吉 🍀", "周りの助けで道が開ける。感謝を忘れずに。"),
    ("🌙 吉 🌙", "落ち着いて過ごすと運気安定。心穏やかに。"),
    ("🌧️ 凶 🌧️", "焦らず、馬を休ませるように心を整える時。")
]

# -------------------------------
# 🎴 ボタンと結果表示
# -------------------------------
if st.button("おみくじを引く 🎴"):
    title, message = random.choice(results)
    st.markdown(f"<h2>{title}</h2>", unsafe_allow_html=True)
    st.success(message)
else:
    st.info("下のボタンを押して、2026年の運勢を占いましょう。")

# -------------------------------
# 🪶 フッター
# -------------------------------
st.markdown("---")
st.caption("© 2026 和風おみくじ 🐴 Designed with ❤️ by Streamlit & Python")
