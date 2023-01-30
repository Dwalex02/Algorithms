# ADSII3ILV - Assignment 1

For this assignment, you need to solve the following four little programming tasks covering basic algorithms and data structures and their application to concrete problems.

To pass the assignment, you also have to test your solution, i.e., implement one or more test cases, and endure your test cases achieve at least 90% of coverage.

Readability of your code and the presence of meaningful and useful comments are also a must.

As the programming language you must use Python (v 3.10).
As the testing framework you must use `pytest`[1].

The structure of the assignment is already given to you but you can add additional files if needed. For instance, you can store test cases targeting different units of code in separate files. 

> *NOTE*: Be sure that you name the scripts that contain the test cases using the usual naming convention, i.e.,  `test_*.py`, and do not mix application and test code in the same scripts.

## Plagiarism

Remember that plagiarism can be punished with a *failure* so pay extra care and neither share your solution nor copy someone else's solution. Because you are implementing basic and well know algorithms pay attention to clearly comment your code.

## Post Submission Evaluation

The lecturer may decide to have an interview with you about your assignment *after* the submission past. An interview does not automatically means there's the suspect of a plagiarism. You can think of it either as an random check at the airport or as an additional occasion to explain and clarify yourself.

## Tasks

### Task 1 - Implement a sorting algorithm

Among the many different sorting algorithms that exist, you are asked to implement the simplest (not necessary the most efficient) one: *insertion sort*

As any other sorting algorithm, you must read in a sequence of integers (a list or array) and return a new sequence of integers sorted by value (small values come before than large values).

See: `insertion_sort.py` and `test_insertion_sort.py`


### Task 2 - Implement a linear data structure

Linear data structures, like list and queue, can be "draw" on a line. In this task, you are asked to implement a *double-linked list*.
A double-linked list is a linked list that contains nodes having a data value, a pointer to the next node, and a pointer to the previous node.

The interface of the double-linked list is already given to you:

- Insertion/Deletion operations:
    - Insertion/Deletion at the beginning of the list
    - Insertion/Deletion at position
    - Insertion/Deletion at the end of the list

    > Note: The operations must `raise` a `ValueError` when provided with inappropriate parameters. For instance, deleting an element from an empty list, removing/inserting at position outside the range [0, size() ) (0 included, size() excluded).

- Printing operations (produce strings):
    - Print the values forward as a list of comma-separated value (no spaces!)
    - Print the values backward as a list of comma-separated value (no spaces!)

- Accessors (return values):
    - get the size of the list
    - get the value of first node (return `None` if the list is empty)
    - get the value of last node (return `None` if the list is empty)
    - get the value of the previous node given another node (return `None` if there no previous node, i.e., head)
    - get the value of the next node given another node (return `None` if there no next node, i.e., tail)

    > Note: The operations must `raise` a `ValueError` when provided with inappropriate parameters. For instance, get next/previous node assumes that the input node belong to the list.

- Other operations:
    - Check if the list contains at least one node with the given value.  (return `False` if the given value/node is not there)

See: `double_linked_list.py` and `test_double_linked_list.py`

### Task 3 - Solve a problem using the appropriate data structures and algorithms

Implement the *Move to Back* program that read in a sequence of characters from an input string, one by one and maintain the read characters in a linked list without duplicates.

When you read in a previously unseen character, set it at the back of the list.
When you read in a character that is already in the list, delete it from the list and reinsert it at the back of the list.

Note: This algorithm implements a variation of a known strategy that is useful for caching, data compression, and many other applications.

See: `move_to_back.py` and `test_move_to_back.py`

### Task 4 - Solve a problem using the appropriate data structures and algorithms

Implement a parentheses balancer checker, i.e., an algorithm that given an expression as input examines whether the pairs and the orders of `{`, `}`, `(`, `)`, `[`, `]` are correct in the given expression.

The parentheses must match. For instance, the string `{[]}` is OK, whereas the string `{[}]` is NOT.

See: `check_balance.py` and `test_check_balance.py`

## Setting up your local environment

To solve this assignment you need to install the `pytest` library. Optionally, you can also install the `pytest-cov`, library. 

If you are using (and you should!!) a virtual environment (`venv`, `conda`, `anaconda`) the file `requirements.txt` list all the dependencies in the format accepted by `pip`.

You can create a virtual environment named `.venv` using the module `venv` and running the following command:

Go to the root of your repository (where this README.md file is):

``` 
$ cd <ROOT_OF_YOUR_PROJECT>
```

Next, create the virtual environment:

```
$ python -m venv .vevn
```

Then, activate the virtual environment:

```
$ . .venv/bin/activate
```

For Windows, you must run `.venv/Script/activate`

You can tell the environment is active because the shell/terminal shows its name:

```
(.venv)$ 
```

Go on and, update `pip`:

```
(.venv)$ pip install --upgrade pip
```

Finally, install the requirements in the active virtual environments:

```
(.venv)$ pip install -r requirements.txt
```

> *NOTE:* once you have created the virtual environment you can configure your Python IDE (e.g., PyCharm) to use it.

## Running tests

`pytest` will run all the tests in the folder where it is invoked that match the pattern `test_*.py`. Hence, after installing `pytest`, you can run the tests as follows (from the project root and with the active virtual environment):

```
(.venv)$ pytest
```

## Computing Code Coverage

If you have installed `pytest-cov`, `pytest` can also compute the statement and branch coverage achieved by the tests, as follows:


```
(.venv)$ pytest --cov --cov-branch
```

> *NOTE:* The file `.coveragerc` contains the configuration of `pytest-cov`

## References

[1] `pytest`: [https://docs.pytest.org/en/7.1.x/](https://docs.pytest.org/en/7.1.x/)