# coding=utf-8
#!/usr/bin/env python

import sys
import logging
from ndfa import DFA


dfas = []


def test(dfa, words):
    """Test function. Tests each word in `words` with the provided dfa."""
    for word in words:
        try:
            dfa.test(word)
        except AssertionError as e:
            logging.error('ERROR: %s\n' % e.message)


def even_count_of_a():
    """DFA that accepts strings with an even number of 'a's."""
    states = list('01')
    alphabet = list('ab')
    transitions = {
        ('0', 'a'): '1',
        ('0', 'b'): '0',
        ('1', 'a'): '0',
        ('1', 'b'): '1',
    }
    start = '0'
    accepts = list('0')
    return states, alphabet, transitions, start, accepts
dfas.append((even_count_of_a, ['abbaaab', '', 'aba', 'aafa', 'abaaaaaaa']))


def even_number():
    """DFA that recognizes an even positive or negative number
    without a leading 0."""
    states = ['q0', 'm', 'p', '0', 'e']
    alphabet = list('0123456789-')
    transitions = {
        ('q0', '0'): '0',
        ('q0', '1'): 'p',
        ('q0', '2'): 'p',
        ('q0', '3'): 'p',
        ('q0', '4'): 'p',
        ('q0', '5'): 'p',
        ('q0', '6'): 'p',
        ('q0', '7'): 'p',
        ('q0', '8'): 'p',
        ('q0', '9'): 'p',
        ('q0', '-'): 'm',
        ('m', '0'): 'e',
        ('m', '1'): 'p',
        ('m', '2'): 'p',
        ('m', '3'): 'p',
        ('m', '4'): 'p',
        ('m', '5'): 'p',
        ('m', '6'): 'p',
        ('m', '7'): 'p',
        ('m', '8'): 'p',
        ('m', '9'): 'p',
        ('m', '-'): 'e',
        ('p', '0'): 'p',
        ('p', '1'): 'p',
        ('p', '2'): 'p',
        ('p', '3'): 'p',
        ('p', '4'): 'p',
        ('p', '5'): 'p',
        ('p', '6'): 'p',
        ('p', '7'): 'p',
        ('p', '8'): 'p',
        ('p', '9'): 'p',
        ('p', '-'): 'e',
        ('0', '0'): 'e',
        ('0', '1'): 'e',
        ('0', '2'): 'e',
        ('0', '3'): 'e',
        ('0', '4'): 'e',
        ('0', '5'): 'e',
        ('0', '6'): 'e',
        ('0', '7'): 'e',
        ('0', '8'): 'e',
        ('0', '9'): 'e',
        ('0', '-'): 'e',
        ('e', '0'): 'e',
        ('e', '1'): 'e',
        ('e', '2'): 'e',
        ('e', '3'): 'e',
        ('e', '4'): 'e',
        ('e', '5'): 'e',
        ('e', '6'): 'e',
        ('e', '7'): 'e',
        ('e', '8'): 'e',
        ('e', '9'): 'e',
        ('e', '-'): 'e',
    }
    start = 'q0'
    accepts = list('p0')
    return states, alphabet, transitions, start, accepts
dfas.append((even_number, ['', '0', '-1', '231891413293749242', '12-5', '012', '-42']))


if __name__ == '__main__':

    # Configure logging
    args = sys.argv[1:]
    fmt = '%(message)s'
    if set(['-v', '--verbose']).isdisjoint(args):
        logging.basicConfig(level=logging.INFO, format=fmt)
    else:
        logging.basicConfig(level=logging.DEBUG, format=fmt)

    for func, words in dfas:
        print '-' * 50
        print 'TESTING %s' % func.__name__
        print '-' * 50
        dfa = DFA(*func())
        test(dfa, words)
