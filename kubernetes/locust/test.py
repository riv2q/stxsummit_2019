from locust import HttpLocust, TaskSet, task


class StatlessAppTestSet(TaskSet):
    """kubernetes load test"""

    @task
    def get_asset_metadata(self):
        url = "/guestbook.php?cmd=set&key=messages&value=,dsa,test"
        self.client.get(url)


class User(HttpLocust):
    task_set = StatlessAppTestSet
