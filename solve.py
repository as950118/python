import sys
import requests

Port = '1111'
Answer = heonjin
Input = sys.stdin.readline()
sys.stdin.readline('\n')
if Input == Answer:
    sys.stdout.write("Correct !\n")
    Data = {"Result":1}
    req = requests.post("http://14.49.39.164:" + Port, data = Data)
    return 1
else:
    sys.stdout.write("Faield ..\n")
    return 0

'''
<?php
while(1){
    if(isset($_POST['Result'])){
        break;
    }
};
?>
'''
