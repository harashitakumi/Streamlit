import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 入門講座")

st.write("基礎")
"Start!!"

#空の要素を追加
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.05) #時間を止める(0.1秒ごとに1進んでいく)

"Done!!!!!"

#2カラムレイアウト
left_column, rigth_column = st.columns(2)
button = left_column.button("右カラムに文字を表示ボタン")
if button:
    rigth_column.write("ここは右カラムです")

#expanderの追加
expander = st.expander("問い合わせ1")
expander.write("問い合わせ1回答")
expander = st.expander("問い合わせ2")
expander.write("問い合わせ2回答")
expander = st.expander("問い合わせ3")
expander.write("問い合わせ3回答")

#スライダー
condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50) #最小値、最大値、はじめの値
"あなたの今のコンディションは", condition

#テキスト入力
option1 = st.sidebar.text_input("あなたの好きなキャラクターを教えてください")
"あなたの好きなキャラクターは、", option1, "です"

#セレクトボックス
option = st.sidebar.selectbox(
    "好きな数字を教えてください",
    list(range(1, 11))
)
"あなたの好きな数字は、", option, "です"

#画像表示
if st.checkbox("はえてくることり"):
    img = Image.open("39484196_p0_square1200.jpg")
    st.image(img, caption = "はえてくることり", use_column_width = True)

audio_file = open("background.wav", "rb")
audio_bytes = audio_file
st.audio(audio_bytes, format = "audio/wav")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})
st.table(df.style.highlight_max(axis=0))

"""
# 春
## 夏
### 秋
#### 冬

```python
print("こんにちは")
print(810)
```
"""

df1 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = [1, 2, 3]
)
st.bar_chart(df1)

#新宿あたりのマップをプロット
df2 = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 137.70],
    columns = ["lat", "lon"]
)
st.map(df2)