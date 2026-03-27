import streamlit as st
import random

st.set_page_config(page_title="随机点餐助手", page_icon="🍽️", layout="centered")

# 微信分享卡片 meta 标签
st.markdown(
    """
    <meta property="og:title" content="随机点餐助手">
    <meta property="og:description" content="点击按钮，随机决定今天吃什么！">
    <meta property="og:image" content="https://https://github.com/DKDK1990/random-food-for-love/tree/main/images/food.jpg">
    <meta property="og:type" content="website">
    """,
    unsafe_allow_html=True
)

MENU = [
    "宫保鸡丁", "酸菜鱼", "麻辣香锅", "西红柿鸡蛋",
    "红烧肉", "沙拉", "披萨", "牛肉面", "饺子", "寿司",
    "炸鸡", "炒饭", "意面", "汉堡", "粥"
]

if "current_food" not in st.session_state:
    st.session_state.current_food = random.choice(MENU)

st.title("🤔 今天吃什么？")
st.markdown("点击下方按钮，帮你随机决定今日美食～")

st.markdown(f"## 🍲 {st.session_state.current_food}")

if st.button("🎲 随机点餐", use_container_width=True):
    st.session_state.current_food = random.choice(MENU)

st.caption("把这个链接分享给朋友，他们也能用～")
