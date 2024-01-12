import torch
import torch.nn as nn
import torch.nn.functional as F

import pytorch_lightning as pl
from torchmetrics.classification import Accuracy
import timm


class ImageClassifier(pl.LightningModule):
    def __init__(
            self,
            model_name='efficientnet_b0',
            num_classes=5,
            drop_rate=0.5,
            pretrained=False,
            lr_pretrained=None,
            lr_final=None,
            optimizer=None,
            criterion=None,
            ):
        super(ImageClassifier, self).__init__()

        self.model = timm.create_model(
            model_name, 
            pretrained=pretrained, 
            num_classes=num_classes,
            drop_rate=drop_rate
            )
        
        self.lr_pretrained = lr_pretrained
        self.lr_final = lr_final
        self.optimizer = optimizer

        if criterion == 'cross_entropy':
            self.criterion = nn.CrossEntropyLoss()
        else:
            self.criterion = nn.CrossEntropyLoss()
        
        self.calc_accuracy = Accuracy(task="multiclass", num_classes=num_classes)

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)

        preds = torch.argmax(logits, dim=1)

        accuracy = self.calc_accuracy(preds, y)

        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('train_accuracy', accuracy, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss


    def validation_step(self, batch):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)

        preds = torch.argmax(logits, dim=1)

        accuracy = self.calc_accuracy(preds, y)

        self.log('val_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('val_accuracy', accuracy, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss


    def test_step(self,batch):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)

        preds = torch.argmax(logits, dim=1)

        accuracy = self.calc_accuracy(preds, y)

        self.log('test_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('test_accuracy', accuracy, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss


    def configure_optimizers(self):
        # Separate the parameters of the pre-trained model and the newly added final layer
        pre_trained_params = []
        final_layer_params = []
        for name, param in self.model.named_parameters():
            if name.startswith('model.classifier'):
                final_layer_params.append(param)
            else:
                pre_trained_params.append(param)

        # Create two parameter groups with different learning rates
        optimizer_groups = [
            {'params': pre_trained_params, 'lr': self.lr_pretrained},
            {'params': final_layer_params, 'lr': self.lr_final}
        ]

        # Initialize the optimizer with these parameter groups
        if self.optimizer == 'Adam':
            optimizer = torch.optim.Adam(optimizer_groups)
        elif self.optimizer == 'AdamW':
            optimizer = torch.optim.AdamW(optimizer_groups)
        elif self.optimizer == 'SGD':
            optimizer = torch.optim.SGD(optimizer_groups)
        else:
            optimizer = torch.optim.AdamW(optimizer_groups)
            
        return optimizer
    
class My_CNN(nn.Module):
    def __init__(self,num_classes):
        
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
        self.conv4 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3)

        self.pool = nn.MaxPool2d(2,2)

        self.fc1 = nn.Linear(128 * 12 * 12, 200)
        self.fc2 = nn.Linear(200, 40)
        self.fc3 = nn.Linear(40, num_classes)


    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv4(x)))
        
        x = torch.flatten(x,1)
        
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))

        return x


class CNN_Model(pl.LightningModule):
    def __init__(
            self,
            num_classes=5,
            #drop_rate=0.5,
            lr=None,
            optimizer=None,
            criterion=None
            ):
        super(CNN_Model, self).__init__()

        self.model = My_CNN(num_classes=num_classes)

        self.lr =lr
        self.optimizer = optimizer

        if criterion == 'cross_entropy':
            self.criterion = nn.CrossEntropyLoss()
        else:
            self.criterion = nn.CrossEntropyLoss()
        
        self.calc_accuracy = Accuracy(task="multiclass", num_classes=num_classes)

    def forward(self,x):
        return self.model(x)
        
    def training_step(self, batch):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)

        preds = torch.argmax(logits, dim=1)

        accuracy = self.calc_accuracy(preds, y)

        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('train_accuracy', accuracy, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss


    def validation_step(self, batch):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)

        preds = torch.argmax(logits, dim=1)

        accuracy = self.calc_accuracy(preds, y)

        self.log('val_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('val_accuracy', accuracy, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss


    def test_step(self,batch):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)

        preds = torch.argmax(logits, dim=1)

        accuracy = self.calc_accuracy(preds, y)

        self.log('test_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('test_accuracy', accuracy, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss


    def configure_optimizers(self):
        # Separate the parameters of the pre-trained model and the newly added final layer
        optimizer_groups = [{'params': self.model.parameters(), 'lr': self.lr}]
        
        # Initialize the optimizer with these parameter groups
        if self.optimizer == 'Adam':
            optimizer = torch.optim.Adam(optimizer_groups)
        elif self.optimizer == 'AdamW':
            optimizer = torch.optim.AdamW(optimizer_groups)
        elif self.optimizer == 'SGD':
            optimizer = torch.optim.SGD(optimizer_groups)
        else:
            optimizer = torch.optim.AdamW(optimizer_groups)
                    
        return optimizer