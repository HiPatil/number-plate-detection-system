from Enet import *
from data_processing import *
from keras.callbacks import TensorBoard
from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True


data_gen_args = dict()
tensorboard = TensorBoard(log_dir='./logs_regis_plate')

car = trainGenerator(8,'/home/himanshu/dl/number_plate_detection/Enet/data/train','images','masks',data_gen_args,image_color_mode = "rgb", target_size = (512,512), save_to_dir = None)
model = Enet()

model_checkpoint = ModelCheckpoint('/home/himanshu/dl/number_plate_detection/Enet/regis_plate.hdf5', monitor = 'loss', verbose=1, save_best_only=True)
model.fit_generator(car, steps_per_epoch = 370, epochs = 50, callbacks = [tensorboard,model_checkpoint])
