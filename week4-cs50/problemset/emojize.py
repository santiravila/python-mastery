import emoji


def main():
    message = input("Input: ")  

    # determine if substr from message is a code/alias
    print(f"Output: {emoji.emojize(message, language="alias")}")
    # code to alias

    # replace alias substr with emoji in the message 
    ...

def validate_alias(alias):
    result = emoji.emojize(alias, laanguage="alias")
    return result != alias


main()