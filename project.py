import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Argument parser")
    parser.add_argument("input_file", type=str, help="Input file path")
    parser.add_argument("output_file", type=str, help="Output file path")
    return parser.parse_args()

def main():
    args = parse_args()


if __name__ == "__main__":
    main()