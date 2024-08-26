# Test script for the fine_depre-grained train-ticketing microservice system
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
limit = 200
task_limits = {f"task_{i}": limit for i in range(1, 42)}
task_counters = {key: 0 for key in task_limits.keys()}
half_task_limits = {f"task_{i}": limit/2 for i in range(1, 5)}
half_task_counters = {key: 0 for key in half_task_limits.keys()}
pacing = 0.01

counter_locks = [threading.Lock() for _ in range(42)]


@events.request.add_listener
def on_request(request_type, name, response_time, response_length, exception, context, **kwargs):
    if exception:
        logger.error(f'FAILURE: {request_type} {name} {response_time}ms {exception}')
    else:
        logger.info(f'SUCCESS: {request_type} {name} {response_time}ms {response_length} bytes')


class StationServiceTask(TaskSet):
    @task
    def post_request(self):
        global task_counters, task_limits
        with counter_locks[0]:
            if task_counters["task_1"] < task_limits["task_1"]:
                task_counters["task_1"] += 1
                name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
                payload = {
                    "id": "string",
                    "name": name,
                    "stayTime": 2
                }
                self.client.post("/api/v1/stationservice/stations", json=payload)
            else:
                logger.info("Request limit reached, skipping task")


class PriceServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[1]:
            if task_counters["task_2"] < task_limits["task_2"]:
                task_counters["task_2"] += 1
                self.client.get("/api/v1/priceservice/prices")
            else:
                logger.info("Request limit reached, skipping task")


class TrainFoodServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[2]:
            if task_counters["task_3"] < task_limits["task_3"]:
                task_counters["task_3"] += 1
                self.client.get("/api/v1/trainfoodservice/trainfoods")
            else:
                logger.info("Request limit reached, skipping task")


class TrainServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[3]:
            if task_counters["task_4"] < task_limits["task_4"]:
                task_counters["task_4"] += 1
                self.client.get("/api/v1/trainservice/trains")
            else:
                logger.info("Request limit reached, skipping task")


class RouteServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[4]:
            if task_counters["task_5"] < task_limits["task_5"]:
                task_counters["task_5"] += 1
                self.client.get("/api/v1/routeservice/routes")
            else:
                logger.info("Request limit reached, skipping task")


class ContactsServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[5]:
            if task_counters["task_6"] < task_limits["task_6"]:
                task_counters["task_6"] += 1
                self.client.get("/api/v1/contactservice/contacts")
            else:
                logger.info("Request limit reached, skipping task")


class AdminBasicInfoServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[6]:
            if task_counters["task_7"] < task_limits["task_7"]:
                task_counters["task_7"] += 1
                self.client.get("/api/v1/adminbasicservice/adminbasic/contacts")
            else:
                logger.info("Request limit reached, skipping task")


# class AdminBasicInfoServiceTask2(TaskSet):
#
#     @task
#     def get_request(self):
#         global task_counters, task_limits
#         with counter_lock_8:
#             if task_counters["task_8"] < task_limits["task_8"]:
#                 task_counters["task_8"] += 1
#                 self.client.get("/api/v1/adminbasicservice/adminbasic/stations")
#             else:
#                 logger.info("Request limit reached, skipping task")


class AdminBasicInfoServiceTask3(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[7]:
            if task_counters["task_9"] < task_limits["task_9"]:
                task_counters["task_9"] += 1
                self.client.get("/api/v1/adminbasicservice/adminbasic/prices")
            else:
                logger.info("Request limit reached, skipping task")


class AdminOrderServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[8]:
            if task_counters["task_10"] < task_limits["task_10"]:
                task_counters["task_10"] += 1
                self.client.get("/api/v1/adminorderservice/adminorder")
            else:
                logger.info("Request limit reached, skipping task")


class BasicServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[9]:
            if task_counters["task_11"] < task_limits["task_11"]:
                task_counters["task_11"] += 1
                cities = ["beijing", "shanghai", "xuzhou", "hangzhou"]
                city = random.choice(cities)
                self.client.get(f"/api/v1/basicservice/basic/{city}")
            else:
                logger.info("Request limit reached, skipping task")


class OrderServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[10]:
            if task_counters["task_12"] < task_limits["task_12"]:
                task_counters["task_12"] += 1
                self.client.get("/api/v1/orderservice/order")
            else:
                logger.info("Request limit reached, skipping task")


class OrderService2Task(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[11]:
            if task_counters["task_13"] < task_limits["task_13"]:
                task_counters["task_13"] += 1
                orderId = "9bb0ac3e-b305-4929-84a9-2dfac9de3471"
                self.client.get(f"/api/v1/orderservice/order/{orderId}")
            else:
                logger.info("Request limit reached, skipping task")


class OrderOtherServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[12]:
            if task_counters["task_14"] < task_limits["task_14"]:
                task_counters["task_14"] += 1
                self.client.get("/api/v1/orderOtherService/orderOther")
            else:
                logger.info("Request limit reached, skipping task")


class SeatServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[13]:
            if task_counters["task_15"] < task_limits["task_15"]:
                task_counters["task_15"] += 1
                self.client.get("/api/v1/seatservice/welcome")
            else:
                logger.info("Request limit reached, skipping task")


class StationFoodServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[14]:
            if task_counters["task_16"] < task_limits["task_16"]:
                task_counters["task_16"] += 1
                cities = ["beijing", "shanghai", "nanjing", "hangzhou"]
                self.client.get("/api/v1/stationfoodservice/stationfoodstores", json=cities)
            else:
                logger.info("Request limit reached, skipping task")


class Travel2ServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[15]:
            if task_counters["task_17"] < task_limits["task_17"]:
                task_counters["task_17"] += 1
                self.client.get("/api/v1/travel2service/trips")
            else:
                logger.info("Request limit reached, skipping task")


class UserServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[16]:
            if task_counters["task_18"] < task_limits["task_18"]:
                task_counters["task_18"] += 1
                password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz123456', k=7))
                user = {
                    "documentNum": "2135488099312X",
                    "documentType": 1,
                    "email": "trainticket_notify@163.com",
                    "gender": 1,
                    "password": password,
                    "userId": "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f",
                    "userName": "fdse_microservice"
                }
                self.client.put("/api/v1/userservice/users", json=user)
            else:
                logger.info("Request limit reached, skipping task")


class AdminTravelServiceTask(TaskSet):

    @task
    def get_request(self):
        global half_task_counters, half_task_limits
        with counter_locks[17]:
            if half_task_counters["task_1"] < half_task_limits["task_1"]:
                half_task_counters["task_1"] += 1
                self.client.get("/api/v1/admintravelservice/admintravel")
            else:
                logger.info("Request limit reached, skipping task")

class AdminTravelServiceTask2(TaskSet):

    @task
    def get_request(self):
        global half_task_counters, half_task_limits
        with counter_locks[18]:
            if half_task_counters["task_2"] < half_task_limits["task_2"]:
                half_task_counters["task_2"] += 1
                self.client.get("/api/v1/admintravelservice/admintravel")
            else:
                logger.info("Request limit reached, skipping task")


class AdminRouteServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[19]:
            if task_counters["task_20"] < task_limits["task_20"]:
                task_counters["task_20"] += 1
                self.client.get("/api/v1/adminrouteservice/adminroute")
            else:
                logger.info("Request limit reached, skipping task")
        # self.client.get("/api/v1/adminrouteservice/adminroute")


class AdminUserServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/adminuserservice/users")
        global task_counters, task_limits
        with counter_locks[20]:
            if task_counters["task_21"] < task_limits["task_21"]:
                task_counters["task_21"] += 1
                self.client.get("/api/v1/adminuserservice/users")
            else:
                logger.info("Request limit reached, skipping task")


class AssuranceServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/assuranceservice/assurances")
        global task_counters, task_limits
        with counter_locks[21]:
            if task_counters["task_22"] < task_limits["task_22"]:
                task_counters["task_22"] += 1
                self.client.get("/api/v1/assuranceservice/assurances")
            else:
                logger.info("Request limit reached, skipping task")


class ConfigServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/configservice/configs")
        global task_counters, task_limits
        with counter_locks[22]:
            if task_counters["task_23"] < task_limits["task_23"]:
                task_counters["task_23"] += 1
                self.client.get("/api/v1/configservice/configs")
            else:
                logger.info("Request limit reached, skipping task")


class ConsignPriceServiceTask(TaskSet):

    @task
    def post_request(self):
        # randon generate beyondPrice, initialPrice
        global task_counters, task_limits
        with counter_locks[23]:
            if task_counters["task_24"] < task_limits["task_24"]:
                task_counters["task_24"] += 1
                price = {
                    "beyondPrice": 1,
                    "id": "c892a88a-0991-4cc4-8012-84613e7aee46",
                    "index": 0,
                    "initialPrice": 2,
                    "initialWeight": 1,
                    "withinPrice": 2
                }
                self.client.post("/api/v1/consignpriceservice/consignprice", json=price)
            else:
                logger.info("Request limit reached, skipping task")


class ConsignServiceTask(TaskSet):

    @task
    def get_request(self):
        # id = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
        # self.client.get(f"/api/v1/consignservice/consigns/account/{id}")
        global task_counters, task_limits
        with counter_locks[24]:
            if task_counters["task_25"] < task_limits["task_25"]:
                task_counters["task_25"] += 1
                id = "c892a88a-0991-4cc4-8012-84613e7aee46"
                self.client.get(f"/api/v1/consignservice/consigns/account/{id}")
            else:
                logger.info("Request limit reached, skipping task")


class NotificationServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/notifyservice/test_send_mq")
        global task_counters, task_limits
        with counter_locks[25]:
            if task_counters["task_26"] < task_limits["task_26"]:
                task_counters["task_26"] += 1
                self.client.get("/api/v1/notifyservice/test_send_mq")
            else:
                logger.info("Request limit reached, skipping task")


class SecurityServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/securityservice/securityConfigs")
        global task_counters, task_limits
        with counter_locks[26]:
            if task_counters["task_27"] < task_limits["task_27"]:
                task_counters["task_27"] += 1
                self.client.get("/api/v1/securityservice/securityConfigs")
            else:
                logger.info("Request limit reached, skipping task")


class TravelServiceTask(TaskSet):

    @task
    def get_request(self):
        # tripId = "G1234"
        # self.client.get("/api/v1/travelservice/train_types/{tripId}")
        global task_counters, task_limits
        with counter_locks[27]:
            if task_counters["task_28"] < task_limits["task_28"]:
                task_counters["task_28"] += 1
                tripId = "G1234"
                self.client.get(f"/api/v1/travelservice/train_types/{tripId}")
            else:
                logger.info("Request limit reached, skipping task")


class CancelServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/cancelservice/welcome")
        global task_counters, task_limits
        with counter_locks[28]:
            if task_counters["task_29"] < task_limits["task_29"]:
                task_counters["task_29"] += 1
                self.client.get("/api/v1/cancelservice/welcome")
            else:
                logger.info("Request limit reached, skipping task")


class ExeServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/executeservice/welcome")
        global task_counters, task_limits
        with counter_locks[29]:
            if task_counters["task_30"] < task_limits["task_30"]:
                task_counters["task_30"] += 1
                self.client.get("/api/v1/executeservice/welcome")
            else:
                logger.info("Request limit reached, skipping task")


class FoodDeliverServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/fooddeliveryservice/orders/all")
        global task_counters, task_limits
        with counter_locks[30]:
            if task_counters["task_31"] < task_limits["task_31"]:
                task_counters["task_31"] += 1
                self.client.get("/api/v1/fooddeliveryservice/orders/all")
            else:
                logger.info("Request limit reached, skipping task")


class FoodServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/foodservice/orders")
        global task_counters, task_limits
        with counter_locks[31]:
            if task_counters["task_32"] < task_limits["task_32"]:
                task_counters["task_32"] += 1
                self.client.get("/api/v1/foodservice/orders")
            else:
                logger.info("Request limit reached, skipping task")


class InsidePaymentServiceTask(TaskSet):

    @task
    def get_request(self):
        global task_counters, task_limits
        with counter_locks[32]:
            if task_counters["task_33"] < task_limits["task_33"]:
                task_counters["task_33"] += 1
                self.client.get("/api/v1/inside_pay_service/inside_payment/account")
            else:
                logger.info("Request limit reached, skipping task")
        # self.client.get("/api/v1/inside_pay_service/inside_payment/account")


class OrderOther2ServiceTask(TaskSet):

    @task
    def get_request(self):
        # travelDate = "2013-08-09"
        # trainNumber = "1"
        # self.client.get(f"/api/v1/orderOtherService/orderOther/{travelDate}/{trainNumber}")
        global task_counters, task_limits
        with counter_locks[33]:
            if task_counters["task_34"] < task_limits["task_34"]:
                task_counters["task_34"] += 1
                travelDate = "2013-08-09"
                trainNumber = "1"
                self.client.get(f"/api/v1/orderOtherService/orderOther/{travelDate}/{trainNumber}")
            else:
                logger.info("Request limit reached, skipping task")


class PaymentServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/paymentservice/payment")
        global task_counters, task_limits
        with counter_locks[34]:
            if task_counters["task_35"] < task_limits["task_35"]:
                task_counters["task_35"] += 1
                self.client.get("/api/v1/paymentservice/payment")
            else:
                logger.info("Request limit reached, skipping task")


class PreserveServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/preserveservice/welcome")
        global task_counters, task_limits
        with counter_locks[35]:
            if task_counters["task_36"] < task_limits["task_36"]:
                task_counters["task_36"] += 1
                self.client.get("/api/v1/preserveservice/welcome")
            else:
                logger.info("Request limit reached, skipping task")


class RebookServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/rebookservice/welcome")
        global task_counters, task_limits
        with counter_locks[36]:
            if task_counters["task_37"] < task_limits["task_37"]:
                task_counters["task_37"] += 1
                self.client.get("/api/v1/rebookservice/welcome")
            else:
                logger.info("Request limit reached, skipping task")


class waitorderServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/waitorderservice/orders")
        global task_counters, task_limits
        with counter_locks[37]:
            if task_counters["task_38"] < task_limits["task_38"]:
                task_counters["task_38"] += 1
                self.client.get("/api/v1/waitorderservice/orders")
            else:
                logger.info("Request limit reached, skipping task")


class TravelPlanServiceTask(TaskSet):

    @task
    def post_request(self):
        # processed_data = {
        #    "departureTime": "2013-08-12",
        #    "endPlace": "shanghai",
        #    "startPlace": "nanjing"
        # }
        # self.client.post("/api/v1/travelplanservice/travelPlan/cheapest", json=processed_data)
        global task_counters, task_limits
        with counter_locks[38]:
            if task_counters["task_39"] < task_limits["task_39"]:
                task_counters["task_39"] += 1
                data = {
                    "departureTime": "2013-08-12",
                    "endPlace": "shanghai",
                    "startPlace": "nanjing"
                }
                self.client.post("/api/v1/travelplanservice/travelPlan/cheapest", json=data)
            else:
                logger.info("Request limit reached, skipping task")


class RoutePlanServiceTask(TaskSet):

    @task
    def post_request(self):
        # processed_data = {
        #     "endStation": "shanghai",
        #     "num": 0,
        #     "startStation": "nanjing",
        #     "travelDate": "2013-08-01"
        # }
        # self.client.post("/api/v1/routeplanservice/routePlan/cheapestRoute", json=processed_data)
        global task_counters, task_limits
        with counter_locks[39]:
            if task_counters["task_40"] < task_limits["task_40"]:
                task_counters["task_40"] += 1
                data = {
                    "endStation": "shanghai",
                    "num": 0,
                    "startStation": "nanjing",
                    "travelDate": "2013-08-01"
                }
                self.client.post("/api/v1/routeplanservice/routePlan/cheapestRoute", json=data)
            else:
                logger.info("Request limit reached, skipping task")


class PreserveOtherServiceTask(TaskSet):

    @task
    def get_request(self):
        # self.client.get("/api/v1/preserveotherservice/welcome")
        global task_counters, task_limits
        with counter_locks[40]:
            if task_counters["task_41"] < task_limits["task_41"]:
                task_counters["task_41"] += 1
                self.client.get("/api/v1/preserveotherservice/welcome")
            else:
                logger.info("Request limit reached, skipping task")


# Station Service Test
class StationService(HttpUser):
    tasks = [StationServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12345"

# Price Service Test
class PriceService(HttpUser):
    tasks = [PriceServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:16579"

# Train Food Service Test
class TrainFoodService(HttpUser):
    tasks = [TrainFoodServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:14567"

#  Train Service Test
class TrainService(HttpUser):
    tasks = [TrainServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:14567"

# Route Service Test
class RouteService(HttpUser):
    tasks = [RouteServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:11178"

# Contacts Service Test
class ContactsService(HttpUser):
    tasks = [ContactsServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12347"

# Admin Basic Info Service Test
class AdminBasicInfoService(HttpUser):
    tasks = [AdminBasicInfoServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18767"

# # Admin Basic Info Service Test2
# class AdminBasicInfoService2(HttpUser):
#     tasks = [AdminBasicInfoServiceTask2]
#     wait_time = constant_pacing(pacing)
#     host = "http://145.108.225.14:18767"

# Admin Basic Info Service Test3
class AdminBasicInfoService3(HttpUser):
    tasks = [AdminBasicInfoServiceTask3]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18767"

# Admin Order Service Test
class AdminOrderService(HttpUser):
    tasks = [AdminOrderServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:16113"

# Basic Service Test
class BasicService(HttpUser):
    tasks = [BasicServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:15680"

# Order Service Test
class OrderService(HttpUser):
    tasks = [OrderServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12031"

# Order Service Test2
class OrderService2(HttpUser):
    tasks = [OrderService2Task]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12031"

# Order Other Service Test
class OrderOtherService(HttpUser):
    tasks = [OrderOtherServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12032"

# Seat Service Test
class SeatService(HttpUser):
    tasks = [SeatServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18898"

# Station Food Service Test
class StationFoodService(HttpUser):
    tasks = [StationFoodServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12345"

# Travel2 Service Test
class Travel2Service(HttpUser):
    tasks = [Travel2ServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:16346"

# User Service Test
class UserService(HttpUser):
    tasks = [UserServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12346"

#Admin Travel Service Test
class AdminTravelService(HttpUser):
    tasks = [AdminTravelServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:17525"

class AdminTravelService2(HttpUser):
    tasks = [AdminTravelServiceTask2]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:17525"

# Admin Route Service Test
class AdminRouteService(HttpUser):
    tasks = [AdminRouteServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:16113"

# Admin User Service Test
class AdminUserService(HttpUser):
    tasks = [AdminUserServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18888"

# Assurance Service Test
class AssuranceService(HttpUser):
    tasks = [AssuranceServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18888"

# Config Service Test
class ConfigService(HttpUser):
    tasks = [ConfigServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:15679"

# Consign Price Service Test
class ConsignPriceService(HttpUser):
    tasks = [ConsignPriceServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:15679"

# Consign Service Test
class ConsignService(HttpUser):
    tasks = [ConsignServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12347"

# Notification Service Test
class NotificationService(HttpUser):
    tasks = [NotificationServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:17853"

# Security Service Test
class SecurityService(HttpUser):
    tasks = [SecurityServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18898"

# Travel Service Test
class TravelService(HttpUser):
    tasks = [TravelServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12346"

# Cancel Service Test
class CancelService(HttpUser):
    tasks = [CancelServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:15680"

# Execute Service Test
class ExecuteService(HttpUser):
    tasks = [ExeServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18957"

# Food Deliver Service Test
class FoodDeliverService(HttpUser):
    tasks = [FoodDeliverServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18957"

# Food Service Test
class FoodService(HttpUser):
    tasks = [FoodServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18856"

#InsidePaymentServiceTask Service Test
class InsidePaymentService(HttpUser):
    tasks = [InsidePaymentServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18673"

#OrderOther2ServiceTask Service Test
class OrderOther2Service(HttpUser):
    tasks = [OrderOther2ServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:12032"

#paymentservice Service Test
class PaymentService(HttpUser):
    tasks = [PaymentServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:17853"

#PreserveServiceTask Service Test
class PreserveService(HttpUser):
    tasks = [PreserveServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18856"

#rebool Service Test
class RebookService(HttpUser):
    tasks = [RebookServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:16579"

#waitorderservice Service Test
class WaitOrderService(HttpUser):
    tasks = [waitorderServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:17525"

#Travel plan Service Test
class TravelPlanService(HttpUser):
    tasks = [TravelPlanServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:16346"

#RoutePlanServiceTask Service Test
class RoutePlanService(HttpUser):
    tasks = [RoutePlanServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:11178"

#PreserveOtherServiceTask
class PreserveOtherService(HttpUser):
    tasks = [PreserveOtherServiceTask]
    wait_time = constant_pacing(pacing)
    host = "http://145.108.225.14:18673"


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
        f"--logfile=results/med/locustfile_burst_high_{pacing}_{args.users}_{args.rate}_{args.run_time}_{args.iteration}.log"
    ]
    os.system(" ".join(command))
