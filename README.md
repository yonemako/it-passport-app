import streamlit as st

# アプリのタイトル
st.title("🧠 ITパスポート 魔法の暗記アプリ")
st.write("難しい用語を、日常の例えと図解で一発暗記！")

# 用語を選択するプルダウン
selected_term = st.selectbox(
    "覚えたい用語を選んでください",
    ["Cookie（クッキー）", "DNS", "WBS"]
)

# ボタンを押したときの処理
if st.button("✨ 魔法の解説を表示する"):
    if selected_term == "Cookie（クッキー）":
        st.subheader("🍪 Cookie（クッキー）")
        st.write("**一言で言うと**: ネット上の『私の身分証・おぼえ書きタグ』")
        
        st.info("💡 日常の例え：常連のカフェで店員さんが「いつものね！」と覚えていてくれるようなもの。ブラウザに小さなメモを貼っておく仕組みです。")
        
        st.text("""
【テキスト図解】
[スマホ] ── 1回目ログイン ──> [Webサーバー]
         <── Cookieを預かる ──┘
        """)
        
        st.warning("⚠️ 引っ掛けポイント：サーバー側ではなく、自分のブラウザ（手元）に保存されます！")

    elif selected_term == "DNS":
        st.subheader("🌐 DNS（Domain Name System）")
        st.write("**一言で言うと**: ネット上の『電話帳』")
        st.info("💡 日常の例え：『Amazonに行きたい！』と入力したとき、裏で数字の住所（IPアドレス）に変換して案内してくれる親切な案内人です。")
