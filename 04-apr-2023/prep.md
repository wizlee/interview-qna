## Recon
- Can view the rule by clicking on the Codility invitation link without starting the timer
    - Once timer is started there is no stopping it
- Attempt [the practise session](https://app.codility.com/demo/take-sample-test/) as many time as you like to get familiar with the environment
- A website suggest to get familiar with strings and lists, thus the sub-section below is dedicated to the relevant findings

### Lists and Strings
Some useful Python functions related to lists and strings:
- run the function passed in by key over each item in test_set
    ```python
    test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5]
    test_set = set(test)

    # using test_set is not compulsory but will make this more performant
    print(max(test_set, key = test.count))
    ```
- `sorted()`: Sorts a list in ascending, descending, or user-defined order ³.
- `''.join()`: Join the iterables using any characters of choice.
- `split()`: The split() function breaks a string based on set criteria ¹.
- `count()`: This method counts the elements ³.
- `append()`: Used for appending and adding elements to the end of a list ³.
- `insert()`: Inserts a given element at a given index in a list ³.
- `reverse()`: Reverses objects of the list in place ³.
- `extend()` or `+=`: Adds each element of the iterable to the end of the list ³.
- `index()`: Returns the lowest index where the element appears ³.
- `copy()`: It returns a shallow copy of a list ³.
- `pop()`: Removes and returns the last value from the list or the given index value ³.
- `remove()`: Removes a given object from the list ³.
- `clear()`: This method is used for removing all items from a list ³.

Potentially useful Pythonic Way of writing things:
- List comprehension
    - Convinently generate a list and/or run a function over each item
    - Examples:
        - generate a list of 10 items with random integers from 0 to 19: `a = [random.randint(0, 19) for _ in range(10)]`
        - generate a list given a condition: `b = [f"even! {i}" if i % 2 == 0 else "Not even" for i in a]`
- Slicing
    - using colon(:) to slice a list into the subset or order that you want
    - Examples:
        - Reverse: `a[::-1]`
        - Split into 2 at the middle:
            ```python
            a = random.sample(range(0, 20), 10)
            mid = len(a) // 2
            low = a[:mid]
            high = a[mid:]
            ```
- Unpacking:
    - Unpacking a tuple: 
        ```python
        my_tuple = (1, 2, 3)
        a, b, c = my_tuple
        ```
    - Using the * operator:
        ```python
        list(range(3, 6))            # normal call with separate arguments
        args = [3, 6]
        list(range(*args))            # call with arguments unpacked from a list
        # both lists outputs [3, 4, 5]
        ```
    - Using ** operators to deliver keyword arguments:
        ```python
        def parrot(voltage, state='a stiff', action='voom'):
            print("-- This parrot wouldn't", action, end=' ')
            print("if you put", voltage, "volts through it.", end=' ')
            print("E's", state, "!")

        d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
        parrot(**d)
        # outputs: -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
        ```
- sets:
    - operators 
        - `^`: symmetric difference
        - `-`: difference
        - `|`: union
        - `&`: intersection operations
    - everything in A that's not in B: `A - B`
    - all the elements that are in exactly one set, i.e. the union of `A - B` and `B - A`: `A ^ B` or `A.symmetric_difference(B)`

## Practise Rounds

- The plan is to use VS Code to quickly protoyping answers and make sure it runs in the Codility environment
- Will use the practise rounds to get familiar with this workflow to be as smooth as possible
    - Change of plan, will not use as much time as possible for the practice round as the real task gives 12 hours to complete.
- After a brief revision on common algorithms and to get warm up with using the language of choice, the rest is up to realtime performance ;)
