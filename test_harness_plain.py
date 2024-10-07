import os
import subprocess
import pytest

# Fixture to provide test cases
@pytest.fixture
def test_cases():
    test_files = []
    expected_outputs = []

    # Load all test files and corresponding expected output files
    for i in range(1, 11): 
        test_files.append(f'TestData/TestFiles/test_{i}.json')
        expected_outputs.append(f'TestData/ExpectedOutput/test_{i}.csv')
    
    return list(zip(test_files, expected_outputs))

# Test function that receives the test cases from the fixture
def test_json_to_csv(test_cases):

    nodes = ["fruit", "fruit"]

    # Iterate over each test case
    for i, (input_file, expected_output_file) in enumerate(test_cases):
        node = nodes[i]

        # File where the actual output will be written
        actual_output_file = f'TestData/ActualOutput/actual_output_{i+1}.csv'

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
