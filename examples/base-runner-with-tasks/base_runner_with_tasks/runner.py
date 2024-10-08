import time

from automato import AutomatoWithTasks

app = AutomatoWithTasks[str]()


@app.job
def job():
    job_result = "job_result"
    print(f"Job: {job_result}")
    app.to_consumer(job_result)


@app.task
def task(task: str):
    with app.lock:
        print("sleeping...")
        time.sleep(2)
        print(f"Task: {task}")


def main():
    app.start()


if __name__ == "__main__":
    main()
