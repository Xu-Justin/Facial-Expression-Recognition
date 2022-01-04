from tensorflow import keras
from config import input_shape, output_shape

def create_model():
    print('Creating new model...', end='\r')
    Resnet_base = keras.applications.resnet50.ResNet50(include_top=False, input_shape=input_shape)
    for layer in Resnet_base.layers:
        layer.trainable = False
    
    input_layer = keras.Input(shape=input_shape)
    Resnet = keras.applications.resnet.preprocess_input(input_layer)
    Resnet = Resnet_base(Resnet)
    Resnet = keras.layers.GlobalAveragePooling2D()(Resnet)
    
    block_1_dn = keras.layers.Dense(units=16)(Resnet)
    block_1_bn = keras.layers.BatchNormalization()(block_1_dn)
    block_1_out = keras.layers.Activation(keras.activations.relu)(block_1_bn)
    
    dropout = keras.layers.Dropout(0.4)(block_1_out)
    
    output_layer = keras.layers.Dense(units=output_shape, activation='softmax')(dropout)
    
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
    
if __name__ == '__main__':
    model = create_model()
    model.summary()
    keras.utils.plot_model(model,"model_plot.png", show_shapes=True)
