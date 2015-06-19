# Activación del servicio SSH en el Raspberry Pi

***1. Instalar ssh***
``` 
sudo apt-get install ssh
```

***2. iniciar el servicio con el siguiente comando:***
```
sudo /etc/init.d/ssh start
```

***3. ejecutar automáticamente al iniciar el Raspberry Pi, ingrese el siguiente código:***
```
sudo update-rc.d ssh defaults
```

***4. conectarse por ip al Raspberry Pi por ssh***
```
ssh usuario@ip
```
