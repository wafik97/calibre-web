from locust import HttpUser, task, between

class CalibreUser(HttpUser):
    wait_time = between(1, 3)
    #host = "http://localhost:8083"
    host = " https://7fcc-5-28-174-93.ngrok-free.app "

    @task
    def view_book_details(self):
        self.client.get("/book/6")


    @task
    def view_download(self):
        self.client.get("/download/stored/")

