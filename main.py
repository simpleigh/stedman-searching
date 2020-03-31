from queue import Queue

from stedman_searching.distances_array import DistancesArray
from stedman_searching.profiling import Profiler, Timer
from stedman_searching.queue_item import QueueItem
from stedman_searching.rows import perm_for_rounds, perm_from_row
from stedman_searching.stedman import multiply_end_perms_from_perm


DISTANCE_THRESHOLD = 14
STAGE = 11

largest_seen = 0

array = DistancesArray(STAGE)
profiler = Profiler()
queue = Queue()
timer = Timer()

profiler.start()

queue.put(QueueItem(perm_for_rounds(STAGE), 0))
while not queue.empty():
    item = queue.get()

    if item.distance > largest_seen:
        largest_seen = item.distance
        print(f'{largest_seen}, {timer.split()}')

    new_distance = item.distance + 2

    if new_distance > DISTANCE_THRESHOLD:
        continue

    new_perms = multiply_end_perms_from_perm(item.perm)
    for new_perm in new_perms:
        index = new_perm.rank_nonlex()
        if array.add(index, new_distance):
            queue.put(QueueItem(new_perm, new_distance))

print(timer.split())
print(array.get_counts())
print(f'get_counts() took {timer.split()}')

profiler.end()
