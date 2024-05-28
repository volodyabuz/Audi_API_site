import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379

with redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0) as client:
    while True:
        problem = client.brpop('problems')[1].decode('utf-8')
        answer = eval(problem)

        client.lpush('answers', answer)