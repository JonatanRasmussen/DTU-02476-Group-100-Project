import os
import opendatasets as od


def main():
    """Downloads the data from Kaggle and places it in "data/raw/"
    """

    dataset_path = os.path.join(os.getcwd(),"data","raw")
    try:
        import kaggle  # type: ignore
    except Exception:
        print(
            "Must athenticate the kaggle api according to https://www.kaggle.com/docs/api"  # noqa: E501
        )
        exit(1)

    dataset = 'https://www.kaggle.com/datasets/muratkokludataset/grapevine-leaves-image-dataset'
    print("info: you can find your username and key under /.kaggle/kaggle.json")
    
    od.download_kaggle_dataset(dataset,dataset_path)


if __name__ == "__main__":
    main()