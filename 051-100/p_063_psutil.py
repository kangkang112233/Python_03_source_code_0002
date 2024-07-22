import psutil

# CPU時間を求める
cpu_times = psutil.cpu_times()
print(cpu_times)

# 特定のCPU時間ごとの使用率を求める
for i in range(3):
    cpu_times_percent = psutil.cpu_times_percent(interval=1, percpu=False)
    print(cpu_times_percent)

# メモリの使用率に関する統計情報を求める
virtual_memory = psutil.virtual_memory()
print(virtual_memory)

# マウントしているディスクパーティション情報を取得する
disk_partitions = psutil.disk_partitions()
print(disk_partitions)

# ネットワークI/Oに関する統計情報を求める
net_io_counters = psutil.net_io_counters()
print(net_io_counters)
