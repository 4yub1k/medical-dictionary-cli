# medical-dictionary-cli
Dictionary Command Line tool: Based on MERRIAM-WEBSTER

#### Feature:
- Search for a simple or medical word in MERRIAM-WEBSTER.
- Write it to Database for future.
- Write it as json with extra fields.

### Setup:
```
pip install -r requirements.txt
```

### Help:
```
python3 dictionarycli.py --help
```

![image](https://github.com/4yub1k/medical-dictionary-cli/assets/45902447/0e29b66b-ab2a-41b5-80de-d74828f4b937)

### Search Online (Medical):
```
py dictionarycli.py search-online --word heart --type  medical
python3 dictionarycli.py search-online --word heart --type  medical
```
![image](https://github.com/4yub1k/medical-dictionary-cli/assets/45902447/817e0d4e-9abd-46a9-8431-c1c7ce23dfd7)

### Search Online (Normal):
```
py dictionarycli.py search-online --word heart
python3 dictionarycli.py search-online --word heart
```
![image](https://github.com/4yub1k/medical-dictionary-cli/assets/45902447/01b873ba-b83b-4e86-8445-27ce81960588)

### Search Local Database (SQlite):
```
py dictionarycli.py search-db --word firefly
```
![image](https://github.com/4yub1k/medical-dictionary-cli/assets/45902447/1882426d-3c4b-4117-b901-bd6f2fddc840)

### Search Files:
```
py dictionarycli.py search-json --word firefly 
```
![image](https://github.com/4yub1k/medical-dictionary-cli/assets/45902447/588c1502-f34c-41d8-b470-a71d47195adb)

