from send_notification_to_appsync import sendMessage

msg = {
    "id": "flag_id",
    "tenantCode": "9999",
    "action": "flag",
    "content": {"status": 'FINISHED'},
}

print('Before')
sendMessage(msg)
print('After')
