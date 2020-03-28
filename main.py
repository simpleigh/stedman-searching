import numpy as np
from queue import Queue

from stedman_searching.lengths_table import LengthsTable
from stedman_searching.queue_item import QueueItem
from stedman_searching.rows import perm_from_row
from stedman_searching.stedman import generate_next_perms
from stedman_searching.timer import Timer


DISTANCE_THRESHOLD = 14
largest_seen = 0

queue = Queue()
queue.put(QueueItem(perm_from_row('1234567890E'), 0))

table = LengthsTable(11)

timer = Timer()

while not queue.empty():
    item = queue.get()

    if item.distance > largest_seen:
        largest_seen = item.distance
        print(f'{largest_seen}, {timer.split()}')

    new_distance = item.distance + 2

    if new_distance > DISTANCE_THRESHOLD:
        continue

    new_perms = generate_next_perms(item.perm)
    for new_perm in new_perms:
        index = new_perm.rank_nonlex()
        if table.add(index, new_distance):
            queue.put(QueueItem(new_perm, new_distance))

timer.split()

distances = np.histogram(
    table._table,
    bins=DISTANCE_THRESHOLD // 2 + 1,
    range=(0, DISTANCE_THRESHOLD + 2)
)
print(distances[0])

print(f'histogram() took {timer.split()}')
