from flask import Flask, render_template, jsonify
import requests
import time
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def ping_urls():
    urls = read_urls_from_file('urls.txt')

    results = []

    for url in urls:
        start_time = time.time()
        try:
            response = requests.get(url)
            response_time = time.time() - start_time
            if response_time > 0:
                response_time = 'X'
            results.append({'url': url, 'response_time': response_time})
        except requests.exceptions.RequestException:
            results.append({'url': url, 'response_time': None})

    return render_template('output.html', results=results)


def count_lines(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def read_urls(some_file, number, result):
    i = 0
    with open(some_file, 'r') as f:
        while i < number:
            value = f.readline()
            value = value.replace('\n', '')
            result.append(value)
            i += 1
    return result


def read_urls_from_file(some_file):
    address = []
    lines = count_lines(some_file)
    address = read_urls(some_file, lines, address)
    return address


def plot():
    # Generate or load data for plotting
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Create a plot using Matplotlib
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot')

    # Save the plot to a temporary file
    plot_file = '/tmp/plot.png'
    plt.savefig(plot_file)

    # Render the template with the plot
    return render_template('output.html', plt=plot_file)


if __name__ == '__main__':
    app.run()

