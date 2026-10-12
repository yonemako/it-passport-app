import streamlit as st

st.title("🧠 ITパスポート 魔法の暗記アプリ")
st.write("50音順や頭文字から用語を選んで、日常の例えと図解でサクッと暗記しよう！")

# サンプルの用語データベース（頭文字・50音順の分類付き）
# 将来的にここを数百語に拡張できます！
terms_db = {
    "Cookie（クッキー）": {
        "kana": "か行",
        "initial": "C",
        "category": "セキュリティ",
        "definition": "ネット上の『私の身分証・おぼえ書きタグ』",
        "analogy": "常連のカフェで店員さんが「いつものね！」と覚えていてくれるようなもの。ブラウザに小さなメモを貼っておく仕組みです。",
        "diagram": "[スマホ] ── 1回目ログイン ──> [Webサーバー]\n         <── Cookieを預かる ──┘",
        "warning": "サーバー側ではなく、自分のブラウザ（手元）に保存されます！"
    },
    "DNS": {
        "kana": "た行",
        "initial": "D",
        "category": "ネットワーク",
        "definition": "ネット上の『電話帳』",
        "analogy": "『Amazonに行きたい！』と入力したとき、裏で数字の住所（IPアドレス）に変換して案内してくれる親切な案内人です。",
        "diagram": "（文字のドメイン名） ── DNS ──> （数字のIPアドレス）",
        "warning": "ドメイン名（文字）からIPアドレス（数字）に変換するのがDNSの役割です。"
    },
    "WBS": {
        "kana": "わ行",
        "initial": "W",
        "category": "マネジメント",
        "definition": "プロジェクトの『巨大なスイカの解体マップ』",
        "analogy": "大きな仕事を小さなパーツに細かく分解して、誰が・いつまでにやるかを整理する設計図です。",
        "diagram": "プロジェクト全体 ──> 大タスク ──> 中タスク ──> 細部",
        "warning": "スケジュール（ガントチャートなど）を作る「前」に、作業を階層的に分解する作業です。"
    },
    "CPUとメモリ": {
        "kana": "さ行",
        "initial": "C",
        "category": "ハードウェア",
        "definition": "「職人（CPU）」と「作業机（メモリ）」",
        "analogy": "CPUはバリバリ働く「料理人（頭脳）」、メモリは一度に広げられる「調理台の広さ」。",
        "diagram": "[CPU（頭脳・処理）] ⇄ [メモリ（一時的な机）]",
        "warning": "電源を切るとメモリの中身はすべて消えます（揮発性）！"
    },
    "SQL": {
        "kana": "さ行",
        "initial": "S",
        "category": "データベース",
        "definition": "データベースにお願いをするための『専用の呪文』",
        "analogy": "図書館の巨大な検索システムで「2026年出版の本を全部出して！」と司書さんにお願いする言葉のようなもの。",
        "diagram": "[ユーザー] ── SQL（命令文） ──> [データベース]",
        "warning": "データベースを「管理するソフト」ではなく、命令を出す「言語」の名前です。"
    },
    "ペネトレーションテスト": {
        "kana": "は行",
        "initial": "P",
        "category": "セキュリティ",
        "definition": "本物のハッカーになりきって『セキュリティの弱点』を探す模擬攻撃",
        "analogy": "自宅の鍵が本当に泥棒に破られないか、専門の鍵師に頼んでわざとピッキングしてもらうようなもの。",
        "diagram": "[攻撃者役（テスター）] ── 模擬ハッキング ──> [システム]",
        "warning": "単なる自動の脆弱性診断ツールではなく、実際に侵入を試みる高度なテストです。"
    }
}

# サイドバーで検索方法を選択
search_mode = st.sidebar.radio(
    "🔍 探す方法を選んでください",
    ["50音順から選ぶ", "アルファベット（A-Z）から選ぶ", "すべての用語一覧"]
)

selected_term = None

if search_mode == "50音順から選ぶ":
    kana_filter = st.sidebar.selectbox("行を選んでね", ["あ行", "か行", "さ行", "た行", "な行", "は行", "ま行", "や行", "ら行", "わ行"])
    filtered_terms = [t for t, data in terms_db.items() if data["kana"] == kana_filter]
    
    if filtered_terms:
        selected_term = st.selectbox("該当する用語", filtered_terms)
    else:
        st.info("この行にはまだ用語が登録されていません。どんどん追加していきましょう！ズバリお任せください。")

elif search_mode == "アルファベット（A-Z）から選ぶ":
    initial_filter = st.sidebar.selectbox("頭文字を選んでね", ["C", "D", "P", "S", "W"])
    filtered_terms = [t for t, data in terms_db.items() if data["initial"] == initial_filter]
    
    if filtered_terms:
        selected_term = st.selectbox("該当する用語", filtered_terms)

else:
    selected_term = st.selectbox("すべての用語から選ぶ", list(terms_db.keys()))

# 選択された用語の解説を表示
if selected_term and selected_term in terms_db:
    item = terms_db[selected_term]
    
    st.markdown(f"### 📌 【{item['category']}】 {selected_term}")
    st.write(f"**一言で言うと**: {item['definition']}")
    st.info(f"💡 日常の例え：{item['analogy']}")
    
    if item['diagram']:
        st.text(f"【テキスト図解】\n{item['diagram']}")
        
    st.warning(f"⚠️ 引っ掛けポイント：{item['warning']}")
