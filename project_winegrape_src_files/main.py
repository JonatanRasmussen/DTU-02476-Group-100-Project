import hydra
from omegaconf import DictConfig

from models.model import ImageClassifier,CNN_Model
from torchvision import transforms

import os
import torch
import json
from PIL import Image

@hydra.main(version_base=None, config_path="conf", config_name="config2")
def main(cfg : DictConfig):

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

    def find_image(path = "project_winegrape_src_files/data/API_image/"):
        images = []
        for image in os.listdir(path):
            images.append(image)

        basic_transformation = [
                    transforms.Resize(224),
                    transforms.ToTensor(),
                    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])
                ]

        img = Image.open(path+images[0])
        img = img.convert('RGB')
        augment = transforms.Compose(basic_transformation)
        aug_img = augment(img) 

        return aug_img.unsqueeze(0), images[0]

    img,img_name = find_image()


    model.eval()
    with torch.no_grad():
        pred = model(img)

    name = ['Ak', 'Ala_Idris', 'Buzgulu', 'Dimnit', 'Nazli']
    prediction = name[torch.argmax(pred)]

    results = {'True outcome':img_name.split(" ")[0], f"{cfg.model.model_name}_Model prediction":prediction}

    with open('project_winegrape_src_files/data/API_image/results.json','w') as f:
        json.dump(results,f)

if __name__=="__main__":
    main()