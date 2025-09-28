def run(args):
    try:
        numbers = [float(x) for x in args]
        print(f"Sum: {sum(numbers)}")
    except ValueError:
        print("Please provide only numbers.")