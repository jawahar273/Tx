import pytest

from .default_engine import TxDefaultEngine


def test_engine_with_out_IO():
    with pytest.raises(TypeError):
        engine = TxDefaultEngine()
