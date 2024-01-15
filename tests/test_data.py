from project_winegrape_src_files.data.data import DataModule
from hydra import initialize, compose

def test_data():
    with initialize(version_base=None, config_path="../project_winegrape_src_files/conf"):
        test_cfg = compose(config_name="test_config")
        data_module = DataModule(
            data_dir=test_cfg.data.dir,
            transform_level=test_cfg.data.transform_level,
            batch_size=test_cfg.data.batch_size,
            val_split=test_cfg.data.val_split,
        )
        data_module.setup()
        training_dataset = data_module.train_dataloader()
        val_dataset = data_module.val_dataloader()
        test_dataset = data_module.test_dataloader()
        assert len(training_dataset) == 2
        assert len(val_dataset) == 1
        assert len(test_dataset) == 1
