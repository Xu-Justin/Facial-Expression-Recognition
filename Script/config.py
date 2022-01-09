root = '../'

# Model
input_shape = (256, 256, 3)  # Height, Width, Channel
output_shape = 7

# Dataset
dir_dataset_raw = root + 'Dataset/raw/'
dir_dataset_train = root + 'Dataset/train/'
dir_dataset_val = root + 'Dataset/val/'
dir_dataset_test = root + 'Dataset/test/'

# Resources
dir_resources = root + 'Resources/'

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
