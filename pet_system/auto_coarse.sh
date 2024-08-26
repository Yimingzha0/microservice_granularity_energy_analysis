#!/bin/bash

iterations=10
#duration between each iteration
delay=20
script_path_1="./coarse_script/burst_high.py"
script_path_2="./coarse_script/burst_med.py"
script_path_3="./coarse_script/burst_low.py"
script_path_4="./coarse_script/even_high.py"
script_path_5="./coarse_script/even_med.py"
script_path_6="./coarse_script/even_low.py"
users=400
rate=40
users_low=10
rate_low=5
runtime_burst="10s"
reset_time=110
runtime_even="120s"

printf "Burst high groups begins...\n"

sleep 1600

for ((i=1; i<=iterations; i++))
do
    echo "Running iteration $i..."
    echo "Parameters: pacing=$pacing, users=$users, rate=$rate, runtime=$runtime_burst, iteration=$i"
    python $script_path_1 -u $users -r $rate --run-time $runtime_burst --iteration $i &
    python $script_path_1 -u $users -r $rate --run-time $runtime_burst --iteration $i &
    sleep 10
    sleep $reset_time
    if [ $i -lt $iterations ]; then
        echo "Waiting for $delay seconds..."
        sleep $delay
    fi
done

sleep 20
printf "Burst medium groups begins...\n"
for ((i=1; i<=iterations; i++))
do
    echo "Running iteration $i..."
    echo "Parameters: pacing=$pacing, users=$users, rate=$rate, runtime=$runtime_burst, iteration=$i"
    python $script_path_2 -u $users -r $rate --run-time $runtime_burst --iteration $i &
    sleep 10
    sleep $reset_time
    if [ $i -lt $iterations ]; then
        echo "Waiting for $delay seconds..."
        sleep $delay
    fi
done

sleep 20
printf "Burst low groups begins...\n"
for ((i=1; i<=iterations; i++))
do
    echo "Running iteration $i..."
    echo "Parameters: pacing=$pacing, users=$users, rate=$rate, runtime=$runtime_burst, iteration=$i"
    python $script_path_3 -u $users -r $rate --run-time $runtime_burst --iteration $i &
    sleep 10
    sleep $reset_time
    if [ $i -lt $iterations ]; then
        echo "Waiting for $delay seconds..."
        sleep $delay
    fi
done

sleep 20
printf "Even high groups begins...\n"
for ((i=1; i<=iterations; i++))
do
    echo "Running iteration $i..."
    echo "Parameters: pacing=$pacing, users=$users, rate=$rate, runtime=$runtime_even, iteration=$i"
    python $script_path_4 -u $users -r $rate --run-time $runtime_even --iteration $i &
    sleep 120
    if [ $i -lt $iterations ]; then
        echo "Waiting for $delay seconds..."
        sleep $delay
    fi
done

sleep 20
printf "Even medium groups begins...\n"
for ((i=1; i<=iterations; i++))
do
    echo "Running iteration $i..."
    echo "Parameters: pacing=$pacing, users=$users, rate=$rate, runtime=$runtime_even, iteration=$i"
    python $script_path_5 -u $users -r $rate --run-time $runtime_even --iteration $i &
    sleep 120
    if [ $i -lt $iterations ]; then
        echo "Waiting for $delay seconds..."
        sleep $delay
    fi
done

sleep 20
printf "Even low groups begins...\n"
for ((i=1; i<=iterations; i++))
do
    echo "Running iteration $i..."
    echo "Parameters: pacing=$pacing, users=$users, rate=$rate, runtime=$runtime_even, iteration=$i"
    python $script_path_6 -u $users_low -r $rate_low --run-time $runtime_even --iteration $i & sleep 120
    if [ $i -lt $iterations ]; then
        echo "Waiting for $delay seconds..."
        sleep $delay
    fi
done

echo "All iterations are done!"