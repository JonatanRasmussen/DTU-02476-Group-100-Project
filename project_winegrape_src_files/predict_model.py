import torch

from pytorch_lightning import seed_everything

from data.data import DataModule
from models.model import ImageClassifier,CNN_Model

import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config2")
def inference(cfg : DictConfig):
    
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

    if cfg.model.model_name == "CNN":
        model = CNN_Model.load_from_checkpoint(
            checkpoint_path = "checkpoints/" + cfg.model.model_name + "_best_model.ckpt",
            map_location="cpu"
        )

    else:
        model = ImageClassifier.load_from_checkpoint(
            checkpoint_path = "checkpoints/" + cfg.model.model_name + "_best_model.ckpt",
            map_location="cpu"
        )
    
    model.eval()

    test_loader = data_module.test_dataloader()

    print(f"model inference for model {cfg.model.model_name}_best_model.ckpt")

    with torch.no_grad():
        n_images = 0
        for images, labels in test_loader:
            n_images += len(labels)
            logits = model(images)

            loss = model.criterion(logits, labels)
            preds = torch.argmax(logits, dim = 1)
            accuracy = model.calc_accuracy(preds, labels)
            
            print(f"number of test images: {n_images}")
            print('train_loss', loss.item())
            print('train_accuracy', accuracy.item()*100, "%")

if __name__=="__main__":
    inference()