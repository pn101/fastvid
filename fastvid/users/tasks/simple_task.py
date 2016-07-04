import requests


class SimpleTask:

    def run(self, instance):
        BASE_URL = 'http://api.openapi.io/ppurio/1/message/sms/dobestan'
        data = {
            'send_phone': '01031186228',
            'dest_phone': instance.phonenumber,
            'msg_body': 'Thank you for registering',
        }
        headers = {
            'x-waple-authorization': 'MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg=='
        }
        response = requests.post(BASE_URL, data=data, headers=headers)
        return response
