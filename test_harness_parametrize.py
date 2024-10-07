import pytest
import subprocess
import re

def fixture():
    test_files = []
    expected_outputs = []
    nodes = ["fruit", "fruit"]

    # Load all test files and corresponding expected output files
    for i in range(1, 12):
        test_files.append(f'TestData/TestFiles/test_{i}.json')
        expected_outputs.append(f'TestData/ExpectedOutput/test_{i}.csv')
    
    return list(zip(test_files, expected_outputs, nodes))


@pytest.mark.parametrize("input_file, expected_output_file, node", fixture())
def test_json_to_csv(input_file, expected_output_file, node):

    # Extract the number from the JSON filename (test_i.json)
    match = re.search(r'test_(\d+)\.json', input_file)
    if match:
        file_number = match.group(1)
    else:
        raise ValueError(f"Filename format invalid for {input_file}")

    # Use the extracted number for the actual output filename
    actual_output_file = f'TestData/ActualOutput/actual_output_{file_number}.csv'

    # Run program using subprocess
    subprocess.run(['python', 'json_to_csv.py', node, input_file, actual_output_file], check=True)

    # Read expected output
    with open(expected_output_file, 'r') as f:
        expected_output = f.read()

    # Read actual output
    with open(actual_output_file, 'r') as f:
        actual_output = f.read()


    # Assert that expected output matches actual output
    assert expected_output.strip() == actual_output.strip(), f"Mismatch between {actual_output_file} and {expected_output_file}"