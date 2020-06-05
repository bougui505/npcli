# npcli
Feed stdin data to a numpy array (default variable name is `data`) and apply arbitrary numpy operation on it and print the result on stdout.
```
$ paste =(seq 10) =(seq 11 20) | ./np.sh 'print(data)'

1 11
2 12
3 13
4 14
5 15
6 16
7 17
8 18
9 19
10 20
```
```
$ paste =(seq 10) =(seq 11 20) | ./np.sh 'mu=data.mean(axis=0);print(mu)'

5.5
15.5
```
```
$ paste =(seq 10) =(seq 11 20) | np 'mu=data.mean(axis=1);print(mu)'

6
7
8
9
10
11
12
13
14
15
```
The python `print` command has been overwritten to print results as a shell friendly format
```
$ paste =(seq 10) =(seq 11 20) | np 'print(data.min());print(data.max())'

1.0
20.0
```
