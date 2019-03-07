from bracket_validation import BracketValidation


def test_class_exists():
    assert BracketValidation


def test_class_instantiation():
    assert BracketValidation()


def test_consecutive_sets():
    validation = BracketValidation()
    
    assert validation.bracket_validation('(This)[should][work]') == True


def test_nested_sets():
    validation = BracketValidation()
    
    assert validation.bracket_validation('(This[should]work)') == True


def test_overlapping_sets():
    validation = BracketValidation()
    
    assert validation.bracket_validation('(This(should not[work])') == False


def test_extra_open_bracket():
    validation = BracketValidation()
    
    assert validation.bracket_validation('(This[should) not work]') == False


def test_extra_close_bracket():
    validation = BracketValidation()
    
    assert validation.bracket_validation('This willnot work]') == False


def test_no_brackets():
    validation = BracketValidation()
    
    assert validation.bracket_validation('(This will not work') == False


def test_no_brackets():
    validation = BracketValidation()
    
    assert validation.bracket_validation('This will work') == True