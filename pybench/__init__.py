import multiprocessing
import time
from pybench.fakeswitch import FakeSwitch


def benchmark_switch(host, port, dpid, queue, duration):
    switch = FakeSwitch(host, port, dpid=dpid)
    switch.register()
    end_time = time.time() + duration
    while time.time() < end_time:
        switch.send_packet_in()
        switch.proc_step()

    switch.close()
    queue.put(switch.get_packet_count())


def benchmark(host, port, num_of_switches, duration):
    queue = multiprocessing.Queue()
    processes = [multiprocessing.Process(
        target=benchmark_switch, args=(host, port, dpid, queue, duration))
        for dpid in range(num_of_switches)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    items = []
    while not queue.empty():
        items.append(queue.get())

    for index, item in enumerate(items):
        print('{}: {}'.format(index, item))

    print('Total: {}'.format(sum(items)))
