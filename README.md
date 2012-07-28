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


License
-------

GPLv3, see LICENSE.md
