# Kittu - PC Stats Recorder

**Kittu** is a command-line tool for recording various PC statistics such as CPU usage, memory usage, disk usage, network statistics, and battery percentage. The recorded data can be printed to the console or saved to a CSV file for further analysis.

**Kittu** was created to generate data for data analysis and other data science applications.

## Features

- Record CPU usage
- Record memory usage
- Record disk usage
- Record network statistics (bytes sent and received)
- Record battery percentage
- Option to print statistics to the console or save to a CSV file

## Installation

You can install **Kittu** using `pip`. Run the following command in your terminal:

```bash
pip install .
```

Make sure to run this command in the same directory as `setup.py` or specify the path to the directory containing `setup.py`.

## Usage

After installation, you can use the `kittu` command in your terminal. Here are the available options:

```bash
kittu [OPTIONS]
```

### Options

- `-np`, `--no_print`: Suppress output to the command prompt. If this flag is set, the stats will not be printed to the console.
- `-i`, `--time_interval`: Interval in seconds between each recording of computer stats. Default is 1 second.
- `-t`, `--time_period`: Duration in minutes for recording stats. The program will record data for this period. Default is 1 minute.
- `-s`, `--save`: Path to the file where the recorded stats will be saved. If not specified, data will not be saved to a file.

### Example

To record stats every 5 seconds for 10 minutes and print them to the console:

```bash
kittu -i 5 -t 10
```

To record stats every 5 seconds for 10 minutes and save them to `stats.csv`:

```bash
kittu -i 5 -t 10 -s stats.csv
```

## Contributing

If you want to contribute to **Kittu**, feel free to fork the repository and submit a pull request. Contributions are welcome!

## Author

Sujit Akulwar
[E-Mail](mailto:sujitakulwar@gmail.com)
