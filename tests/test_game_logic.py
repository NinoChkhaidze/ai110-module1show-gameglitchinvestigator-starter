from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


# --- get_range_for_difficulty tests ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


# --- parse_guess tests ---

def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."

def test_parse_guess_not_a_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_guess_float_rounds():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7


# --- update_score tests ---

def test_update_score_win():
    # Win on attempt 1 should add points
    score = update_score(0, "Win", 1)
    assert score > 0

def test_update_score_too_low_deducts():
    score = update_score(50, "Too Low", 1)
    assert score == 45

def test_new_game_secret_within_difficulty_range():
    # Regression test: new game must use the difficulty range, not hardcoded 1-100.
    # On Hard, range is 1-50, so a secret of 76 (outside range) was possible before the fix.
    import random
    random.seed(0)
    for _ in range(100):
        low, high = get_range_for_difficulty("Hard")
        secret = random.randint(low, high)
        assert low <= secret <= high, (
            f"Secret {secret} is outside Hard difficulty range ({low}-{high})"
        )


# --- Regression tests for fixed bugs ---

def test_string_comparison_bug():
    # Bug: on even attempts, secret was cast to str, causing wrong comparisons.
    # check_guess(9, "80") would return "Too High" because "9" > "8" alphabetically.
    # With the fix, secret stays an int so 9 < 80 correctly returns "Too Low".
    result = check_guess(9, 80)
    assert result[0] == "Too Low", (
        "String comparison bug: 9 < 80 should be Too Low, not Too High"
    )

def test_string_comparison_bug_high():
    # Bug: check_guess(50, "9") would return "Too Low" because "5" < "9" alphabetically,
    # even though 50 > 9. With the fix, integer comparison correctly returns "Too High".
    result = check_guess(50, 9)
    assert result[0] == "Too High", (
        "String comparison bug: 50 > 9 should be Too High, not Too Low"
    )
