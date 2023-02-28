#!/bin/bash
dir="syscalls/negselresults"
mkdir -p $dir
# rm $dir/*
set -o noclobber


for n in {4..7}; do
for ((r = 0 ; 2 <= n-r ; r++)); do
#snd_cert
java -jar negsel2.jar -self syscalls/snd-cert/snd-cert.train -n "$n" -r "$r" -c -l -k  < syscalls/snd-cert/all.tests >| "${dir}/cert_n_${n}_r_${r}"
# snd-unm
java -jar negsel2.jar -self syscalls/snd-unm/snd-unm.train -n "$n" -r "$r" -c -l -k < syscalls/snd-unm/all.tests >| "${dir}/unm_n_${n}_r_${r}"
done
done