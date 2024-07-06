import argparse
import json
import yaml
import xmltodict
from pathlib import Path

def load_json(json_file):
    try:
        path = Path(json_file)
        if path.is_file():
            with path.open("r") as jf:
                data = json.load(jf)
                print("Valid JSON")
                return data
        else:
            print(f"Error: {json_file} does not exist.")
            return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None

def save_json(data, json_file):
    try:
        path = Path(json_file)
        with path.open("w") as jf:
            json.dump(data, jf, indent=4)
            print(f"Data saved to {json_file}")
    except Exception as e:
        print(f"Error: {e}")


def load_yaml(yaml_file):
    try:
        path = Path(yaml_file)
        if path.is_file():
            with path.open("r") as yf:
                data = yaml.safe_load(yf)
                print("Valid YAML")
                return data
        else:
            print(f"Error: {yaml_file} does not exist.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def save_yaml(data, yaml_file):
    try:
        path = Path(yaml_file)
        with path.open("w") as yf:
            yaml.dump(data, yf)
            print(f"Data saved to {yaml_file}")
    except Exception as e:
        print(f"Error: {e}")


def load_xml(xml_file):
    try:
        path = Path(xml_file)
        if path.is_file():
            with path.open("r") as xf:
                data = xmltodict.parse(xf.read())
                print("Valid XML")
                return data
        else:
            print(f"Error: {xml_file} does not exist.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def save_xml(data, xml_file):
    try:
        path = Path(xml_file)
        with path.open("w") as xf:
            xf.write(xmltodict.unparse(data, pretty=True))
            print(f"Data saved to {xml_file}")
    except Exception as e:
        print(f"Error: {e}")
        

def parse_args():
    parser = argparse.ArgumentParser(description="Argument parser")
    parser.add_argument("input_file", type=str, help="Input file path")
    parser.add_argument("output_file", type=str, help="Output file path")
    return parser.parse_args()

def main():
    args = parse_args()
    input_file_json = load_json(args.input_file)
    print(input_file_json)


if __name__ == "__main__":
    main()