# Super parameters
clamp = 2.0
channels_in = 3
log10_lr = -4.5
lr = 10 ** log10_lr
epochs = 1000
weight_decay = 1e-5
init_scale = 0.01

lamda_reconstruction = 5
lamda_guide = 1
lamda_low_frequency = 1
device_ids = [0]

# Train:
batch_size = 8
cropsize = 224
betas = (0.5, 0.999)
weight_step = 1000
gamma = 0.5
gradient_accumulation_steps=8

# Val:
cropsize_val = 1024
batchsize_val = 2
shuffle_val = False
val_freq = 50

#for Kaggle use this as path /kaggle/input/steganography-imagenet/steganography_dataset_imagenet/train

# Dataset
TRAIN_PATH = '/kaggle/input/steganography-imagenet/steganography_dataset_imagenet/train/'#'./data/imagenet/steganography_dataset_imagenet/train/' #/teamspace/studios/this_studio/HiNet-stego/data/imagenet/steganography_dataset_imagenet/train
VAL_PATH = '/kaggle/input/steganography-imagenet/steganography_dataset_imagenet/test/'
format_train = 'png'
format_val = 'jpeg'

# Display and logging:
loss_display_cutoff = 2.0
loss_names = ['L', 'lr']
silent = False
live_visualization = False
progress_bar = False


# Saving checkpoints:

MODEL_PATH = './output/model/'
checkpoint_on_error = True
SAVE_freq = 50

IMAGE_PATH = './output/image/'
IMAGE_PATH_cover = IMAGE_PATH + 'cover-valid/'
IMAGE_PATH_secret = IMAGE_PATH + 'secret-valid/'
IMAGE_PATH_steg = IMAGE_PATH + 'steg-valid/'
IMAGE_PATH_secret_rev = IMAGE_PATH + 'secret-rev-valid/'

# Load:
suffix = 'model.pt'
tain_next = True
trained_epoch = 500  # Update this to the epoch from which you want to resume

