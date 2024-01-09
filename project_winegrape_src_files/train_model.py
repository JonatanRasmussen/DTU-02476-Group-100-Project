from pytorch_lightning import Trainer, seed_everything

from data.data import DataModule
from models.model import ImageClassifier
from torchvision import transforms 

def main():
    """
    Python script used to train and validate deep learning models.
    The models are trained with the data from the grapevine leaves image dataset.
    """
    
    # Seeding for reproducibility
    seed_everything(123)

    #-----------------------------------------------------------
    # Setting up the data
    data_module = DataModule(transform_level='light')
    data_module.setup()

    #-----------------------------------------------------------
    # Choosing a model
    model = ImageClassifier(
        model_name='efficientnet_b0',
        #model_name = 'resnetv2_50t',
        num_classes=5,
        drop_rate=0.3,
        pretrained=True,
        lr_pretrained=1e-5,
        lr_final=1e-4,
        optimizer="AdamW",
        criterion='cross_entropy',
    )


    #-----------------------------------------------------------
    # Training the model
    trainer = Trainer(
        max_epochs = 40,
        log_every_n_steps = 40
    )

    trainer.fit(model,
        data_module.train_dataloader(),
        data_module.val_dataloader()
    )

    #-----------------------------------------------------------
    # Testing model
    trainer.test(dataloaders = data_module.test_dataloader())

if __name__=="__main__":
    # Optional to see the list of models.
    # print(timm.models.list_models())

    main()