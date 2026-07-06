import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("waste_model.h5")

# Check model structure
model.summary()