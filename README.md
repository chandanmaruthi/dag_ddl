# Directed Acyclic Graph test

Pre_requisite:
create an python 3 environment
```
virtualenv --python=/usr/bin/python3.6 env
source env/bin/activate
```

Run the script
```
 python dag_run.py 

```

Enter Input Values

```
7 
0,1 
0,2 
1,3 
1,5 
2,5 
6,2 

```

# Note on Missing Items
The following improvements can be done to the code [ not done in the interest of time ]
- Unit Tests
- Read from File
- Remove/reduce cyclomatic complexity using better data structures
- Storage