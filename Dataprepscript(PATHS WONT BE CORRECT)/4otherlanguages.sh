#!/bin/bash
r=3
set -o noclobber

mkdir task3
rm task3/*
for lang in "xhosa" "plautdietsch" "middle-english" "hiligaynon"
do
java -jar negsel2.jar -self english.train -n 10 -r "$r" -c -l < "lang/${lang}.txt" >| "task3/english_train_${lang}_test_r_$r"
done
java -jar negsel2.jar -self english.train -n 10 -r "$r" -c -l < english.test >| "task3/english_train_english_test_r_$r"
