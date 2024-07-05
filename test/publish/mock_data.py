import json
import math
import decimal


class Common:
    FILE_TYPE_TRADE_REGISTRATION_MASKED_PASSWORD = (
        "TradeRegistrationMaskedPassword"  # 貿易登録証(パスワードマスク済)
    )

    @classmethod
    def get_str_number(cls, no):
        if type(no) is float:
            no = math.floor(no)
        elif type(no) is decimal.Decimal:
            no = int(no)
        return str(no)


def get_trade_registration_pdf_s3_path(
    cci_code, company_code, code1, code2, report_type
):
    company_code = Common.get_str_number(company_code)
    file_name = "trade_registration_{}_{}.pdf".format(code1, code2)
    if report_type == Common.FILE_TYPE_TRADE_REGISTRATION_MASKED_PASSWORD:
        file_name = "trade_registration_{}_{}_masked.pdf".format(code1, code2)
    result = "content/{}/company/{}/trade_registration/{}".format(
        cci_code, company_code, file_name
    )
    return result


# Lambda '${Env}-${ServiceName}-report-stream'
# /home/pionero/Desktop/Workspace/jcci/jcci_eco_api_v2/handlers/v2/report/process_sqs_stream.py

# record_handler:28

record = {
    "attributes": {
        "approximate_first_receive_timestamp": "1715699308792",
        "approximate_receive_count": "1",
        "aws_trace_header": "None",
        "message_deduplication_id": "None",
        "message_group_id": "None",
        "raw_event": "[SENSITIVE]",
        "sender_id": "AIDAIERWYNSNBY7YRB6SY",
        "sent_timestamp": "1715699308784",
        "sequence_number": "None",
    },
    "aws_region": "ap-northeast-1",
    "body": {
        "Type": "Notification",
        "MessageId": "29e6e841-264c-52e5-a679-b6fca6e03576",
        "TopicArn": "arn:aws:sns:ap-northeast-1:206719415840:dev-eco-topic",
        "Message": {
            "file_storage_id": 11769,
            "cci_code": 8888,
            "user_id": "murakami",
            "file_type": "TradeRegistrationMaskedPassword",
            "file_type2": "null",
            "trade_company_code": "8888000008",
            "code1": "8888000008",
            "code2": "7c0716f84a3f18d4756ea044af92e5c9",
            "topic_type": "report",
        },
        "Timestamp": "2024-05-14T15:08:28.718Z",
        "SignatureVersion": "1",
        "Signature": "FsnFYex4XTbCR2iGGrwwwu/Q8fLjF126RhOEwUNcdxMZVpuW2Gvb/XKIO32/HGzek+FvkUKTtsCIMXaHcaEqngISmYETfiGHeaH+jhJpKCNWhx4KGtC1VJHTtOi6ENtfl2bRhB0GSv8yNNZ/MbK+yA3nPzwKWgaPiMCb8Bz3n5R42r+C7rsUqU7XkDmxzbp/pWUUMsvn2OiaZHPLkAxNCrEYqHEkUyMRRrOFamI+SHbIKeef1B/NrQxNgxTXei6yvWmhd5WnCAPQCXMSXB/XqWEC5SL8eLegR7YqauGzEUcipllWPPPfUsqDIhuXN0O8Ox2tWh2nfXNdyC/GrQd4Eg==",
        "SigningCertURL": "https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-60eadc530605d63b8e62a523676ef735.pem",
        "UnsubscribeURL": "https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:206719415840:dev-eco-topic:ccb12801-4749-44a3-b36e-6474483e474e",
        "MessageAttributes": {
            "system_tenant_id": {"Type": "String", "Value": "jcci"},
            "system_id": {"Type": "String", "Value": "jcci"},
            "env": {"Type": "String", "Value": "dev"},
            "topic_type": {"Type": "String", "Value": "report"},
        },
    },
    "event_source": "aws:sqs",
    "event_source_arn": "arn:aws:sqs:ap-northeast-1:206719415840:dev-eco-report-queue",
    "json_body": {
        "Type": "Notification",
        "MessageId": "29e6e841-264c-52e5-a679-b6fca6e03576",
        "TopicArn": "arn:aws:sns:ap-northeast-1:206719415840:dev-eco-topic",
        "Message": {
            "file_storage_id": 11769,
            "cci_code": 8888,
            "user_id": "murakami",
            "file_type": "TradeRegistrationMaskedPassword",
            "file_type2": "null",
            "trade_company_code": "8888000008",
            "code1": "8888000008",
            "code2": "7c0716f84a3f18d4756ea044af92e5c9",
            "topic_type": "report",
        },
        "Timestamp": "2024-05-14T15:08:28.718Z",
        "SignatureVersion": "1",
        "Signature": "FsnFYex4XTbCR2iGGrwwwu/Q8fLjF126RhOEwUNcdxMZVpuW2Gvb/XKIO32/HGzek+FvkUKTtsCIMXaHcaEqngISmYETfiGHeaH+jhJpKCNWhx4KGtC1VJHTtOi6ENtfl2bRhB0GSv8yNNZ/MbK+yA3nPzwKWgaPiMCb8Bz3n5R42r+C7rsUqU7XkDmxzbp/pWUUMsvn2OiaZHPLkAxNCrEYqHEkUyMRRrOFamI+SHbIKeef1B/NrQxNgxTXei6yvWmhd5WnCAPQCXMSXB/XqWEC5SL8eLegR7YqauGzEUcipllWPPPfUsqDIhuXN0O8Ox2tWh2nfXNdyC/GrQd4Eg==",
        "SigningCertURL": "https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-60eadc530605d63b8e62a523676ef735.pem",
        "UnsubscribeURL": "https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:206719415840:dev-eco-topic:ccb12801-4749-44a3-b36e-6474483e474e",
        "MessageAttributes": {
            "system_tenant_id": {"Type": "String", "Value": "jcci"},
            "system_id": {"Type": "String", "Value": "jcci"},
            "env": {"Type": "String", "Value": "dev"},
            "topic_type": {"Type": "String", "Value": "report"},
        },
    },
    "md5_of_body": "52f2de54dceec0db02a86f7448babb96",
    "message_attributes": {},
    "message_id": "cf8522ee-3c9a-4f5f-ad0f-e10317de13d5",
    "queue_url": "https://sqs.ap-northeast-1.amazonaws.com/206719415840/dev-eco-report-queue",
    "raw_event": "[SENSITIVE]",
    "receipt_handle": "AQEB0KEx9V0kO48mDnmGAzzCLa79GkN+fz9UEZpfclpoMbjHIcpIDrbnJj1QFl3uf7MdJejgt5VZQbhFlo5v927af2PAq2B2w3WLPnrmr4kPtiZE+FuMZTZTG2E+wm5A0UGkz9eWqb0fNvvvKKWQAobi9FxiQHiylQMSeMNaQe1whID35EiisZ+qf2KcUVj2GM585YI/EZC8AYvsicissXoKr2mLJco7stQ3ZhsizfjCovgrr2AzX5Z2sBDShz3/omPPui9trvfiuzrwsD70KQKjmgWQfGHNZ9n2lWjs8rXuDgOoRW8CJi2lejJdyKfNe3z/v8wSv3n+dxGn+KOgASsPo4wqr3Jc2iQ9Otmd9DPrk0/nzaYMcR0BoG8qxU2wrjMY5cxuLPXbQXDO9uyg529wWoOZHV657SFz+TUu7CmMvJs=",
}

# /home/pionero/Desktop/Workspace/jcci/jcci_eco_api_v2/handlers/v2/report/report_task/report_task_app.py
# record_handler:27
payload = record.get("body")
# {
#     "Type": "Notification",
#     "MessageId": "29e6e841-264c-52e5-a679-b6fca6e03576",
#     "TopicArn": "arn:aws:sns:ap-northeast-1:206719415840:dev-eco-topic",
#     "Message": {
#         "file_storage_id": 11769,
#         "cci_code": 8888,
#         "user_id": "murakami",
#         "file_type": "TradeRegistrationMaskedPassword",
#         "file_type2": "null",
#         "trade_company_code": "8888000008",
#         "code1": "8888000008",
#         "code2": "7c0716f84a3f18d4756ea044af92e5c9",
#         "topic_type": "report",
#     },
#     "Timestamp": "2024-05-14T15:08:28.718Z",
#     "SignatureVersion": "1",
#     "Signature": "FsnFYex4XTbCR2iGGrwwwu/Q8fLjF126RhOEwUNcdxMZVpuW2Gvb/XKIO32/HGzek+FvkUKTtsCIMXaHcaEqngISmYETfiGHeaH+jhJpKCNWhx4KGtC1VJHTtOi6ENtfl2bRhB0GSv8yNNZ/MbK+yA3nPzwKWgaPiMCb8Bz3n5R42r+C7rsUqU7XkDmxzbp/pWUUMsvn2OiaZHPLkAxNCrEYqHEkUyMRRrOFamI+SHbIKeef1B/NrQxNgxTXei6yvWmhd5WnCAPQCXMSXB/XqWEC5SL8eLegR7YqauGzEUcipllWPPPfUsqDIhuXN0O8Ox2tWh2nfXNdyC/GrQd4Eg==",
#     "SigningCertURL": "https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-60eadc530605d63b8e62a523676ef735.pem",
#     "UnsubscribeURL": "https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:206719415840:dev-eco-topic:ccb12801-4749-44a3-b36e-6474483e474e",
#     "MessageAttributes": {
#         "system_tenant_id": {"Type": "String", "Value": "jcci"},
#         "system_id": {"Type": "String", "Value": "jcci"},
#         "env": {"Type": "String", "Value": "dev"},
#         "topic_type": {"Type": "String", "Value": "report"},
#     },
# }
# record_handler:29
item = payload

# record_handler:33
message = item.get("Message", "")
# {
#     "file_storage_id": 11769,
#     "cci_code": 8888,
#     "user_id": "murakami",
#     "file_type": "TradeRegistrationMaskedPassword",
#     "file_type2": "null",
#     "trade_company_code": "8888000008",
#     "code1": "8888000008",
#     "code2": "7c0716f84a3f18d4756ea044af92e5c9",
#     "topic_type": "report",
# }

# record_handler:34
locale = message.get("locale", "ja")
# default ja

# record_handler:41
file_storage_id = message.get("file_storage_id")
# record_handler:42
force = message.get("force", False)

# report_task:77
file_storage = {
    "file_type": "TradeRegistrationMaskedPassword",
    "file_name": "",
    "latest_ip_address": "217.178.36.252",
    "file_type2": "null",
    "generation_info": "null",
    "latest_user_id": "murakami",
    "code1": "8888000008",
    "generation_start_date": "2024-05-15 00:08:28.543000",
    "created_at": "2024-05-15 00:08:28.583000",
    "cci_code": 8888,
    "code2": "7c0716f84a3f18d4756ea044af92e5c9",
    "generation_end_date": "null",
    "updated_at": "2024-05-15 00:08:31.837000",
    "id": 11769,
    "code3": "null",
    "file_info": "null",
    "trade_company_code": 8888000008,
    "document_code": "",
    "retry_count": 2,
    "user_id": "murakami",
    "file_date": "null",
    "is_deleted": False,
    "file_path": "",
}

# report_task:79
file_type = file_storage.get(
    "file_type"
)  # FILE_TYPE_TRADE_REGISTRATION_MASKED_PASSWORD=TradeRegistrationMaskedPassword

# /home/pionero/Desktop/Workspace/jcci/jcci_eco_api_v2/libraries/python/report_common.py
# generate_trade_registration_with_file_storage:3107,3108
cci_code = file_storage.get("cci_code")
trade_company_code = file_storage.get("trade_company_code")

# generate_trade_registration_with_file_storage:3111,3112,3113
code1 = file_storage.get("code1")
code2 = file_storage.get("code2")
file_type = file_storage.get("file_type")

# generate_trade_registration_with_file_storage:3115-3118
s3_path = get_trade_registration_pdf_s3_path(
    cci_code, trade_company_code, code1, code2, file_type
)
file_name = "貿易登録証_{}_{}.pdf".format(trade_company_code, code2)
pdf_title = "貿易登録証"
template_file_name = "trade_registration.xlsx"

print(
    json.dumps(
        {
            "id": file_storage_id,
            "cciCode": message.get("cci_code"),
            "companyCode": message.get(
                'trade_company_code', message.get('transaction_code')
            ),
            "content": {"status": "ReportCommon.STATUS_STARTED"},
        }
    )
)
