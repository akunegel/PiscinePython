def ft_filter(func, arg):
    """
        filter(function, args: list)
        returns a list of every item in list for wich function(item)
        returns True.
    """
    return [item for item in arg if func(item)]
