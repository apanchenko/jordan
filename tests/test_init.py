from contextlib import nullcontext as no_raise
from pytest import mark, raises
import peano

def test_version():
    assert peano.__version__ == '0.1.3'

@mark.parametrize("name, value, expect", [
    ("delay", -100, raises(ValueError)),
    ("delay", 0, raises(ValueError)),
    ("delay", 1, no_raise()),
    ("delay", 10, no_raise()),
    ("delay", 600, no_raise()),
    ("latency_accuracy", -1, raises(ValueError)),
    ("latency_accuracy", 0, no_raise()),
    ("latency_accuracy", 9, no_raise()),
    ("latency_accuracy", 12, raises(ValueError)),
    ("min_batch_size", 0, raises(ValueError)),
    ("min_batch_size", 1, no_raise()),
    ("max_batch_duration", 0, raises(ValueError)),
    ("max_batch_duration", 1, no_raise()),
])
def test_init_validation(name, value, expect):
    with expect:
        peano.init('', '', '', '', **{name: value})
