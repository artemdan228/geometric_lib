figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}")

    try:
        result = eval(f'{fig}.{func}(*{size})')
        return result
    except Exception as e:
        raise ValueError(f"Error calculating {func} for {fig}: {e}")


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        try:
            size = list(
                map(int,
                    input(
                        "Input figure sizes separated by space (1 for circle and square)\n"
                    ).split(' ')
                    )
            )
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    try:
        result = calc(fig, func, size)
        print(f"{func} of {fig} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
