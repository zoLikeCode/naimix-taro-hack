## Naimix: Code | MISIS GO

##### Наша команда разработала инновационную распределенную систему для прогнозирования и оптимизации подбора кандидатов с использованием Таро, применяя микросервисный подход для точной и персонализированной оценки.

### Демонстрация работы сервиса
------
1. #### [Ссылка на рабочий прототип](http://go.itatmisis.ru:80)
2. #### [Скринкаст работы сервиса](https://disk.yandex.ru/i/jbZzCyoUb1iwbw)
------
  
# Запуск проекта

Для начала работы с проектом выполните следующие шаги:

1. Склонируйте репозиторий на свой компьютер:
   ```bash
   git clone https://github.com/zoLikeCode/naimix-taro-hack

2. Создайте файл `.env` в директории [`ml_part/`](ml_part/). 

- Пример структуры файла можно найти в [`ml_part/.env.example`](ml_part/.env.example).

- Для получения необходимого ключа перейдите по данной [ссылке](https://habr.com/ru/articles/780008/), где подробно описан процесс его получения.

3. Запустите команду для сборки и запуска проекта в Docker:  
   ```bash
   docker-compose up --build

## Функциональность

### LLM
- В основе работы системы лежит библиотека `langchain`, выбранная за её гибкость, удобство использования и возможность интеграции с различными моделями, включая локально развёрнутые, если позволяют вычислительные ресурсы.
- **YandexGPT** была выбрана как одна из лучших LLM-моделей на рынке, благодаря высокой скорости работы, отличной гибкости в промптинге и минимальным галлюцинациям.

### Backend
- Микросервисная архитектура нашего решения позволяет легко и быстро интегрировать систему в другие проекты или сервисы, обеспечивая гибкость и масштабируемость.
- В качестве **системы управления базами данных** была выбрана **PostgreSQL**. Она была выбрана за высокую производительность, надежность, безопасность и возможности масштабирования, что позволяет системе выдерживать большие объемы запросов и обеспечивать стабильную работу при высоких нагрузках.

### Web
- Основным языком программирования был выбран **TypeScript**, благодаря его надёжности, статической типизации и удобству в разработке сложных веб-приложений.
- В качестве основного фреймворка используется **Next.js**, который обеспечивает высокую производительность, серверный рендеринг и отличную поддержку современных веб-стандартов. Это делает его идеальным выбором для создания масштабируемых и производительных веб-приложений.

## Технологии и инструменты
<img src="https://img.shields.io/badge/python-grey?style=for-the-badge&logo=python&logoColor=yellow"/> <img src="https://img.shields.io/badge/react-grey?style=for-the-badge&logo=react&logoColor=turquoise"/> <img src="https://img.shields.io/badge/YandexGPT-grey?style=for-the-badge"/> <img src="https://img.shields.io/badge/fastapi-grey?style=for-the-badge&logo=fastapi&logoColor=turquoise"/> <img src="https://img.shields.io/badge/postgresql-grey?style=for-the-badge&logo=postgresql&logoColor=turquoise"/> <img src="https://img.shields.io/badge/langchain-grey?style=for-the-badge&logo=langchain&logoColor=green"/> <img src="https://img.shields.io/badge/next.js-grey?style=for-the-badge&logo=next.js&logoColor=white"/> <img src="https://img.shields.io/badge/TypeScript-grey?style=for-the-badge&logo=TypeScript&logoColor=turquoise"/> <img src="https://img.shields.io/badge/chart.js-grey?style=for-the-badge&logo=chart.js&logoColor=yellow"/> <img src="https://img.shields.io/badge/docker-grey?style=for-the-badge&logo=docker&logoColor=turquoise"/>

## Команда проекта
- [Никита Зонтов](https://github.com/zoLikeCode) - капитан команды, backend и DE разработчик
- Светлана Шубина - project manager, разработчик дизайна
- [Максим Меркулов](https://github.com/spioncino) - frontend разработчик
- [Павел Шабуров](https://github.com/Shavelo) - ML-разработчик
- [Денис Басанский](https://github.com/Bigilittle) - ML-разработчик

## Архитектура

![alt text](image.png)

```plaintext
│   .gitignore
│   docker-compose.yml
│   image.png
│   readme.md
├───backend
│   │   .gitignore
│   │   database.py
│   │   Dockerfile
│   │   main.py
│   │   models.py
│   │   pdf_adapter.py
│   │   requirements.txt
│   ├───photo
│   ├───resumes
│   └───taro
├───frontend
│   │   .eslintrc.json
│   │   .gitignore
│   │   .prettierrc
│   │   bun.lockb
│   │   Dockerfile
│   │   next.config.ts
│   │   package.json
│   │   readme.md
│   │   tsconfig.json
│   ├───public
│   │       acceptIcon.tsx
│   │       avatar.jpg
│   │       backTaroCards.png
│   │       iconMenu.png
│   │       logo.png
│   │       SortArrow.tsx
│   │       taroCards.png
│   │       UpArrow.tsx
│   └───src
│       └───app
│           │   globals.css
│           │   icon.ico
│           │   index.ts
│           │   layout.tsx
│           │   not-found.tsx
│           │   page.module.css
│           │   page.tsx
│           │   store.ts
│           ├───candidates
│           │       page.module.css
│           │       page.tsx
│           ├───fonts
│           │   └───Graphik
│           ├───history
│           │       page.module.css
│           │       page.tsx
│           ├───lib
│           │       getAllProfiles.tsx
│           │       getProfile.tsx
│           │       getTaro.tsx
│           │       getTaroCards.tsx
│           │       getTaros.tsx
│           │       postCompetency.tsx
│           │       postTaroSpead.tsx
│           ├───ui
│           │   │   index.ts
│           │   ├───attrbText
│           │   │       attrbText.module.css
│           │   │       attrbText.tsx
│           │   │       attrRasklText.module.css
│           │   │       attrRasklText.tsx
│           │   ├───button
│           │   │       button.module.css
│           │   │       button.tsx│
│           │   ├───descriptionText
│           │   │       descriptionText.module.css
│           │   │       descriptionText.tsx
│           │   ├───employeeInfo
│           │   │       employeeInfo.module.css
│           │   │       employeeInfo.tsx
│           │   ├───filters
│           │   │       filters.module.css
│           │   │       filters.tsx
│           │   ├───popupFilter
│           │   │       popupFilter.module.css
│           │   │       popupFilter.tsx
│           │   ├───popupMenuNav
│           │   │       popupMenuNav.module.css
│           │   │       popupMenuNav.tsx
│           │   ├───radarCharts
│           │   │       radarCharts.tsx
│           │   ├───staffBlock
│           │   │       staffBlock.module.css
│           │   │       staffBlock.tsx
│           │   ├───taroCards
│           │   │       taroCards.module.css
│           │   │       taroCards.tsx
│           │   │
│           │   └───textAboutWorks
│           │           textAboutWorks.module.css
│           │           textAboutWorks.tsx
│           └───users
│               └───[id]
│                       page.module.css
│                       page.tsx
└───ml_part
    │   .dockerignore
    │   .env.example
    │   api.py
    │   Dockerfile
    │   readme.md
    │   requirements.txt
    │   server.py
    │   tarot.py    │
    └───prompts
            compatibility.txt
            competency_map.txt
            feedback.txt
            forecast.txt
            profile_extract.txt
            question.txt
            recommendations.txt
            rules.txt
            summ_rec.txt
            summ_tarot_full.txt
            tarot_description.txt
            tarot_one.txt
            tarot_spread.txt
            work_history_review.txt
```
---------
### Промежуточный итог
- Наш проект основан на использовании современных и проверенных технологий, обеспечивающих надёжность, масштабируемость и удобство. Благодаря библиотеке `langchain` и модели **YandexGPT**, система предоставляет точные и персонализированные рекомендации на основе карт Таро. 

- Микросервисная архитектура backend, поддерживаемая базой данных **PostgreSQL**, гарантирует гибкость и простоту интеграции, а также стабильную работу при высоких нагрузках. 

- Frontend, построенный на **TypeScript** и **Next.js**, обеспечивает высокую производительность, удобство использования и соответствие современным веб-стандартам. 

- Эта совокупность технологий делает наше решение инновационным, устойчивым и готовым к внедрению в реальные HR-процессы.
