from ..hashtable.hashtable import Hashtable, Node
from ..repeated_word.repeated_word import repeated_word


def test_same_case_word_match_string():
    sentance = 'Moses supposes his toeses are roses, but Moses supposes erroneously for nobod\'s toeses are roses or posies as Moses supposes his toeses to be.'

    expected = 'moses'
    actual = repeated_word(sentance)
    assert expected == actual


def test_opposite_case_word_match_string():
    sentance = 'How much wood would A woodchuck chuck if a woodchuck could chuck wood?'
    expected = 'a'
    actual = repeated_word(sentance)
    assert expected == actual


def test_empty_string():
    sentance = ''
    expected = None
    actual = repeated_word(sentance)
    assert expected == actual


def test_punctuation():
    sentance = 'Best day I ever, ever had.'

    expected = 'ever'
    actual = repeated_word(sentance)
    assert expected == actual


def test_no_matching_words():
    sentance = 'Not even the rain has such small hands.'
    expected = None
    actual = repeated_word(sentance)
    assert expected == actual
