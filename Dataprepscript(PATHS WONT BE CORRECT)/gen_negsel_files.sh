#!/bin/bash
mkdir AUC
set -o noclobber

for i in {1..9}
do
java -jar negsel2.jar -self english.train -n 10 -r "$i" -c -l < english.test >| "AUC/english_train_english_test_r_$i"
java -jar negsel2.jar -self english.train -n 10 -r "$i" -c -l < tagalog.test >| "AUC/english_train_tatalog_test_r_$i"
done