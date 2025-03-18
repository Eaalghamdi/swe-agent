import json
import argparse

# Function to read the JSON data from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to process the data and generate results
def process_data(data):
    results = {}
    
    # Loop through each entry in the data and check for occurrences of "main.py"
    for key, value in data.items():
        model_patch = value.get("model_patch", "")
        # Check if "main.py" exists in the model_patch string
        if "main.py" in model_patch:
            results[key] = 1
        else:
            results[key] = 0
    
    return results

# Main function for the CLI
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Check if 'main.py' exists in the provided JSON data.")
    parser.add_argument('input_file', type=str, help="The path to the input JSON file.")
    parser.add_argument('output_file', type=str, help="The path to save the output JSON file.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Read data from input file
    data = read_json_file(args.input_file)

    # Process the data
    results = process_data(data)

    # Save the results to the output file
    with open(args.output_file, 'w') as f:
        json.dump(results, f, indent=4)

    print(f"Data has been saved to '{args.output_file}'")

# Entry point for the script
if __name__ == "__main__":
    main()
