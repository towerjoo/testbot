_DEBUG = True

def debug(thing):
    if _DEBUG:
        print thing


def main_handler(ctx):
    """
    :param ctx:
     Dict
     ctx is the context object containing message data, the user who owns the bot instance, and

    :return:
        The bot's return value will be POSTed to its specified webhook address, if one is provided.
    """
    # First create an instance of the API interface
    # api = MC(ctx)
    # gather_macros()
    debug("Starting main handler.")
    print ctx
    debug("Processing complete.")
    # api.trace("I gathered all macro variables and put them in the DB.")
