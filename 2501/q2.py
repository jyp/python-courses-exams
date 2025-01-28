def histogram(max_bar, labels, counts):
    max_count = 0
    for l in labels:
        if max_count < counts[l]:
            max_count = counts[l]
    if max_count == 0:
        print("No meaningful data")
        return
    scale_factor = max_bar / max_count
    for l in labels:
        count = counts[l]
        bar_length = int(count * scale_factor)
        print(l.ljust(10) + bar_length * "*")

counts = {"pig": 19, "cat":57, "wolf":42, "horse":26}
labels = ["horse", "pig", "cat"]

histogram(20,labels,counts)
