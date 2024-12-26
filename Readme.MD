# Pypeline

This repository contains a Python implementation of a simple pipeline for processing tasks using threads and queues.

## Overview

The `Pipeline` class allows you to create a series of tasks that can be executed in sequence. Each task can be a function or a generator function. The pipeline uses threads to run each task concurrently, passing the output of one task as the input to the next.

## Features

- Supports both regular functions and generator functions as tasks.
- Uses threading for concurrent execution of tasks.
- Utilizes queues to manage the flow of data between tasks.
- Provides methods to start and stop the pipeline.

## Usage

### Initialization

To create a pipeline, initialize it with a list of tasks:

```python
from pypeline import Pipeline

def task1(item):
    return item + 1

def task2(item):
    yield item * 2

tasks = [task1, task2]
pipeline = Pipeline(tasks)
```

### Adding Items

To add an item to the pipeline, use the `put` method:

```python
pipeline.put(1)
```

### Retrieving Results

To retrieve results from the pipeline, use the `get` method:

```python
result = pipeline.get()
print(result)  # Output will depend on the tasks defined
```

You can also retrieve results as a generator:

```python
for result in pipeline.get(generator=True):
    print(result)
```

### Starting and Stopping the Pipeline

To start the pipeline, use the `start` method:

```python
pipeline.start()
```

To stop the pipeline, use the `stop` method:

```python
pipeline.stop()
```

