import multiprocessing
import time
from pybench.fakeswitch import FakeSwitch
from pybench.util import make_random_mac, make_random_ip


def benchmark_switch(switch, queue, duration):
    dstmac = make_random_mac()
    dstip = '192.168.0.2'

    end_time = time.time() + duration
    while time.time() < end_time:
        switch.send_packet_in(
            srcmac=make_random_mac(), dstmac=dstmac,
            srcip=make_random_ip(), dstip=dstip)
        switch.proc_step()

    switch.close()
    queue.put(switch.get_packet_count())


def benchmark(host, port, num_of_switches, duration):
    queue = multiprocessing.Queue()
    switches = [FakeSwitch(host, port, dpid)
                for dpid in range(num_of_switches)]
    processes = [multiprocessing.Process(
        target=benchmark_switch, args=(switch, queue, duration))
        for switch in switches]

    for switch in switches:
        switch.register()

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
