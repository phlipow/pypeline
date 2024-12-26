import threading
from queue import Queue
from inspect import isgeneratorfunction

class Pipeline:

    def __init__(self, tasks):
        self._STOPPER = '__stop__'
        self._queues = [Queue() for _ in range(len(tasks) + 1)]
        self._threads = [threading.Thread(target=self._run_task_, args=(tasks[i], i)) for i in range(len(tasks))]

    def _run_task_(self, task, i):
        for item in iter(self._queues[i].get, self._STOPPER):
            if isgeneratorfunction(task):
                for result in task(item):
                    self._queues[i+1].put(result)  
            else:
                self._queues[i+1].put(task(item))
        self._queues[i+1].put(self._STOPPER)

    def put(self, item):
        self._queues[0].put(item)

    def get(self, generator=False):
        if not generator:
            result = self._queues[-1].get()
            return result if result != self._STOPPER else None
        else:
            yield from iter(self._queues[-1].get, self._STOPPER)

    def start(self):
        for thread in self._threads:
            thread.start()

    def stop(self):
        self._queues[0].put(self._STOPPER)
        for thread in self._threads:
            thread.join()
