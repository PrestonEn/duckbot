import tools
import pytest

def test_kubernetes_correction():
    test_message = tools.make_correction("tom", "kubernetes")

    assert test_message == "I think tom means K8s"
# end def test_kubernetes_correction
