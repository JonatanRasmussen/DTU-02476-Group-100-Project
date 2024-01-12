from hydra import initialize, compose
import os

def test_config() -> None:
    with initialize(version_base=None, config_path="../conf"):
        test_cfg = compose(config_name="test_config")
        # assert top level keys
        assert "reproducibility" in test_cfg.keys()
        assert "data" in test_cfg.keys()
        assert "model" in test_cfg.keys()
        assert "optimization" in test_cfg.keys()
        assert "training" in test_cfg.keys()
        assert "logging" in test_cfg.keys()
        # assert data exists
        assert os.path.exists(os.path.dirname(test_cfg.data.dir))
