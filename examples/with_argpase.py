import argparse

def hello():
    parser = argparse.ArgumentParser(description="Display greetings")
    parser.add_argument("--count", type=int, default=1, required=False,
            help="Nymber of greetings")
    parser.add_argument("--name", type=str, required=True,
            help="The person to greet")

    args = parser.parse_args()

    count = getattr(args, 'count')
    name = getattr(args, 'name')

    for x in range(count):
        print(f"Hello {name}!")


if __name__ == "__main__":
    hello()

