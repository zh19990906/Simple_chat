import redis
import schedule
import time

def func():
    r = redis.Redis(host='localhost', port='6379', db='12', decode_responses=True, password='zhangheng0906')
    key_list = r.keys()
    # print(key_list)
    for key in key_list:
        r.delete(key)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print('++++++++++++++=================')

if __name__ == '__main__':
    schedule.every().day.at("00:00").do(func)
    while True:
        schedule.run_pending()  # 运行所有可以运行的任务
        time.sleep(1)



