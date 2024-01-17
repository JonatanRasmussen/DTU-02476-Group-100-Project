from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.loggers import WandbLogger
from pytorch_lightning.callbacks import ModelCheckpoint

from data.data import DataModule
from models.model import ImageClassifier,CNN_Model

import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config2")
def main(cfg : DictConfig):
    """
    Python script used to train and validate deep learning models.
    The models are trained with the data from the grapevine leaves image dataset.
    """

    print(f"Configuration: \n {OmegaConf.to_yaml(cfg)}")

    # Seeding for reproducibility
    seed_everything(cfg.reproducibility.seed)
    
    #-----------------------------------------------------------
    # Setting up the data
    data_module = DataModule(
        data_dir=cfg.data.dir,
        transform_level=cfg.data.transform_level,
        img_size=224,
        batch_size=cfg.data.batch_size,
        val_split=cfg.data.val_split,
        num_workers=cfg.data.num_workers
    )
    data_module.setup()

    #-----------------------------------------------------------
    # Choosing a model

    if cfg.model.model_name=="CNN":
        model = CNN_Model(
            num_classes=cfg.model.num_classes,
            lr = cfg.optimization.lr,
            optimizer=cfg.optimization.optimizer,
            criterion=cfg.optimization.criterion
        )

    else:
        model = ImageClassifier(
            model_name=cfg.model.model_name,
            num_classes=cfg.model.num_classes,
            drop_rate=cfg.model.drop_rate,
            pretrained=cfg.model.pretrained,
            lr_pretrained=cfg.optimization.lr_pretrained,
            lr_final=cfg.optimization.lr_final,
            optimizer=cfg.optimization.optimizer,
            criterion=cfg.optimization.criterion,
        )

    #-----------------------------------------------------------
    # Training the model
    trainer = Trainer(
        max_epochs = cfg.training.max_epochs,
        logger=WandbLogger(name=cfg.model.model_name, project=cfg.logging.wandb_project),
        log_every_n_steps = cfg.logging.log_every_n_steps,
        callbacks=[
            ModelCheckpoint(
                dirpath="checkpoints/",
                filename=cfg.model.model_name + "_best_model",
                save_top_k=1,
                monitor="val_accuracy",
                mode="max",
            )
        ]
    )

    trainer.fit(model,
        data_module.train_dataloader(),
        data_module.val_dataloader()
    )

if __name__=="__main__":
    main()