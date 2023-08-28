def process_file(line):
    segments = []
    x, y, w, h = map(float, line)
    x_min = x - (w / 2)
    y_min = y - (h / 2)
    x_max = x + (w / 2)
    y_max = y + (h / 2)
    segment = [[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]]
    segments.append(segment)
    return segments

print(process_file([44,44,62,62]))