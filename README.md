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


!(https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/dockerfile)

[build](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/1.build.png)


![push](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/2.docker_push.png)


![manifest](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/3.apply_manifest.png)


![completed](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/4.completed.png)


![logs](https://github.com/Mahach22/6_7_Kuberflow_TFJob/blob/main/5.logs.png)
