# Student Marks Lookup

## Functionality
This Python program allows users to retrieve the marks of students from a predefined dictionary. It performs the following tasks:

1. **Defines a Dictionary**: Contains student names as keys and their marks as values.
2. **Takes User Input**: Asks the user to input a student's name.
3. **Fetches Data**: Displays the marks for the entered name if it exists in the dictionary.
4. **Handles Missing Names**: Shows an appropriate message if the student is not found.

## How It Works
- A dictionary named `dictionary` is created with sample student names and corresponding marks.
- The program uses `input()` to collect the student's name from the user.
- A conditional statement checks if the name exists in the dictionary.
- If found, the marks are printed.
- If not found, the program informs the user that the student name is not present.

## Sample Output
**Case 1: Name Found**
```
Enter student's name=Ram
Ram's marks: 91
```

**Case 2: Name Not Found**
```
Enter student's name=John
Student name not found
```

## Usage
Use this program to perform a quick lookup of student marks by entering the student name exactly as it appears in the dictionary.

# List Extraction and Reversal

## Functionality
This Python program demonstrates basic list operations including slicing and reversing. It performs the following actions:

1. **Creates a List**: A list of numbers from 1 to 10 is initialized.
2. **Extracts Elements**: The first five elements from the list are sliced and stored.
3. **Reverses the Slice**: The sliced list is then reversed.
4. **Displays Results**: Both the original slice and its reversed version are printed.

## How It Works
- A list named `list` is initialized with integers from 1 through 10.
- The first five elements are extracted using `list[0:5]`.
- These elements are reversed using the `.reverse()` method.
- Results are printed to the console.

## Sample Output
```
Original list=  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements:  [1, 2, 3, 4, 5]
Reversed extracted elements:  [5, 4, 3, 2, 1]
```

## Usage
Use this program to understand and practice basic list slicing and reversal techniques in Python.

