import torch
import torch.nn as nn
import pytorch_lightning as pl
from torchmetrics.classification import Accuracy
import timm

class ImageClassifier(pl.LightningModule):
    def __init__(
            self,
            model_name='efficientnet_es.ra_in1k',
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

        self.log('val_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('val_accuracy', accuracy, on_step=True, on_epoch=True, prog_bar=True, logger=True)
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