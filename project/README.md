
# CS50_PROGRESS_TRACKER

This Python script helps users track their progress through various courses by marking completed weeks and calculating completion percentages for each course.



#### Video Demo
<https://www.youtube.com/watch?v=rnsa7o48F2Q>



## Description

This project offers a comprehensive overview of all CS50 courses, allowing you to explore topics and track your progress. Mark completed weeks and get a ** visualization of progress, including completion percentages.



## Features

- Display a list of available courses before and after marking.
- Allows user to select a course and mark completed weeks.
- Automatically calculates and displays completion percentages for each course.


## Usage

1. Run the `project.py` script.
2. Follow the prompts to select a course and input completed weeks.
3. Enter an empty string to exit the loop whenever needed and view the final table with completion percentages.



## Course Schedule Representation

Course schedules are represented using a dictionary (**`course_week_dict`**) containing course names as keys and a nested dictionary of weeks and topics as values. Completed weeks are tracked by adding "**" to the topic name which itself is a string. Tabulate libarary is used to format that dictionary accordingly.



## Functionality Details

- **`course_select`**: Display the list of courses and takes user input to select a course. Returns an empty string to terminate the loop if the user provides an empty input.
- **`week_select`**: Asks the user to input a week number. Terminates the loop if the user provides an empty input and ensures the input is converted to a float.
- **`course_week_schedule`**: Prints a table of courses, weeks, and topics. Allows users to mark completed weeks and calculates completion percentages. The loop terminates upon providing an empty input. And then again the prints the table with weeks marked and diaplays completion percentages.



## Testing

The `test_project.py` script contains automated tests for the `course_select` and `week_select` functions. It uses the `pytest` framework to run test cases and verify the correctness of the functionalities. To run the tests, simply execute the `test_project.py` script.
However both of the courses takes 0 parameters, a monkeypatch fixture is used to mock their inputs.



## Design Choices

- Use of dictionaries to represent course schedules for easy access and modification.
- Conversion of week input to float to handle cases where week numbers are non-integer
- Appending "**" to topic names to track completed weeks.



## Error Handling

- Raises errors for invalid week numbers and selected courses not in the course list.



## Dependencies

- This script uses the **`tabulate`** library for tabular output. Make sure to install it using **`pip install tabulate`**.


## Author

- MUMMANA JAGADEESH - mummanajagadeesh97@gmail.com
