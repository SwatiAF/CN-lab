## Multiple Routers

1. connect PC0 with Router0 using copper cross-over cable - `fastethernet0/0`
2. connect Router0 to Router1 using Serial DCE with the connection named as `serial2/0`, then connect Router1 to Router2 using serial DCE named `serial3/0`
3. connect Router2 to PC1 using copper cross-over cable - `fastethernet1/0`
4. set the IP addresses, subnet mask (`255.0.0.0` for all PCs and routers) and gateways accordingly.

  a. PC0: 
    IP addr. = `10.0.0.1`
    gateway = `10.0.0.10`
    
  b. Router0:
    gateway1 = `10.0.0.10`
    gateway2 = `20.0.0.10`
    
  c. Router1: 
    gateway1 = `20.0.0.20`
    gateway2 = `30.0.0.10`
    
  d. Router2:
    gateway1 = `30.0.0.20`
    gateway2 = `40.0.0.10`
    
  e. PC1:
    IP addr. = `40.0.0.1`
    gateway = `40.0.0.10`
    
![image](https://user-images.githubusercontent.com/83855603/201946917-6e3235d3-c2bb-4321-877a-8b3d5241a0dc.png)
    
![image](https://user-images.githubusercontent.com/83855603/201749681-f13e42f1-74f0-4bd9-a056-1573f83e0d84.png)

6. for the Router0, the first gateway is set to IP address of `10.0.0.10` which is as same as gateway of PC0
7. then set up the connection between the 

  i. Router0 and the PC0 using the CLI. 
  
  ii. Router0 and Router1
  
  iii. Router1 and Router2
  
  iv. Router2 and PC1 using CLI
  
- CLI commands for Router0
  
![image](https://user-images.githubusercontent.com/83855603/201750259-c2f8d3df-14ea-4ee1-b14d-530545fdee37.png)

- CLI commands for Router1

![image](https://user-images.githubusercontent.com/83855603/201750443-d66aecd9-d7ce-459d-bdaa-a9cdb33388ad.png)

- CLI commands for Router2

![image](https://user-images.githubusercontent.com/83855603/201950094-4edb8ef1-d214-49c4-9883-aa0885f3b64d.png)
  
7. after all proper connections, the lights at all ends will be green indicating that the connection is established.

![image](https://user-images.githubusercontent.com/83855603/201951496-fecf8b5a-a7fe-4a25-9f2a-3313fc87f4ec.png)

8. Teaching the Router0 about the 30.0.0.0 and 40.0.0.0 networks

![image](https://user-images.githubusercontent.com/83855603/202365282-a9be57c7-d61b-4b62-90a7-a97adb9c84cc.png)

9. Teaching the Router1 about the 10.0.0.0 and 40.0.0.0 networks

![image](https://user-images.githubusercontent.com/83855603/202366235-f7924058-bd61-4368-856d-1483bcb2660d.png)

10. Teaching the Router2 about the 10.0.0.0 and 20.0.0.0 networks

![image](https://user-images.githubusercontent.com/83855603/202367073-70fe6ab2-e5e4-4cb2-bed5-5611e5e80a46.png)

 

