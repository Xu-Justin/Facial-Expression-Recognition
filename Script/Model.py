from tensorflow import keras
from config import input_shape, output_shape

data_augmentation = keras.Sequential(
    [
        keras.layers.RandomFlip(mode='horizontal'),
        keras.layers.RandomZoom(height_factor=(-0.1,0.1)),
        keras.layers.RandomTranslation(height_factor=(-0.1,0.1), width_factor=(-0.1,0.1)),
        keras.layers.RandomRotation(factor = (0.1))
    ]
)

def create_model():
    print('Creating new model...', end='\r')
    
    Resnet_base = keras.applications.resnet50.ResNet50(include_top=False, input_shape=input_shape)
    for layer in Resnet_base.layers:
        layer.trainable = False
    
    input_layer = keras.Input(shape=input_shape)
    Resnet = keras.applications.resnet.preprocess_input(input_layer)
    Resnet = Resnet_base(Resnet)
    Resnet = keras.layers.GlobalAveragePooling2D()(Resnet)
    
    block_1_dn = keras.layers.Dense(units=4096)(Resnet)
    block_1_bn = keras.layers.BatchNormalization()(block_1_dn)
    block_1_act = keras.layers.Activation(keras.activations.relu)(block_1_bn)
    block_1_out = keras.layers.Dropout(0.5)(block_1_act)
    
    block_2_dn = keras.layers.Dense(units=2048)(block_1_out)
    block_2_bn = keras.layers.BatchNormalization()(block_2_dn)
    block_2_act = keras.layers.Activation(keras.activations.relu)(block_2_bn)
    block_2_out = keras.layers.Dropout(0.5)(block_2_act)
    
    output_layer = keras.layers.Dense(units=output_shape, activation='softmax')(block_2_out)
    
    model=keras.Model(inputs=[input_layer],outputs=[output_layer])
    model.compile(loss='categorical_crossentropy', optimizer=keras.optimizers.Adam(learning_rate=3e-4), metrics=['accuracy'])
    
    print('Successfully created new model.')
    return model

def load_model(dir):
    print('Loading model from %s'%dir, end='\r')
    model = keras.models.load_model(dir)
    print('Successfully loaded model from %s'%dir)
    return model

def save_model(dir, model):
    print('Saving model to %s'%dir, end='\r')
    model.save(dir)
    print('Successfully saved model to %s'%dir)

def save_plot(dir, model):
    print('Saving model plot to %s'%dir, end='\r')
    keras.utils.plot_model(model,dir, show_shapes=True)
    print('Successfully saved model plot to %s'%dir)

if __name__ == '__main__':
    model = create_model()
    model.summary()
    save_plot("model_plot.png", model)