NEW_LINE = "\n"  # used in f-strings


def snowflakeToTime(snowflake: int) -> int:
    return snowflake // 4194304000 + 1420070400


def tryOrDefault(func, defaultVal=None):
    try:
        return func()
    except:
        pass
    return defaultVal


def pluralSuffix(val: int) -> str:
    if val != 1:
        return "s"
    return ""
