import requests


def send_sms(sender, receiver, content):
    BASE_URL = 'http://api.openapi.io/ppurio/1/message/sms/dobestan'
    data = {
        'send_phone': sender,
        'dest_phone': receiver,
        'msg_body': content,
    }
    headers = {
        'x-waple-authorization': 'MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg=='
    }
    response = requests.post(BASE_URL, data=data, headers=headers)
    return response
