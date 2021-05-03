import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Data Frame')

df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']

)

st.map(df)

option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください. ',
    list(range(1, 11))
)

condition = st.sidebar.slider(
    'あなたの今の調子は？', 0, 100, 50
)

'あなたの好きな数字は', option, 'です'
'コンディション：', condition

left_column, right_column = st.beta_columns(2)
button = left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右からむ')

# if st.checkbox('Show Image'):
#     st.write('Display Image')
#     img = Image.open('sample.png')

#     st.image(img, caption='Kohei Imanishi', use_column_width=True)