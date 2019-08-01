import pytest

from lisp_int import parse


def test_parse_works_correctly():
    assets = {
        '(+ 2 (* 2 2))': ['+', 2, ['*', 2, 2]],
        '(define (size 2))': ['define', ['size', 2]],
        '(+ (* 5 3) (/ 8 4))': ['+', ['*', 5, 3], ['/', 8, 4]]
    }
    for src, result in assets.items():
        assert parse(src) == result
