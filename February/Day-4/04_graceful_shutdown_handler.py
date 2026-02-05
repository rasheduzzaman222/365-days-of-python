import signal
import time

running = True

def shutdown_handler(signum, frame):
    global running
    print("Shutdown signal received")
    running = False


signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

if __name__ == "__main__":
    while running:
        print("Running...")
        time.sleep(1)

    print("Clean shutdown completed")
