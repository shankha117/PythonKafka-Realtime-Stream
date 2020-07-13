from multiprocessing import Process
import  traceback
# load configs
from config_loader import load_config
load_config()
from kafka_producer import Producers



def start_all_producers():
    try:
        p1 = Process(target=Producers().start_producer, args=(1,))
        p2 = Process(target=Producers().start_producer, args=(2,))
        p3 = Process(target=Producers().start_producer, args=(3,))

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()


    except Exception as e:
        print(traceback.format_exc())

start_all_producers()
