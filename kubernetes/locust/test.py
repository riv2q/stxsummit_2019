import random
import string

from locust import HttpLocust, TaskSet, task


class StatlessAppTestSet(TaskSet):
    """Asset metadata test"""

    @task
    def get_asset_metadata(self):
        random_text = lambda length: ''.join(
            random.sample(string.ascii_letters, length))
        url = "/guestbook.php?cmd=set&key=messages&value=,dsa,test"

        with self.client.get(
            url,
            catch_response=True
        ) as response:
            text_response = str(response.content)
            if "fail" in text_response:
                response.failure(text_response)


class User(HttpLocust):
    task_set = StatlessAppTestSet
    min_wait = 5000
    max_wait = 15000
