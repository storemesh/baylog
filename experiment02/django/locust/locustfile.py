from locust import HttpUser, task, constant_throughput
import random
import json

class TestProfileUser(HttpUser):
    wait_time = constant_throughput(50)

    @task
    def read_profile(self):
        id = random.randrange(1, 51)
        url = f"/api/v1/profile/{id}/"
        with self.client.get(url, catch_response=True) as response:
            print(f'read, {response.status_code}, {url}' )

    @task
    def update_profile(self):
        id = random.randrange(1, 51)
        url = f'/api/v1/profile/{id}/'
        data = {
            "name": f"test_{id}"
        }
        payload = json.dumps(data)
        headers = {'content-type': 'application/json'}
        with  self.client.patch(url, headers=headers,  json=data,  catch_response=True) as response:
            print(f'update, {response.status_code}, {url}' )
