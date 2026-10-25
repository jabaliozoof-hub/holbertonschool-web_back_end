# Python - Async

This project covers asynchronous programming concepts in Python using `asyncio`, coroutines, tasks, and measuring execution time as part of the Holberton School backend curriculum.

## Requirements
* Ubuntu 20.04 LTS using `python3` (version 3.8)
* `pycodestyle` compliance (version 2.5.x)
* All files are executable and end with a new line
* Type-annotated functions and documentation for all modules and functions

## Tasks

* **0. The basics of async**: `0-basic_async_syntax.py` - An async coroutine that waits for a random delay between `0` and `max_delay` seconds and returns it[cite: 2].
* **1. Let's execute multiple coroutines at the same time with async**: `1-concurrent_coroutines.py` - An async routine that spawns `wait_random` multiple times and returns the list of delays in ascending order[cite: 3].
* **2. Measure the runtime**: `2-measure_runtime.py` - A function that measures total execution time for `wait_n` and returns `total_time / n`[cite: 4].
* **3. Tasks**: `3-tasks.py` - A function that takes an integer `max_delay` and returns an `asyncio.Task`[cite: 5].
* **4. Tasks**: `4-tasks.py` - A modified version of `wait_n` that utilizes `task_wait_random`[cite: 6].
