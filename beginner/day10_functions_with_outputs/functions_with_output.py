# Functions with output


def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""

    if f_name == "" or l_name == "":
        return

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name('eNry', 'coOp')
print(formated_string)
