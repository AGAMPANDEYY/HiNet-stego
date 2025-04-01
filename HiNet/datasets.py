import glob
from PIL import Image
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as T
import config as c
from natsort import natsorted
import random


def to_rgb(image):
    rgb_image = Image.new("RGB", image.size)
    rgb_image.paste(image)
    return rgb_image


class Hinet_Dataset(Dataset):
    def __init__(self, transforms_=None, mode="train"):

        self.transform = transforms_
        self.mode = mode
        if mode == 'train':
            # train
            print(f"Train path: {c.TRAIN_PATH}")
            print(f"format of train is {c.format_train} ")
            self.files_cover = natsorted(glob.glob(c.TRAIN_PATH + "/cover/*.JPEG", recursive=True))
            self.files_secret=natsorted(glob.glob(c.TRAIN_PATH + "/secret/*.JPEG", recursive=True))
            # Randomly select 500 images from each
            self.files_cover = random.sample(self.files_cover, min(500, len(self.files_cover)))
            self.files_secret = random.sample(self.files_secret, min(500, len(self.files_secret)))
            
            # Combine lists, ensuring equal length
            min_len = min(len(self.files_cover), len(self.files_secret))
            self.files_cover = self.files_cover[:min_len]
            self.files_secret = self.files_secret[:min_len]
            
            # Combine cover and secret lists
            self.files = self.files_cover + self.files_secret
            
            print(f"Selected {len(self.files)} images for training.")

        else:
            # test
            self.files = sorted(glob.glob(c.VAL_PATH + "/*." + c.format_val))

    def __getitem__(self, index):
        try:
            image = Image.open(self.files[index])
            image = to_rgb(image)
            item = self.transform(image)
            return item

        except:
            return self.__getitem__(index + 1)

    def __len__(self):
        if self.mode == 'shuffle':
            return max(len(self.files_cover), len(self.files_secret))

        else:
            return len(self.files)


transform = T.Compose([
    T.RandomHorizontalFlip(),
    T.RandomVerticalFlip(),
    T.RandomCrop(c.cropsize),
    T.ToTensor()
])

transform_val = T.Compose([
    T.CenterCrop(c.cropsize_val),
    T.ToTensor(),
])


# Training data loader
trainloader = DataLoader(
    Hinet_Dataset(transforms_=transform, mode="train"),
    batch_size=c.batch_size,
    shuffle=True,
    pin_memory=True,
    num_workers=2,
    drop_last=True
)
# Test data loader
testloader = DataLoader(
    Hinet_Dataset(transforms_=transform_val, mode="val"),
    batch_size=c.batchsize_val,
    shuffle=False,
    pin_memory=True,
    num_workers=1,
    drop_last=True
)