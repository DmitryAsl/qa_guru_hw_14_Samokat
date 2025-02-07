<h2 align="center"> Тестовый проект UI автотестов на сайт samokat.ru</h2>  


### Используемый стек
<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" height=50 weight=50 />  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" height=50 weight=50 />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height=50 weight=50 />
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/selenoid.svg" height=50 weight=50 />
  <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height=50 weight=50 />
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/Telegram.svg" height=50 weight=50 />
</p>        

### Автоматизированные кейсы
1. Выбор адреса доставки
2. Поиск товара
3. Поиск несуществующего товара
4. Добавление товара в корзину
5. Удаление товара из корзины
6. Корректность расчета стоимости корзины

<details>
<summary><h3> Запуск тестов с помощью Jenkins </h3></summary>

  > **Перейти в [сборку](https://jenkins.autotests.cloud/job/C17_dmitry_asl_hw14_Samokat/)**  
  > **Перейти на вкладку "Build with Parameters"** 
  <p>
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/jenkins.jpg" />
  </p>  
  
  > **Выбрать параметры из выпадающих список и нажать "Build"**
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/build_jenkins.jpg" />
  
  > dfsd
</details>

<details>
<summary><h3> Запуск тестов локально </h3></summary>  
  В терминале выполнить команду
  
  ```
  pytest tests --browser='chrome' --browser_version='126.0'
  ```

  > **--browser** - браузер в котором запустят тесты (доступен еще firefox)  
  > **--browser_version** - версия запускаемого браузера  
</details>
