__author__ = 'Noureldien'

from builtins import print

import CNN
import CNN.utils
import CNN.recog
import CNN.detec

print('Traffic Sign Recognition')

mnist_dataset = "D:\\_Dataset\\MNIST\\mnist.pkl"
gtsrb_dataset = "D:\\_Dataset\\GTSRB\\gtsrb_normalized.pkl"
belgiumTS_dataset = "D:\\_Dataset\\\BelgiumTS\\BelgiumTS_normalized_28.pkl"
superclass_dataset = "D:\\_Dataset\\SuperClass\\SuperClass_normalized.pkl"

gtsrb_model = 'D:\\_Dataset\\GTSRB\\cnn_model.pkl'
superclass_model = 'D:\\_Dataset\\SuperClass\\cnn_model.pkl'
superclass_model_svm = 'D:\\_Dataset\\SuperClass\\cnn_model_svm.pkl'

gtsdb_dataset = 'D:\\_Dataset\\GTSDB\\gtsdb_prohibitory_organized.pkl'
gtsdb_model = 'D:\\_Dataset\\GTSDB\\cnn_model.pkl'

gtsrb_dim = 28
mnist_dim = 28

# region Recognition

# train model on mnist database
# CNN.recog.train(dataset_path=mnist_dataset ,learning_rate=0.1, n_epochs=200, nkerns=(20, 50), batch_size=500)
# CNN.recog.train(dataset_path=mnist_dataset ,learning_rate=0.1, n_epochs=1, nkerns=(20, 50), batch_size=100)
# CNN.recog.train(dataset_path=mnist_dataset ,learning_rate=0.1, n_epochs=1, nkerns=(10, 20), batch_size=100) # 4.22%
# CNN.recog.train(dataset_path=mnist_dataset ,learning_rate=0.2, n_epochs=5, nkerns=(10, 20), batch_size=50) # 1.53%
# CNN.recog.train(dataset_path=mnist_dataset ,learning_rate=0.05, n_epochs=5, nkerns=(10, 20), batch_size=50) # 1.64%
# CNN.recog.train(dataset_path=mnist_dataset ,learning_rate=0.2, n_epochs=5, nkerns=(20, 50), batch_size=50) # 1.13%
# CNN.recog.train(dataset_path=mnist_dataset, learning_rate=0.2, n_epochs=1, kernel_dim=(5, 5), nkerns=(100, 200), mpl_layers=(500, 10), batch_size=50) # 1.98%
# CNN.recog.train(img_dim=mnist_dim, dataset_path=mnist_dataset, learning_rate=0.2, n_epochs=5, nkerns=[20, 50], batch_size=50)

# train model on gtsrb database
# CNN.recog.train(dataset_path=mnist_dataset, learning_rate=0.2, n_epochs=5, kernel_dim=(5, 5), nkerns=(100, 200), mpl_layers=(500, 10), batch_size=50)
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.1, n_epochs=5, nkerns=(20, 50), batch_size=50) # 3.73%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.2, n_epochs=1, nkerns=(20, 50), batch_size=50) # 3.35%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.1, n_epochs=5, nkerns=(40, 100), batch_size=50) # 3.06%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.2, n_epochs=5, nkerns=(40, 100), batch_size=50) # 2.77%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.2, n_epochs=5, nkerns=(40, 100), batch_size=50, mlp_layers=(800, 10)) # 3.12%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.2, n_epochs=1, nkerns=(20, 50), batch_size=50, mlp_layers=(500, 10)) # 4.77%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.2, n_epochs=1, nkerns=(20, 50), batch_size=50, mlp_layers=(100, 10)) # 5.06%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.2, n_epochs=1, nkerns=(20, 50), batch_size=50, mlp_layers=(200, 10)) # 4.31%
# CNN.recog.train(dataset_path=gtsrb_dataset, learning_rate=0.2, n_epochs=1, nkerns=[4, 10], batch_size=50, mlp_layers=(50, 10)) # 8.00%

# test model on specific image
# CNN.recog.classify_img_from_file("D:\\_Dataset\\GTSRB\\Final_Test_Preprocessed_28\\00412.png", gtsrb_model)
# CNN.recog.classify_img_from_file("D:\\_Dataset\\BelgiumTS\\Test_Scaled\\00031\\02656_00000.png", gtsrb_model, is_rgb=True)

# train model on gtsrb database
# cnn.evaluate_lenet5(img_dim=gtsrb_dim, dataset=gtsrb_dataset, learning_rate=0.1, n_epochs=5, kernel_dim=[5, 5], nkerns=[100, 200], mpl_layers=[500, 10], batch_size=50)

# train model on SuperClass database
# CNN.cnn.train(model_path=superclass_model, dataset_path=superclass_dataset, learning_rate=0.01, n_epochs=1, batch_size=2, nkerns=(8, 8*9), mlp_layers=(340, 3)) # 8.50%
# CNN.recog.train_cnn_svm(model_path=superclass_model_svm, dataset_path=superclass_dataset, learning_rate=0.01, n_epochs=1, batch_size=2, nkerns=(8, 8*9), mlp_layers=(500, 3)) # 5.01%

# test model on specific image
# CNN.cnn.classify_img_from_file("D:\\_Dataset\\SuperClass\\Test_Preprocessed_Revised\\00001\\00045_00004.png", superclass_model)

###### experiments ######x

# CNN.utils.rgb_to_gs_and_save("D:\\_Dataset\\UK\\preprocessed\\small 8.png")
# CNN.utils.preprocess_image(filePathRead="D:\\_Dataset\\UK\\preprocessed\\small.png", filePathWrite="D:\\_Dataset\\UK\\preprocessed\\small 1.png")

# CNN.cnn.classify_img_from_file("D:\\_Dataset\\UK\\preprocessed\\small 8.png", superclass_model)
# CNN.cnn.classify_img_from_file("D:\\_Dataset\\UK\\preprocessed\\small 8.png", superclass_model_svm, CNN.cnn.ClassifierType.svm)

# CNN.utils.probability_map("D:\\_Dataset\\UK\\preprocessed\\big 2.png", superclass_model)
# CNN.utils.probability_map("D:\\_Dataset\\UK\\preprocessed\\big 2.png", superclass_model_svm, CNN.cnn.ClassifierType.svm)

# endregion

# region Detection

# extract region images to train the detector
#CNN.utils.rerialize_gtsdb()
#CNN.utils.organize_gtsdb()

# train the detector
# CNN.detec.train(dataset_path=gtsdb_dataset, recognition_model_path=gtsrb_model, detection_model_path=gtsdb_model, batch_size=500, learning_rate=0.01, n_epochs=1) # 10.01%
# CNN.detec.train(dataset_path=gtsdb_dataset, recognition_model_path=gtsrb_model, detection_model_path=gtsdb_model, batch_size=100, learning_rate=0.1, n_epochs=1) # 7.48%
# CNN.detec.train(dataset_path=gtsdb_dataset, recognition_model_path=gtsrb_model, detection_model_path=gtsdb_model, batch_size=10, learning_rate=0.1, n_epochs=1) # 4.42%

#CNN.detec.train(dataset_path=gtsdb_dataset, recognition_model_path=gtsrb_model, batch_size=10, learning_rate=0.1, n_epochs=1)

# test the detector
#CNN.detec.detect_img_from_file(img_path="D:\\_Dataset\\GTSDB\\Test_PNG\\00025.png", model_path=gtsdb_model)
CNN.detec.detect_img_from_file(img_path="D:\\_Dataset\\GTSDB\\Test_PNG\\_img1.png", model_path=gtsdb_model)


# endregion
