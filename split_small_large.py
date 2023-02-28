import os

perixes = ["unm", "cert"]
for pefix in perixes:
    make_dirs = [f"syscalls/snd-{pefix}/small/small.tests", f"syscalls/snd-{pefix}/small/small.labelss", f"syscalls/snd-{pefix}/large/large.tests", 
                 f"syscalls/snd-{pefix}/large/large.labelss", f"syscalls/snd-{pefix}/small/small.train", f"syscalls/snd-{pefix}/large/large.train"]
    [os.makedirs(os.path.dirname(file), exist_ok=True) for file in make_dirs]

    #write tests and labels to small and large files and open the initial files for reading
    with open(f"syscalls/snd-{pefix}/small/small.tests", 'w') as smalltests, open(f"syscalls/snd-{pefix}/small/small.labelss", 'w') as smalllabelss, \
    open(f"syscalls/snd-{pefix}/large/large.tests", 'w') as largetests, open(f"syscalls/snd-{pefix}/large/large.labelss", 'w') as largelabelss, \
    open(f"syscalls/snd-{pefix}/all.tests", 'r') as tests,open(f"syscalls/snd-{pefix}/all.labelss") as labelss:
        for line, label in zip(tests, labelss): 
            if len(line) < 31:
                smalltests.write(line)
                smalllabelss.write(label)
            else:
                largetests.write(line)
                largelabelss.write(label)

    #write train and labels to small and large files and open the initial files for reading
    with open(f"syscalls/snd-{pefix}/small/small.train", 'w') as smalltrain, \
    open(f"syscalls/snd-{pefix}/large/large.train", 'w') as largetrain, \
    open(f"syscalls/snd-{pefix}/snd-{pefix}.train", 'r') as trains:
        for line in trains:
            if len(line) < 31:
                smalltrain.write(line)
            else:
                largetrain.write(line)
