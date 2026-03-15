from logic_utils import check_guess

"""def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
"""

def test_incorrect_guess_directions_not_swapped():
    """
    Regression test for the swapped Too High / Too Low bug.
    Previously, guess > secret incorrectly returned "Too Low" and vice versa.
    check_guess returns a (outcome, message) tuple, so we unpack accordingly.
    """
    # Guess is higher than secret → must say "Too High", not "Too Low"
    outcome_high, _ = check_guess(75, 50)
    assert outcome_high == "Too High", (
        f'Expected "Too High" when guess > secret, got "{outcome_high}" — '
        "direction bug may still be present"
    )

    # Guess is lower than secret → must say "Too Low", not "Too High"
    outcome_low, _ = check_guess(25, 50)
    assert outcome_low == "Too Low", (
        f'Expected "Too Low" when guess < secret, got "{outcome_low}" — '
        "direction bug may still be present"
    )
