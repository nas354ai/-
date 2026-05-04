import streamlit as st

from utils.profit_analyzer import profit_analyzer

st.title("商品售價分析器")


item_price = st.number_input("請輸入進貨商品價格 (RMB)", min_value=0.0, value=100.0)
item_weight = st.number_input("請輸入進貨商品重量 (KG)", min_value=0.0, value=1.0)
china_shipping = st.number_input("請輸入國際運費 (RMB)", min_value=0.0, value=8.0)


if st.button("開始分析"):
    result = profit_analyzer(item_price, item_weight, china_shipping)

    st.write("---")

    st.info(f"當前計算邏輯：匯率使用 **4.5** | 平台抽成 **20%** | 目標毛利 **30%**")

    st.success(f"### 建議零售價：NT$ {result['建議售價']}")
    
    st.caption(f"註：此計算已包含 10% 的營業稅與營所稅預留。")

    st.write("---")

    st.markdown("### --- 毛利 30% 分析 ---")

    st.write(f"**採購價：** {item_price} RMB")

    st.success(f"**建議售價：** NT$ {result['建議售價']}")
    
   
    col1, col2 = st.columns(2)
    col1.metric("總成本", f"NT$ {result['總成本']}")
    col2.metric("實拿純利", f"NT$ {result['實拿純利']}")