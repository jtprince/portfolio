

    values = [1, 2, 4, 5, 6, 7]

    windows = []
    for index in range(0, len(values) - 2):
        window = (values[index], values[index + 1], values[index + 2])
        windows.append(window)

    # windows -> [(1, 2, 4), (2, 4, 5), (4, 5, 6), (5, 6, 7)]


    def sliding_window(values):
        windows = []
        for index in range(0, len(values) - 2):
            window = (values[index], values[index + 1], values[index + 2])
            windows.append(window)
        return windows

    # len(values) as starting range
    # extra bracket around last value


    print(sliding_window(values))
    print(sliding_window(values))


    def sliding_window(window_size, values):
        windows = []
        for index in range(0, len(values) - window_size + 1):
            window = []
            for sub_index in range(index, index + window_size):
                window.append(values[sub_index])
            windows.append(tuple(window))
        return windows

    # forgot to add extra +1 on range


    print(sliding_window(3, values))
    print(sliding_window(20, values))


    def _get_subwindow(start, window_size, values):
        return tuple(values[index] for index in range(start, start + window_size))


    def sliding_window(window_size, values):
        return [
            _get_subwindow(index, window_size, values)
            for index in range(0, len(values) - window_size + 1)
        ]


    print(sliding_window(3, values))
    print(sliding_window(20, values))


    from toolz.itertoolz import sliding_window
    list(sliding_window(3, values))


    from cytoolz.itertoolz import sliding_window
    list(sliding_window(3, values))
