from flask import Flask, render_template, request

app = Flask(__name__)

def rabin_karp(text, pattern):
    pattern_indices = []
    steps = []

    prime = 101
    d = 256
    pattern_length = len(pattern)
    text_length = len(text)
    h = pow(d, pattern_length - 1, prime)

    pattern_hash = sum(ord(pattern[i]) * pow(d, pattern_length - 1 - i, prime) for i in range(pattern_length)) % prime
    text_hash = sum(ord(text[i]) * pow(d, pattern_length - 1 - i, prime) for i in range(pattern_length)) % prime

    for i in range(text_length - pattern_length + 1):
        window = text[i:i+pattern_length]
        steps.append(list(window))
        if pattern_hash == text_hash and window == pattern:
            pattern_indices.append(i)

        if i < text_length - pattern_length:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % prime
            text_hash = (text_hash + prime) % prime

    return pattern_indices, steps

@app.route('/', methods=['GET', 'POST'])
def index():
    pattern_indices = []
    steps = []

    if request.method == 'POST':
        text = request.form['text']
        pattern = request.form['pattern']
        pattern_indices, steps = rabin_karp(text, pattern)

    return render_template('index.html', pattern_indices=pattern_indices, steps=steps)  

if __name__ == '__main__':
    app.run(debug=True)
