from hydra import initialize, compose
import os

def test_config() -> None:
    with initialize(version_base=None, config_path="../conf"):
        cfg = compose(config_name="config")
        # assert top level keys
        assert "reproducibility" in cfg.keys()
        assert "data" in cfg.keys()
        assert "model" in cfg.keys()
        assert "optimization" in cfg.keys()
        assert "training" in cfg.keys()
        assert "logging" in cfg.keys()
        # assert data exists
        assert os.path.exists(os.path.dirname(cfg.data.dir))
