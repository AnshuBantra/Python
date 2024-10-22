#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 3 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;