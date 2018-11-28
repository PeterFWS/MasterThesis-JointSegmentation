import Models 
import LoadBatches

# Global parameters
train_images_path = "./data/images_prepped_train/"
train_segs_path = "./data/annotations_prepped_train/"
save_weights_path = "./weights/ex1"

input_height = 512  #8708
input_width = 512  #11608
n_classes = 11
train_batch_size = 1
epochs = 3

validate = False

# Compile model
m = Models.Segnet.segnet(n_classes, input_height=input_height, input_width=input_width)
m.compile(loss="categorical_crossentropy",
      optimizer="adadelta",
      metrics=["accuracy"])
# m.load_weights("./data/vgg16_weights_th_dim_ordering_th_kernels.h5")


G = LoadBatches.imageSegmentationGenerator( train_images_path , train_segs_path ,  train_batch_size,  n_classes , input_height , input_width , input_height , input_width   )


if validate:
	val_images_path = "./data/images_prepped_test/"
	val_segs_path = "./data/annotations_prepped_test/"
	val_batch_size = 2

	G2 = LoadBatches.imageSegmentationGenerator( val_images_path , val_segs_path ,  val_batch_size,  n_classes , input_height , input_width , input_height , input_width   )
	
	for ep in range( epochs ):
		m.fit_generator( G , 512  , validation_data=G2 , validation_steps=200 ,  epochs=1 )
		m.save_weights( save_weights_path + "." + str( ep )  )
		m.save( save_weights_path + ".model." + str( ep ) )

else:
	for ep in range( epochs ):
		m.fit_generator( G , steps_per_epoch=512  , epochs=1 )  #12 // train_batch_size
		m.save_weights( save_weights_path + "." + str( ep ) )
		m.save( save_weights_path + ".model." + str( ep ) )
