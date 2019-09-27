import json

from kivy.network.urlrequest import UrlRequest

from store.manager import Manager

manager = Manager()


class APIManager (object):

    def get_init_data(self):
        host = 'http://10.0.1.90:8000'
        endpoint = '/locations/all/'
        url = host + endpoint
        headers = {'content-type': "application/json"}

        req = UrlRequest(
            url=url,
            req_headers=headers,
            method='GET',
            on_success=self.init_response,
            on_failure=self.init_failure,
        )

    def init_failure(self, req, result):
        print(f'We failed with: {result}')

    def init_response(self, req, result):
        data = result[0]['controllers'][0]['switches']
        manager.switch_manager.initial_data(data)
        data = result[0]['controllers'][0]['sensors']
        manager.sensor_manager.initial_data(data)

    def patch(self, uuid, value):
        host = 'http://10.0.1.90:8000'
        endpoint = f'/switches/switches/{uuid}/'
        url = host + endpoint

        headers = {'content-type': "application/json"}
        body = {
            "sw_value": value
        }
        body = json.dumps(body)

        req = UrlRequest(
            url=url,
            req_headers=headers,
            req_body=body,
            method='PATCH',
            on_success=self.patch_response,
            on_failure=self.patch_failure,
        )

    def patch_response(self, req, response):
        # print(response)
        # uuid = response['id']
        # value = response['sw_value']
        # print(uuid, value)
        # manager.switch_manager.update_object(
        #   uuid = response['id'],
        #   value = response['sw_value']
        #   )
        # print(response)
        pass

    def patch_failure(self, req, result):
        print(f'We failed with: {result}')
