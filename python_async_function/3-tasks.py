#!/usr/init/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Module for 3-tasks.
Contains a function that returns an asyncio.Task.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns a asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
