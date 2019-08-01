import pytest

from lisp_int import parse

@pytest.mark.parametrize("src, result",
                         [('(+ 2 (* 2 2))', ['+', 2, ['*', 2, 2]]),
                          ('(define (size 2))', ['define', ['size', 2]]),
                          ('(+ (* 5 3) (/ 8 4))', ['+', ['*', 5, 3], ['/', 8, 4]])])
def test_parse_works_correctly(src, result):
    assert parse(src) == result
