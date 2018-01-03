import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from collections import defaultdict

# plt.plot(np.arange(10))
# plt.show()

path = 'E:/personal/Python/data1/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

# records = open(path).readline()
records = [json.loads(line) for line in open(path)]
print(records)
print(records[0])

timezones = [rec['tz'] for rec in records if 'tz' in rec]
print(timezones)

def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(timezones)
print(counts['America/New_York'])