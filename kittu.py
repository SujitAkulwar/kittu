import argparse
import psutil
import time
import sys
import csv
import os

def record_stats(print_output, time_interval, time_period, file_name):
    iterations = (time_period * 60) // time_interval 
    print(f"Total Iterations: {iterations}")

    title = [
        "Index", "CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)",
        "Bytes Sent", "Bytes Received", "Battery Percentage"
    ]

    file = None
    if file_name is not None:
        if not file_name.lower().endswith('.csv'):
            file_name += '.csv'
        if os.path.exists(file_name):
            raise FileExistsError(f"The file '{file_name}' already exists.")

        try:
            file = open(file_name, 'w', newline='')
            csv_writer = csv.writer(file)
            csv_writer.writerow(title)
        except IOError as e:
            print(f"Error opening file {file_name}: {e}")
            sys.exit(1)

    if print_output:
        print(title)

    try:
        for i in range(iterations):
            try:
                cpu_usage = psutil.cpu_percent(interval=None)
                time.sleep(time_interval) 

                memory_info = psutil.virtual_memory()
                disk_usage = psutil.disk_usage('/')
                network_info = psutil.net_io_counters()
                sensors_battery = psutil.sensors_battery()

                battery_percentage = "N/A" if sensors_battery is None else f"{sensors_battery.percent}%"

                stats = [
                    i + 1,  
                    cpu_usage,
                    memory_info.percent,
                    disk_usage.percent,
                    network_info.bytes_sent,
                    network_info.bytes_recv,
                    battery_percentage
                ]

                if print_output:
                    print(stats)

                if file:
                    try:
                        csv_writer.writerow(stats)
                    except IOError as e:
                        print(f"Error writing to file {file_name}: {e}")
                        sys.exit(0)
                    except KeyboardInterrupt:
                        print("\nRecording stopped by user.")
                        sys.exit(0)
            except KeyboardInterrupt:
                print("\nRecording stopped by user.")
                sys.exit(0)
    finally:
        if file:
            file.close()


def main():
    parser = argparse.ArgumentParser(description="PC Stats Recorder")

    parser.add_argument('-np', '--no_print', action='store_true',
                        help='Suppress output to the command prompt. If this flag is set, the stats will not be printed to the console.')
    parser.add_argument('-i', '--time_interval', type=int, default=1,
                        help='Interval in seconds between each recording of computer stats. Default is 1 second.')
    parser.add_argument('-t', '--time_period', type=int, default=1,
                        help='Duration in minutes for recording stats. The program will record data for this period. Default is 1 minute.')
    parser.add_argument('-s', '--save', type=str, default=None,
                        help='Path to the file where the recorded stats will be saved. If not specified, data will not be saved to a file.')

    args = parser.parse_args()

    print("Initializing...")

    try:
        record_stats(not args.no_print, args.time_interval, args.time_period, args.file_name)
    except KeyboardInterrupt:
        print("\nRecording stopped by user.")
        sys.exit(0)


if __name__ == '__main__':
    main()