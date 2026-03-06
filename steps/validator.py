def validate_output(ai_output):

    if ai_output is None:
        return False

    if len(ai_output.strip()) == 0:
        return False

    # basic validation: must contain text insights
    if len(ai_output) < 20:
        return False

    return True