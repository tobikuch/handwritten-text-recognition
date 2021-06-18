import tensorflow as tf

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model("../output/iam/puigcerver/") # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('../output/model.tflite', 'wb') as f:
  f.write(tflite_model)
