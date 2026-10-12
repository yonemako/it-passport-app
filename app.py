import streamlit as st

st.title("🧠 ITパスポート 魔法の暗記アプリ（完全版）")
st.write("試験に出る重要用語を網羅！頭文字や行をタップしてサクッと暗記しよう！")

# 拡張された完全版用語データベース
terms_db = {
    # --- セキュリティ・ネットワーク (アルファベット) ---
    "Cookie（クッキー）": {
        "kana": "か行", "initial": "C", "category": "セキュリティ",
        "definition": "ネット上の『私の身分証・おぼえ書きタグ』",
        "analogy": "常連のカフェで店員さんが「いつものね！」と覚えていてくれるようなもの。",
        "diagram": "[スマホ] ── 1回目ログイン ──> [Webサーバー]\n         <── Cookieを預かる ──┘",
        "warning": "サーバー側ではなく、自分のブラウザ（手元）に保存されます！"
    },
    "DNS（Domain Name System）": {
        "kana": "", "initial": "D", "category": "ネットワーク",
        "definition": "ネット上の『電話帳』",
        "analogy": "『Amazonに行きたい！』と入力したとき、裏で数字の住所（IPアドレス）に変換して案内してくれる親切な案内人。",
        "diagram": "（文字のドメイン名） ── DNS ──> （数字のIPアドレス）",
        "warning": "ドメイン名からIPアドレスに変換するのがDNSの役割です。"
    },
    "WBS（Work Breakdown Structure）": {
        "kana": "", "initial": "W", "category": "マネジメント",
        "definition": "プロジェクトの『巨大なスイカの解体マップ』",
        "analogy": "大きな仕事を小さなパーツに細かく分解して、誰が・いつまでにやるかを整理する設計図。",
        "diagram": "プロジェクト全体 ──> 大タスク ──> 中タスク",
        "warning": "スケジュールを作る「前」に、作業を階層的に分解する作業です。"
    },
    "CPUとメモリ（主記憶装置）": {
        "kana": "さ行", "initial": "C", "category": "テクノロジ",
        "definition": "「職人（CPU）」と「作業机（メモリ）」",
        "analogy": "CPUは頭脳（料理人）、メモリは調理台の広さ。調理台が広いほど同時にたくさん作業できます。",
        "diagram": "[CPU（頭脳）] ⇄ [メモリ（一時的な机）]",
        "warning": "電源を切るとメモリの中身はすべて消えます（揮発性）！"
    },
    "SQL（Structured Query Language）": {
        "kana": "", "initial": "S", "category": "テクノロジ",
        "definition": "データベースにお願いをするための『専用の呪文』",
        "analogy": "図書館の検索システムで「本を全部出して！」と司書さんにお願いする言葉のようなもの。",
        "diagram": "[ユーザー] ── SQL（命令文） ──> [データベース]",
        "warning": "データベースを「管理するソフト」ではなく、命令を出す「言語」の名前です。"
    },
    "ペネトレーションテスト": {
        "kana": "は行", "initial": "P", "category": "セキュリティ",
        "definition": "本物のハッカーになりきって『セキュリティの弱点』を探す模擬攻撃",
        "analogy": "自宅の鍵が本当に泥棒に破られないか、専門の鍵師に頼んでわざとピッキングしてもらうようなもの。",
        "diagram": "[攻撃者役] ── 模擬ハッキング ──> [システム]",
        "warning": "単なる自動ツールではなく、実際に侵入を試みる高度なテストです。"
    },
    "IoT（Internet of Things）": {
        "kana": "", "initial": "I", "category": "テクノロジ",
        "definition": "あらゆるモノがインターネットに繋がる仕組み",
        "analogy": "エアコンや冷蔵庫がネットと繋がり、外出先からスマホで操作できるようになること。",
        "diagram": "[家電・センサー] ── ネット接続 ──> [スマホ・クラウド]",
        "warning": "パソコンだけでなく、車や家電など「モノ」が主役です。"
    },
    "RPA（Robotic Process Automation）": {
        "kana": "", "initial": "R", "category": "ストラテジ",
        "definition": "ソフトウェアの『ロボットによる業務自動化』",
        "analogy": "人間の代わりに、パソコン上の定型作業（コピペやデータ入力）を爆速でこなしてくれるデジタル社員。",
        "diagram": "[RPAロボット] ── 自動操作 ──> [Excel・Webブラウザ]",
        "warning": "物理的なロボットではなく、PC上で動くソフトウェアのことです。"
    },
    "SaaS（Software as a Service）": {
        "kana": "", "initial": "S", "category": "テクノロジ",
        "definition": "ネット経由で利用する『ソフトウェアのレンタルサービス』",
        "analogy": "CDを買ってインストールするのではなく、動画配信サブスクのようにネット越しにアプリを使う仕組み（Google WorkspaceやGmailなど）。",
        "diagram": "[クラウド上のアプリ] ── ネット ──> [手元の端末]",
        "warning": "利用者がインフラやOSを管理する必要はありません。"
    },

    # --- 日本語用語 (50音順) ---
    "アジャイル開発": {
        "kana": "あ行", "initial": "A", "category": "マネジメント",
        "definition": "「短いサイクルで実装・テストを繰り返す」柔軟な開発手法",
        "analogy": "全体を一気に作らず、まずは動くミニチュアを作って見せ合いながら軌道修正していく方法。",
        "diagram": "計画 ⇄ 設計 ⇄ 実装 ⇄ テスト（これを高速で回す）",
        "warning": "最初にカチッとした全体計画を作らないため、仕様変更に強い反面、全体像が見えにくい特徴があります。"
    },
    "ウォータフォール開発": {
        "kana": "わ行", "initial": "W", "category": "マネジメント",
        "definition": "「上流から下流へ滝のように順番に進める」伝統的な開発手法",
        "analogy": "家を建てる時と同じように、設計図を完璧に作ってから、順番に工事を進めていく方法。",
        "diagram": "要件定義 ➔ 外部設計 ➔ 内部設計 ➔ プログラミング ➔ テスト",
        "warning": "途中で「やっぱり部屋を増やしたい」という仕様変更をするのが非常に難しいです。"
    },
    "ガントチャート": {
        "kana": "か行", "initial": "G", "category": "マネジメント",
        "definition": "横軸に「時間」、縦軸に「作業内容」をとったスケジュール表",
        "analogy": "夏休みの計画表のように、「いつからいつまでにどの宿題をやるか」がひと目で分かる表。",
        "diagram": "作業A [████░░░░]\n作業B [░░████░░]",
        "warning": "作業同士の「依存関係（どれが終わらないと次に進めないか）」が分かりにくい弱点があります。"
    },
    "サプライチェーンマネジメント（SCM）": {
        "kana": "さ行", "initial": "S", "category": "ストラテジ",
        "definition": "調達から販売までの流れを全体最適化する経営手法",
        "analogy": "原材料の仕入れ、工場での製造、物流、店舗での販売までをチーム一丸となって無駄なく管理すること。",
        "diagram": "調達 ➔ 製造 ➔ 流通 ➔ 販売 ➔ 顧客",
        "warning": "自社だけでなく、サプライヤーや小売店とも情報を共有するのがポイントです。"
    },
    "フィッシング詐欺": {
        "kana": "は行", "initial": "P", "category": "セキュリティ",
        "definition": "本物そっくりの偽サイトに誘導して個人情報を盗み出す手口",
        "analogy": "釣り針（Fishing）を垂らして、引っかかった人からパスワードや暗証番号を釣り上げる悪質な罠。",
        "diagram": "[偽メール・SMS] ➔ [そっくりな偽サイト] ➔ [個人情報詐取]",
        "warning": "URLが本物と微妙に違う（例：jpがbzになっている等）特徴があります。"
    }
}

# 探すモードの選択
mode = st.radio("🔤 探す方式を選ぶ", ["50音順から探す", "アルファベット（A-Z）から探す"], horizontal=True)

if mode == "50音順から探す":
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
                st.caption("（この行の登録用語は準備中です。随所追加できます！）")

else:
    active_initials = ["A", "C", "D", "G", "I", "P", "R", "S", "W"]
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
                st.caption("（登録用語は準備中です）")

# 選択された用語の詳細表示
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
