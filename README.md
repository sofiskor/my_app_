Имеется плата (тестер), реализующая функционал загрузки прошивки в сторонний микроконтроллер. 
Для данной платы необходима возможность обновления загружаемой в этот микроконтроллер прошивки, 
которая содержится в памяти тестера, для чего будет использоваться подключение тестера к ПК через VCP (virtual com port).
Для данной цели было разработано приложение, предназначенное для передачи прошивки микроконтроллера 
с персонального компьютера на целевое устройство через виртуальный последовательный порт с использованием библиотеки PyQT.