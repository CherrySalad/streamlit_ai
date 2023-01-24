import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.applications.imagenet_utils import decode_predictions



resnet50_pre = tf.keras.applications.resnet.ResNet50(weights='imagenet', input_shape=(224, 224, 3))


# 웹 페이지

st.title('이미지 분류 인공지능 웹페이지')
file = st.file_uploader('이미지를 올려주세요', type=['jpg', 'png'])
### 사진 파일을 업로드 가능하게 해준다

## 웹 페이지 내 서비스
if file is None:
    st.text('이미지를 먼저 올려주세요')
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    ### 이미지를 노출시켜주는 함수이다
    img_resized = ImageOps.fit(image, (224, 224), Image.ANTIALIAS)
    img_resized = img_resized.convert('RGB')
    img_resized = np.asarray(img_resized)

    pred = resnet50_pre.predict(img_resized.reshape([1, 224, 224, 3]))
    decoded_pred = decode_predictions(pred)
    results = ''
    for i, instance in enumerate(decoded_pred[0]):
        results += f'{i+1}위 : {instance[1]} ({instance[2] * 100 : 0.2f})'
    st.success(results)
