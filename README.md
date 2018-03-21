# timekeeper
Log time when you arrived to work, went for lunch, leave work, ...

## Usage

```
usage: log_in.py [-h] [--action {in,out,lunch}]

optional arguments:
  -h, --help            show this help message and exit
  --action {in,out,lunch}
```
  
  
- Log in --> arrive to work
```
log_in.py --action in
```


- Log out --> leave work
```
log_in.py --action out
```


- Lunch --> leave for lunch
```
log_in.py --action lunch
```

___

## Known issues

- The output csv file has no dates, thus it is difficult to know how much you have worked each day, if you took some days off (or if you do not work everyday = even weekends)
