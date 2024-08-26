# Test script for the fine_depre-grained pet microservice system
from locust import HttpUser, TaskSet, task, between, events, constant_pacing
import random
import logging
from datetime import datetime
import os
import threading
import argparse

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)
log_filename = os.path.join(results_dir, f'locust_requests_{timestamp}.log')

logger = logging.getLogger('locust')
limit = 800
task_limits = {f"task_{i}": limit for i in range(1, 21)}
task_counters = {key: 0 for key in task_limits.keys()}
pacing = 0.2

counter_locks = [threading.Lock() for _ in range(21)]


@events.request.add_listener
def on_request(request_type, name, response_time, response_length, exception, context, **kwargs):
    if exception:
        logger.error(f'FAILURE: {request_type} {name} {response_time}ms {exception}')
    else:
        logger.info(f'SUCCESS: {request_type} {name} {response_time}ms {response_length} bytes')

class CustomerTask(TaskSet):
    @task
    def task_1(self):
        with counter_locks[0]:
            global task_counters, task_limits
            if task_counters['task_1'] < task_limits['task_1']:
                self.client.get("/owners")
                task_counters['task_1'] += 1
            else:
                logger.info("Request limit reached, skipping task")

class CustomerTask2(TaskSet):

    @task
    def task_2(self):
        with counter_locks[1]:
            global task_counters, task_limits
            if task_counters['task_2'] < task_limits['task_2']:
                id = random.randint(1, 10)
                self.client.get(f"/owners/{id}")
                task_counters['task_2'] += 1
            else:
                logger.info("Request limit reached, skipping task")

class PetsTask(TaskSet):
    @task
    def task_3(self):
        with counter_locks[2]:
            global task_counters, task_limits
            if task_counters['task_3'] < task_limits['task_3']:
                self.client.get("/petApi/petTypes")
                task_counters['task_3'] += 1
            else:
                logger.info("Request limit reached, skipping task")

class PetsTask2(TaskSet):

    @task
    def task_4(self):
        with counter_locks[3]:
            global task_counters, task_limits
            if task_counters['task_4'] < task_limits['task_4']:
                id = random.randint(1, 8)
                self.client.get(f"/petApi/owners/1/pets/{id}")
                task_counters['task_4'] += 1
            else:
                logger.info("Request limit reached, skipping task")
class VetsTask(TaskSet):
    @task
    def task_5(self):
        with counter_locks[4]:
            global task_counters, task_limits
            if task_counters['task_5'] < task_limits['task_5']:
                id = random.randint(1, 6)
                first_name = random.choice(["James", "Helen", "Linda", "Michael", "Mary", "John"])
                last_name = random.choice(["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis"])
                data = {
                    "firstName": first_name,
                    "lastName": last_name
                }
                self.client.post(f"/vets/Update/{id}", json=data)
                task_counters['task_5'] += 1
            else:
                logger.info("Request limit reached, skipping task")

class VetsTask2(TaskSet):

        @task
        def task_6(self):
            with counter_locks[5]:
                global task_counters, task_limits
                if task_counters['task_6'] < task_limits['task_6']:
                    id = random.randint(1, 6)
                    self.client.get(f"/vets/vets/{id}")
                    task_counters['task_6'] += 1
                else:
                    logger.info("Request limit reached, skipping task")

class VisitsTask(TaskSet):
    @task
    def task_7(self):
        with counter_locks[6]:
            global task_counters, task_limits
            if task_counters['task_7'] < task_limits['task_7']:
                self.client.get("/visits/visits")
                task_counters['task_7'] += 1
            else:
                logger.info("Request limit reached, skipping task")

class VisitsTask2(TaskSet):

        @task
        def task_8(self):
            with counter_locks[7]:
                global task_counters, task_limits
                if task_counters['task_8'] < task_limits['task_8']:
                    id = random.randint(1, 6)
                    data = {
                        "date": "2022-01-01",
                        "description": "Test visit",
                        "petId": id
                    }
                    self.client.post(f"/visits/visits/update/{id}",json=data)
                    task_counters['task_8'] += 1
                else:
                    logger.info("Request limit reached, skipping task")

class VetsTask3(TaskSet):

    @task
    def task_6(self):
        with counter_locks[9]:
            global task_counters, task_limits
            if task_counters['task_9'] < task_limits['task_9']:
                self.client.get("/vets")
                task_counters['task_9'] += 1
            else:
                logger.info("Request limit reached, skipping task")


class VisitsTask3(TaskSet):

        @task
        def task_9(self):
            with counter_locks[10]:
                global task_counters, task_limits
                if task_counters['task_10'] < task_limits['task_10']:
                    id = random.randint(1, 6)
                    self.client.get(f"/visits/pets/visits/{id}")
                    task_counters['task_10'] += 1
                else:
                    logger.info("Request limit reached, skipping task")



class CustomerTaskTest(HttpUser):
    tasks = [CustomerTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class CustomerTask2Test(HttpUser):
    tasks = [CustomerTask2]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class PetsTaskTest(HttpUser):
    tasks = [PetsTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class PetsTask2Test(HttpUser):
    tasks = [PetsTask2]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class VetsTaskTest(HttpUser):
    tasks = [VetsTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class VetsTask2Test(HttpUser):
    tasks = [VetsTask2]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class VisitsTaskTest(HttpUser):
    tasks = [VisitsTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class VetsTask3Test(HttpUser):
    tasks = [VetsTask3]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class VisitsTask3Test(HttpUser):
    tasks = [VisitsTask3]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

class VisitsTask2Test(HttpUser):
    tasks = [VisitsTask2]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:8081"

if __name__ == "__main__":
    import os
    import sys


    @events.quitting.add_listener
    def _(environment, **kwargs):
        logger.info(f"Total requests: {sum(task_counters.values())}")


    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--users", type=int, required=True, help="Number of users")
    parser.add_argument("-r", "--rate", type=int, required=True, help="Spawn rate")
    parser.add_argument("--run-time", type=str, required=True, help="Run time")
    parser.add_argument("--iteration", type=int, required=True, help="Iteration number")
    args = parser.parse_args()

    command = [
        sys.executable, "-m", "locust",
        "-f", __file__,
        "--headless",
        "-u", str(args.users),  # Number of users
        "-r", str(args.rate),  # Spawn rate
        "--run-time", args.run_time,
        "--csv=locust_report",
        f"--logfile=results/coarse/locustfile_even_high_{pacing}_{args.users}_{args.rate}_{args.run_time}_{args.iteration}.log"
    ]
    os.system(" ".join(command))
