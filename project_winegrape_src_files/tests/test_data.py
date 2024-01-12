from ..data.data import DataModule
from hydra import initialize, compose

def test_data():
    with initialize(version_base=None, config_path="../conf"):
        cfg = compose(config_name="config")
        data_module = DataModule(
            data_dir=cfg.data.dir,
            transform_level=cfg.data.transform_level,
            batch_size=cfg.data.batch_size,
            val_split=cfg.data.val_split,
        )
        data_module.setup()
        training_dataset = data_module.train_dataloader()
        val_dataset = data_module.val_dataloader()
        assert len(training_dataset) == 13
        assert len(val_dataset) == 3
