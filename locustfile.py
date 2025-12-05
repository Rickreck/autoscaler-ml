from locust import HttpUser, task, between

class MLUser(HttpUser):
    host = "https://autoscaler-ml-api-197064753472.us-central1.run.app"
    wait_time = between(0.1, 0.5)

    @task
    def predict(self):
        self.client.post("/predict", json={"size_m2": 120})
