import torch
import os
import numpy as np
from pathlib import Path
from pytorch_lightning import LightningDataModule

from torchvision import transforms, datasets
from torch.utils.data import DataLoader, Subset

class DataModule(LightningDataModule):
    
    def __init__(
            self,
            data_dir="data/raw/grapevine-leaves-image-dataset/Grapevine_Leaves_Image_Dataset",
            transform_level=None,
            img_size = 224,
            batch_size=8,
            val_split = 0.2,
            num_workers = 0
        ):
        super().__init__()
        self.root_dir = Path(data_dir)
        self.transform_level = transform_level
        self.img_size = img_size
        self.batch_size = batch_size
        self.val_split = val_split
        self.num_workers = num_workers

        self.transform_val,self.transform_train = self.which_transform()

    def which_transform(self):

        basic_transformation = [
            transforms.Resize(self.img_size),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])
        ]

        if self.transform_level == 'light':
            data_transform = [
                transforms.RandomHorizontalFlip(),
                transforms.RandomVerticalFlip()
            ]
        elif self.transform_level == 'moderate':
            data_transform = [
                transforms.RandomHorizontalFlip(),
                transforms.RandomVerticalFlip(),
                transforms.RandomRotation(degrees = (5,15))
            ]
        elif self.transform_level == 'heavy':
            data_transform = [
                transforms.RandomHorizontalFlip(),
                transforms.RandomVerticalFlip(),
                transforms.RandomAffine(degrees = (20,70),translate = (0.05,0.15), scale = (0.8,0.9))
            ]
        else:
            data_transform = None
        
        return transforms.Compose(basic_transformation),transforms.Compose(basic_transformation + data_transform)

    def setup(self, stage=None):

        train_dataset = datasets.ImageFolder(root=self.root_dir, transform=self.transform_train)
        val_dataset = datasets.ImageFolder(root=self.root_dir, transform=self.transform_val)
        
        n_data = len(train_dataset)
        
        split_idx = int(np.floor(self.val_split * n_data)) 
        indices = torch.randperm(n_data)
    
        train_dataset = Subset(train_dataset, indices[split_idx:])
        val_dataset = Subset(val_dataset, indices[:split_idx]) 
        val_dataset, test_dataset = torch.utils.data.random_split(val_dataset, [0.8, 0.2])

        self.train_dataset = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True, num_workers = self.num_workers)
        self.val_dataset = DataLoader(val_dataset, batch_size=self.batch_size, shuffle = False, num_workers = self.num_workers)
        self.test_dataset = DataLoader(test_dataset, batch_size=len(test_dataset), shuffle = False, num_workers = self.num_workers)

    def train_dataloader(self):
        return self.train_dataset

    def val_dataloader(self):
        return self.val_dataset
    
    def test_dataloader(self):
        return self.test_dataset