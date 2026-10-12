import streamlit as st

st.title("🧠 ITパスポート 魔法の暗記アプリ")
st.write("頭文字や行をタップして、知りたい用語をスマートに引き出そう！")

# 用語データベース
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
        "analogy": "CPUはバリバリ働く料理人、メモリは一度に広げられる調理台の広さ。",
        "diagram": "[CPU（頭脳・処理）] ⇄ [メモリ（一時的な机）]",
        "warning": "電源を切るとメモリの中身はすべて消えます（揮発性）！"
    },
    "SQL": {
        "kana": "さ行",
        "initial": "S",
        "category": "データベース",
        "definition": "データベースにお願いをするための『専用の呪文』",
        "analogy": "図書館の検索システムで「本を全部出して！」と司書さんにお願いする言葉のようなもの。",
        "diagram": "[ユーザー] ── SQL（命令文） ──> [データベース]",
        "warning": "データベースを「管理するソフト」ではなく、命令を出す「言語」の名前です。"
    },
    "ペネトレーションテスト": {
        "kana": "は行",
        "initial": "P",
        "category": "セキュリティ",
        "definition": "本物のハッカーになりきって『セキュリティの弱点』を探す模擬攻撃",
        "analogy": "自宅の鍵が本当に泥棒に破られないか、専門の鍵師に頼んでわざとピッキングしてもらうようなもの。",
        "diagram": "[攻撃者役] ── 模擬ハッキング ──> [システム]",
        "warning": "単なる自動の脆弱性診断ツールではなく、実際に侵入を試みる高度なテストです。"
    }
}

# 探すモードの選択（50音順かアルファベット順か）
mode = st.radio("🔤 探す方式を選ぶ", ["50音順から探す", "アルファベット（A-Z）から探す"], horizontal=True)

selected_term = None

if mode == "50音順から探す":
    # 50音の行タブを作成
    kana_tabs = st.tabs(["あ行", "か行", "さ行", "た行", "な行", "は行", "ま行", "や行", "ら行", "わ行"])
    kana_list = ["あ行", "か行", "さ行", "た行", "な行", "は行", "ま行", "や行", "ら行", "わ行"]
    
    for i, tab in enumerate(kana_tabs):
        with tab:
            current_kana = kana_list[i]
            matched = [t for t, d in terms_db.items() if d["kana"] == current_kana]
            if matched:
                st.write(f"【{current_kana}】の用語一覧:")
                for term in matched:
                    if st.button(term, key=f"btn_{term}"):
                        st.session_state["active_term"] = term
            else:
                st.caption("（この行の登録用語はまだありません）")

else:
    # アルファベットのタブを作成
    initials = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # 登録されている頭文字だけに絞るか、すべて並べるか（ここではスッキリ見せるため主要なものをタブに）
    active_initials = ["C", "D", "P", "S", "W"]
    alpha_tabs = st.tabs(active_initials)
    
    for i, tab in enumerate(alpha_tabs):
        with tab:
            cur_init = active_initials[i]
            matched = [t for t, d in terms_db.items() if d["initial"] == cur_init]
            if matched:
                st.write(f"頭文字【{cur_init}】の用語一覧:")
                for term in matched:
                    if st.button(term, key=f"btn_alpha_{term}"):
                        st.session_state["active_term"] = term
            else:
                st.caption("（登録用語はまだありません）")

# タップされて保持している用語があれば詳細を表示
if "active_term" in st.session_state:
    term = st.session_state["active_term"]
    if term in terms_db:
        item = terms_db[term]
        st.divider()
        st.markdown(f"### 📌 【{item['category']}】 {term}")
        st.write(f"**一言で言うと**: {item['definition']}")
        st.info(f"💡 日常の例え：{item['analogy']}")
        if item['diagram']:
            st.text(f"【テキスト図解】\n{item['diagram']}")
        st.warning(f"⚠️ 引っ掛けポイント：{item['warning']}")
