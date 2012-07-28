ndfa - nondeterministic and deterministic finite automata
=========================================================

Finit state machine implementations.

`ndfa.py` currently contains only a DFA class. NFA will follow later.


Usage
-----

Here is an example of a DFA that accepts strings with an even number of 'a's.

    from ndfa import DFA

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

    dfa = DFA(states, alphabet, transitions, start, accepts)

To test some words with this dfa:

    >>> dfa.test('')
    True
    >>> dfa.test('aababa')
    True
    >>> dfa.test('baaa')
    False
    >>> dfa.test('foo')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "ndfa.py", line 24, in test
        'Symbol "%s" must be in alphabet.' % symbol
    AssertionError: Symbol "f" must be in alphabet.


Output
------

The DFA class uses the python logging module. To see basic output, set log
level to INFO:

    >>> import logging
    >>> logging.basicConfig(level=logging.INFO, format='%(message)s')
    >>> dfa.test('aba')
    Testing word "aba"...
    Accepted: True

...or to DEBUG for more verbose output:

    >>> import logging
    >>> logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    >>> dfa.test('aba')
    Testing word "aba"...
    Initial state: 0
    Current symbol: a
    New state: 1
    Current symbol: b
    New state: 1
    Current symbol: a
    New state: 0
    Final state: 0
    Accepted: True


License
-------

GPLv3, see LICENSE.md
