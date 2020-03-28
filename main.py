from cProfile import Profile
from pstats import Stats
from queue import Queue

from stedman_searching.distances_table import DistancesTable
from stedman_searching.queue_item import QueueItem
from stedman_searching.rows import perm_from_row
from stedman_searching.stedman import multiply_end_perms_from_perm
from stedman_searching.timer import Timer


DISTANCE_THRESHOLD = 14
largest_seen = 0

profile = Profile()
profile.enable()

queue = Queue()
queue.put(QueueItem(perm_from_row('1234567890E'), 0))

table = DistancesTable(11)

timer = Timer()

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
        if table.add(index, new_distance):
            queue.put(QueueItem(new_perm, new_distance))

print(timer.split())
print(table.get_counts())
print(f'get_counts() took {timer.split()}')

stats = Stats(profile)
stats.sort_stats('cumulative')
stats.print_stats(20)
