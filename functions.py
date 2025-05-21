import tensorflow as tf
import numpy as np
# Define the num_to_char function
# Integers to original chaecters
import tensorflow ;

char_img = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

char_to_num = tensorflow.keras.layers.StringLookup(
    vocabulary=list(char_img), mask_token=None
)

num_to_char = tensorflow.keras.layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), mask_token=None, invert=True
)


def decode_batch_predictions(pred): 
    input_len = np.ones(pred.shape[0]) * pred.shape[1] 
    results = tf.keras.backend.ctc_decode(pred, 
                                       input_length=input_len, 
                                       greedy=True)[0][0][:, :5] 
    output_text = [] 
    for res in results: 
        res = tf.strings.reduce_join(num_to_char(res)).numpy().decode("utf-8") 
        output_text.append(res) 
    return output_text
