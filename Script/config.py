root = '../'

# Model
input_shape = (256, 256, 3)  # Height, Width, Channel
output_shape = 7

# Dataset
train_batch = root + 'Dataset/train-batch/'
val_batch = root + 'Dataset/val-batch/'
test_batch = root + 'Dataset/test-batch/'

# Resources
dir_model_saved = root + 'Resources/model_saved/'
dir_model_plot = root + 'Resources/model_plot/'
dir_model_summary = root + 'Resources/model_summary/'
dir_haarcascade = root + 'Resources/haarcascade/'
dir_video = root + 'Resources/video/'

# Output Description
facial_expression = {
    0 : 'angry',
    1 : 'disgust',
    2 : 'fear',
    3 : 'happy',
    4 : 'sad',
    5 : 'surprise',
    6 : 'neutral'
}

facial_expression_rev = dict()
for key in facial_expression:
    facial_expression_rev[facial_expression[key]] = key
    
facial_expression_color_bgr = {
    0 : (101,85,236),
    1 : (83,110,242),
    2 : (208,152,103),
    3 : (85,206,255),
    4 : (166,193,91),
    5 : (184,136,231),
    6 : (250,247,244)
}

assert(len(facial_expression) == output_shape)
assert(len(facial_expression) == len(facial_expression_rev))