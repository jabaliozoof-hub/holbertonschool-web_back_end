# Python - Async Comprehension

This project contains Python scripts focusing on asynchronous programming concepts, specifically asynchronous generators, asynchronous comprehensions, and running asynchronous tasks in parallel using `asyncio`.

---

## Resources
* [PEP 530 -- Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
* [What's New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.8.html#pep-530-asynchronous-comprehensions)
* [Type-hints for generators](https://www.python.org/dev/peps/pep-0484/)

---

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators

---

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version 2.5.x)
* All your modules should have documentation
* All your functions should have documentation
* All your functions and coroutines must be type-annotated

---

## Tasks

### 0. Async Generator
* **File:** `0-async_generator.py`
* **Description:** A coroutine called `async_generator` that takes no arguments. It loops 10 times, each time asynchronously waiting 1 second, then yields a random number between 0 and 10 using the `random` module.

### 1. Async Comprehensions
* **File:** `1-async_comprehension.py`
* **Description:** A coroutine called `async_comprehension` that takes no arguments. It imports `async_generator` from the previous task and collects 10 random numbers using an async comprehension over `async_generator`, then returns the 10 random numbers.

### 2. Run time for four parallel comprehensions
* **File:** `2-measure_runtime.py`
* **Description:** A coroutine called `measure_runtime` that imports `async_comprehension` from the previous file and executes it four times in parallel using `asyncio.gather`. It measures the total runtime and returns it.
