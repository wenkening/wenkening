import random

import pytest

@pytest.mark.flaky(reruns=8, reruns_delay=2)
def test_example(self):
    print(3)
    assert random.choice([True, False])

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_example(self):
    print(3)
    assert random.choice([True, False])

@pytest.mark.run(order=2)
def test_foo():
    assert True


@pytest.mark.run(order=1)
def test_bar():
    assert True
