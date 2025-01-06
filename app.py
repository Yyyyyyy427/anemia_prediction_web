from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# 加载模型
model = tf.keras.models.load_model('./anemia_model_files/anemia_model.h5')

@app.route('/')
def home():
    return "Flask service is running!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'result': 'No image uploaded'}), 400

    try:
        # 处理上传的图片
        image = Image.open(request.files['image']).resize((224, 224))  # 替换为模型输入尺寸
        image_array = np.array(image) / 255.0  # 归一化
        image_array = np.expand_dims(image_array, axis=0)

        # 模型预测
        prediction = model.predict(image_array)
        result = 'Anemic' if prediction[0][0] > 0.5 else 'Not Anemic'

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
