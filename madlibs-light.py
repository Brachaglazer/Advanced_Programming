# Day 1 Dictionary Mad Libs (NO nested dictionaries)
# -------------------------------------------------
TEMPLATE = (
    "I was waiting for the {adj1} train at {num1} o’clock when a {noun1} "
    "{verb_past1} past me and shouted, “{exclaim1}!” "
    "I grabbed my {noun2} and ran {num2} steps to the {noun3}."
)

TEMPLATE_TWO = (
    "I love {verb_past1} to the {noun1} with {noun2} because we really have fun."
    "Sometimes the {adj1} {noun3} yells to us, “{exclaim1}!” "
    "The best time to go is at {num1}:{num2}."
)

# PROMPTS is a dictionary:
#   key   = placeholder name (must match TEMPLATE placeholders)
#   value = what we ask the user to type
PROMPTS = {
    "adj1": "Enter an adjective",
    "num1": "Enter a number (0-23)",
    "noun1": "Enter a noun",
    "verb_past1": "Enter a past-tense verb",
    "exclaim1": "Enter an exclamation (one word)",
    "noun2": "Enter a noun",
    "num2": "Enter a number (1-500)",
    "noun3": "Enter a noun",
}

# RULES is a dictionary:
#   key   = placeholder name (only for some placeholders)
#   value = a rule dictionary describing how to validate the input
#  we access a dictionary within a dictionary like it is a nested loop
#  For instance, to access num1's max value 23 : RULES["num1"]["max"]
#  To access the value word of exclaim1 : RULES["exclaim1"]["type"]

RULES = {
    "num1": {"type": "int", "min": 0, "max": 23},
    "num2": {"type": "int", "min": 1, "max": 500},
    "exclaim1": {"type": "word"},
}

# state tracks information across multiple plays
state = {
    "plays_total": 0,
    "best_score": None,
}


def validate_input(key, raw, rules):
    """
    Validate ONE user entry.

    Parameters:
      key   : the placeholder key (example: "num1" or "noun2")
      raw   : the user's raw input (a string)
      rules : the RULES dictionary

    Return:
      (ok, value, error_message)
        ok = True/False
        value = cleaned value (string or int) if ok is True, else None
        error_message = "" if ok is True, else a message to show the user

    Rules supported:
      - If key NOT in rules: accept any non-empty string (strip whitespace)
      - {"type":"int", "min":..., "max":...}
      - {"type":"word"}  -> one word only (no spaces), not empty

    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"]
    """
    stripped_input = raw.strip()
    rule = rules.get(key)
    if not rule:
        return (True, stripped_input, "")
    if rule["type"] == "int":
        try:
            stripped_input = int(stripped_input)
        except ValueError as e:
            return (False, None, "Please enter a valid integer.")
    if "min" in rule:
        if stripped_input < rule["min"]:
            return (False, None, "Please enter a valid integer.")
        if stripped_input > rule["max"]:
            return (False, None, "Please enter a valid integer.")
    if rule["type"] == "word":
        if stripped_input == "":
            return (False, None, "Please enter a valid integer.")
        for letter in stripped_input:
            if letter.isspace():
                return (False, None, "Please enter a valid word.")
    return (True, stripped_input, "")


def collect_answers(prompts, rules):
    """
    Build the answers dictionary.

    prompts: PROMPTS dict (placeholder -> prompt)
    rules  : RULES dict (placeholder -> rule)

    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"]

    Returns:
      answers dict where:
        key   = placeholder name (example: "noun1")
        value = validated user input (string or int)

    Requirements:
      - Start with answers = {}
      - Loop through prompts.items()
      - For each key:
          keep prompting until validate_input(...) returns ok=True
      - Store answers using answers[key] = value
    """
    answers = {}
    for key, value in prompts.items():
        while True:
            user_input = input(value)
            ok, cleaned, message = validate_input(key, user_input, RULES)
            if ok == False:
                print(message)
                continue
            answers[key] = user_input
            break
    return answers


def score_answers(answers, rules):
    """
    Compute a score for one round.

    Recommended scoring:
      - +1 for each answer key in answers
      - +2 bonus if that key also appears in rules

    Example:
      If answers has 8 keys, and 3 keys are in rules:
        score = 8*1 + 3*2 = 14


    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"]
    """
    # Requirements:
    #   - iterate over the dictionary keys in answers (for key in answers:)
    #   - use membership test (if key in rules:)
    score = 0
    for key in answers:
        score += 1
        if key in rules:
            score += 2
    return score


def play_once():
    """
    Play one round of Mad Libs.

    Steps:
      1) Collect answers into a dictionary
      2) Fill TEMPLATE using TEMPLATE.format_map(answers)
      3) Score the round
      4) Update state:
          - plays_total increases by 1
          - best_score updates if this score is higher
      5) Print:
          - completed story
          - answers dict
          - score
    """
    print("\nFill in the blanks (you won't see the full story until the end!)\n")

    answers = collect_answers(PROMPTS, RULES)
    chosen = input("Template one or two?")
    if chosen.lower() == "two":
        finished = TEMPLATE_TWO.format_map(answers)
    else:
        finished =TEMPLATE.format_map(answers)
    score = score_answers(answers, RULES)
    state["plays_total"] += 1
    if state["best_score"] == None or score > state["best_score"]:
        state["best_score"] = score
    print(f"story: {finished}")
    print(f"answers: {answers}")
    print(f"score: {score}")


def main():
    """

    What main  does:
    - Repeatedly asks the user if they want to play
    - Calls play_once() when the user says 'y'
    - Stops when the user says 'n'
    - Prints a summary using the state dictionary
    """

    print("Mad Libs ")

    # until the user chooses to stop.
    while True:
        play = input("Do you want to play? ")
        play_normal = play.strip().lower()
        if play_normal == 'n':
            break
        elif play_normal == 'y':
            play_once()
        else:
            continue
    print(state)


if __name__ == "__main__":
    main()
