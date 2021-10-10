import requests
import line_notify.setting

line_api = setting.line_api

def main(comment=[]):
    send_line_notify(comment)

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = Line_API
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f' {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()
