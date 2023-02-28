#!/bin/bash

#SMALL TESTS
dir="syscalls/negselresults/small"
mkdir -p $dir
rm $dir/*
set -o noclobber

for n in {3..7}; do
for ((r = 1 ; 2 <= n-r ; r++)); do
echo "generating size=small n=${n} r=${r}"
#snd_cert
java -jar negsel2.jar -self syscalls/snd-cert/small/small.train -n "$n" -r "$r" -c -l -k  < syscalls/snd-cert/small/small.tests >| "${dir}/cert_n_${n}_r_${r}"
# snd-unm
java -jar negsel2.jar -self syscalls/snd-unm/small/small.train -n "$n" -r "$r" -c -l -k < syscalls/snd-unm/small/small.tests >| "${dir}/unm_n_${n}_r_${r}"
done
done

# LARGE tests
dir="syscalls/negselresults/large"
mkdir -p $dir
rm $dir/*
set -o noclobber

for n in 15 20 25 30; do
for ((r = 1 ; 1 <= n-r ; r+=4)); do
echo "generating size=large n=${n} r=${r}"
#snd_cert
java -jar negsel2.jar -self syscalls/snd-cert/large/large.train -n "$n" -r "$r" -c -l -k  < syscalls/snd-cert/large/large.tests >| "${dir}/cert_n_${n}_r_${r}"
# snd-unm
java -jar negsel2.jar -self syscalls/snd-unm/large/large.train -n "$n" -r "$r" -c -l -k < syscalls/snd-unm/large/large.tests >| "${dir}/unm_n_${n}_r_${r}"
done
done