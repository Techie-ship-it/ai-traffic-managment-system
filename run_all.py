import threading
import subprocess

def run_vehicle_detection():
    subprocess.run(["python", "vehicle_detection.py"])

def run_simulation():
    subprocess.run(["python", "simulation.py"])

def run_signal_time():
    subprocess.run(["python", "signal_time.py"])

if __name__ == "__main__":
    # Create threads for each script
    t1 = threading.Thread(target=run_vehicle_detection)
    t2 = threading.Thread(target=run_simulation)
    t3 = threading.Thread(target=run_signal_time)

    # Start all threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()

    print("All scripts finished running.")
