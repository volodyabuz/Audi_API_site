import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379

with redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0) as client:
    while True:
        problem = input(":::")
        client.lpush('problems', problem)

        answer = client.brpop('answers')[1].decode('utf-8')
        print(f"Answer: {answer}")
