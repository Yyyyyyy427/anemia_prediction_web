import tensorflow as tf
import numpy as np
import os

# 生成模拟数据（RGB 特征 + 标签）
data = np.random.rand(1000, 3)  # RGB 特征
labels = np.random.randint(0, 2, size=(1000,))  # 二分类标签

# 定义简单模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 编译和训练
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(data, labels, epochs=5, batch_size=32, verbose=1)

# 保存模型
os.makedirs('./anemia_model_files', exist_ok=True)
model.save('./anemia_model_files/anemia_model.h5')
print("Model saved!")
