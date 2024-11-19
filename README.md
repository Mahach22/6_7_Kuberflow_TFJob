# 6_7_Kuberflow_TFJob

**Данный проект создан в рамках выполнения задания 1 урока 6.7.**

Условия задания:
1. Создайте Python-скрипт для обучения простой модели на наборе данных MNIST (любую берите, одежду/цифры).
2. Создайте Dockerfile для упаковки вашего скрипта в Docker-контейнер.
3. Соберите Docker-образ и загрузите его в Docker Hub или другой реестр контейнеров.
4. Создайте манифест для Kubeflow TFJob, который запустит обучение модели в Kubernetes.
5. Проверьте статус выполнения задания.
6. Убедитесь, что под завершился со статусом Completed и модель была успешно сохранена.
В качестве решения необходимо прислать ссылку на git репозиторий, в котором будет находится Docker файл, питон скрипт тренировки модели, а также yaml файл развертывания. В репозитории обязательно должнен быть скриншот со статусом completed. А также скриншот в котором видны эпохи вашей модели.
Брать код тренировки модели из LMS категорически запрещено. Можете использовать готовый код для обучения модели, но обертку для него сделайте самостоятельно.


**Процесс выполнения задания:**

1. Создаем [Python-скрипт для обучения модели на наборе данных MNIST](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/fashion_mnist_train.py) 
2. Создаем [dockerfile](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/dockerfile) для упаковки скрипта и необходимых зависимостей в контейнер
3. Собираем Docker-образ командой ```docker build -t mahach22/fashion-mnist-train:v2 .``` (с первой версией не сложилось, модель оказалось сложной для виртуальной машины)
![build](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/1.build.png)
Отправляем образ в докер хаб командой ```docker push mahach22/fashion-mnist-train:v2```
![push](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/2.docker_push.png)
4. Создаем [манифест](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/mnist-tfjob.yaml) для Kuberflow TFJob, который будет проводить обучение модели в Kubernetes командой ```kubectl apply -f mnist-tfjob.yaml```
5. Проверяем статус выполнения задания командой ```kubectl get pods```
![manifest](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/3.apply_manifest.png)
6. Задание завершилось со статусом Completed

![completed](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/4.completed.png)
8. Проверяем логи, чтобы увидеть эпохи командой ```kubectl logs mnist-worker-0```
![logs](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/5.logs.png)










