import streamlit as st
import random

# 设置页面标题和图标（手机浏览器标签页会显示）
st.set_page_config(page_title="随机点餐助手", page_icon="🍽️", layout="centered")

# 菜单数据（你可以自由增删改）
MENU = [
    "宫保鸡丁", "酸菜鱼", "麻辣香锅", "西红柿鸡蛋",
    "红烧肉", "沙拉", "披萨", "牛肉面", "饺子", "寿司",
    "炸鸡", "炒饭", "意面", "汉堡", "粥"
]

# 初始化 session_state 保存当前菜品
if "current_food" not in st.session_state:
    st.session_state.current_food = random.choice(MENU)

# 界面布局
st.title("🤔 今天吃什么？")
st.markdown("点击下方按钮，帮你随机决定今日美食～")

# 显示当前随机菜品（大号字体）
st.markdown(f"## 🍲 {st.session_state.current_food}")

# 随机按钮
if st.button("🎲 随机点餐", use_container_width=True):
    st.session_state.current_food = random.choice(MENU)
    st.rerun()  # 刷新页面，显示新菜品

# 页脚小提示
st.caption("把这个链接分享给朋友，他们也能用～")