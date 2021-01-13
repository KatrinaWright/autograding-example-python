# Technical HW: Writing Loops & Sequences
Please complete the following functions. You can test by running the 'pytest' command.

## Problem 4: squared_sum

Write a function ```squared_sum``` in pseudocode or python that takes an array of numbers as input and outputs the following:

| **Example call** | **Returns** |
| -------------- | --------- |
| ```squared_sum ([])``` | ```0``` |
| ```squared_sum ([5, -2, 3])``` | ```38``` |
| ```squared_sum ([-3, 4])``` | ```25``` |
| ```squared_sum ([7, -1, 15, 0])``` | ```275``` |


## Problem 5: mix

Write a function ```mix``` in pseudocode or python that takes two strings as parameters and returns one array with the first element from the first array, and the second element from the second array, and every other element thereafter.

| **Example call** | **Returns** |
| -------------- | --------- |
| ```mix(hello, there)``` | ```htehlelroe``` |
| ```mix(1234, abcd)``` | ```1a2b3c4d``` |
| ```mix(12, abcd)``` | ```1a2bcd``` |
| ```mix(1234, ab)``` | ```1a2b34``` |


## Testing
The tests are failing right now because the functions aren't outputting the correct information. Fixing this up will make the tests green.

### Setup command
`sudo -H pip3 install pytest`

### Run command
`pytest`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
