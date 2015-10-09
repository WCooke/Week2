      File: test.sh                                    

echo "CPU/Mem INFO"


sed '2q;d' /proc/cpuinfo
sed '5q;d' /proc/cpuinfo
sed '1q;d' /proc/meminfo
sed '7q;d' /proc/stat
