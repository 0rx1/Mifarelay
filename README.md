# MIFA-RELAY
1. To reproduce the attack you simply run [pm3server.py](https://github.com/0rx1/Mifarelay/blob/main/pm3server.py "pm3server.py") to launch a local http server for capturing and saving the UIDs Received.
 ![](https://i.ibb.co/gMQQSK0/one.png)
 2. Run  [capture.py](https://github.com/0rx1/Mifarelay/blob/main/capture.py "capture.py") to prepare your proxmark3 to detect near cards & dump the UID
![](https://i.ibb.co/VMLfPpH/two.png)
2. While the data in being captured now you can run the final script [sim.py](https://github.com/0rx1/Mifarelay/blob/main/sim.py "sim.py") to pick which captured card you want to simulate via the second proxmark3
![](https://i.ibb.co/FzbjpZP/carbon-1.png)

**Happy Hacking**
