import random
import streamlit as st

# -------------------------------
# ページ設定
# -------------------------------
st.set_page_config(
    page_title="和風おみくじ（2026年・午年）",
    page_icon="🐴",
    layout="centered"
)

# -------------------------------
# 🌸 背景 + 桜吹雪アニメーション（確実に動作する版）
# -------------------------------
sakura_css = """
<style>
/* 背景 */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom, #fffaf0, #fde8b8);
    color: #3b1e00;
    font-family: "Yu Mincho", "Hiragino Mincho ProN", serif;
    overflow: hidden;
}

/* ボタンデザイン */
div.stButton > button {
    background: linear-gradient(180deg, #fff5cc, #f7d774);
    color: #3b1e00;
    border: 2px solid #d4a017;
    border-radius: 30px;
    padding: 0.8em 1.8em;
    font-size: 1.2em;
    font-weight: bold;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    transition: 0.2s;
}
div.stButton > button:hover {
    background: linear-gradient(180deg, #fff8d9, #f9da78);
    transform: scale(1.05);
}

/* 桜の花びら（固定画像を使用） */
.sakura {
    position: fixed;
    top: -10px;
    width: 25px;
    height: 25px;
    background-image: url('https://raw.githubusercontent.com/miiton/CSS-Sakura/master/sakura.png');
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 0.9;
    z-index: 0;
    pointer-events: none;
    animation-name: fall;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}

/* アニメーション定義 */
@keyframes fall {
    0% {
        transform: translateX(0) rotate(0deg);
        top: -10px;
        opacity: 1;
    }
    100% {
        transform: translateX(200px) rotate(360deg);
        top: 110%;
        opacity: 0;
    }
}
</style>
"""
st.markdown(sakura_css, unsafe_allow_html=True)

# 🌸 複数の桜を生成（JSでアニメ時間をずらす）
sakura_js = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    const numPetals = 30;
    for (let i = 0; i < numPetals; i++) {
        const petal = document.createElement('div');
        petal.className = 'sakura';
        petal.style.left = Math.random() * 100 + 'vw';
        petal.style.animationDuration = 6 + Math.random() * 6 + 's';
        petal.style.animationDelay = Math.random() * 5 + 's';
        petal.style.transform = 'scale(' + (0.5 + Math.random() * 0.8) + ')';
        document.body.appendChild(petal);
    }
});
</script>
"""
st.markdown(sakura_js, unsafe_allow_html=True)

# -------------------------------
# 🐴 タイトル
# -------------------------------
st.markdown("<h1 style='text-align:center;'>🐴 2026年・午年 和風おみくじ 🎴</h1>", unsafe_allow_html=True)
st.write("桜舞う春のように、幸せが訪れる一年を占いましょう🌸")

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
    st.markdown(f"<h2 style='text-align:center;'>{title}</h2>", unsafe_allow_html=True)
    st.success(message)
else:
    st.info("🌸 下のボタンを押して、運勢を占いましょう。")

# -------------------------------
# 🪶 フッター
# -------------------------------
st.markdown("---")
st.caption("© 2026 和風おみくじ 🐴 Designed with ❤️ by Streamlit & Python")
