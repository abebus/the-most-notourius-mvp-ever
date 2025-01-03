# Vision Document for MVP

## 1. Заголовок
- **Название проекта**: PricePredictor
- **Версия документа**: 0.1
- **Дата создания**: 06.12.2024
- **Автор(ы)**: Намаев Альберт

---

## 2. Краткое резюме
- **Проблема**: Покупатели и продавцы квартир не имеют точного понимания текущей рыночной стоимости недвижимости, что приводит к неправильным решениям и потерям денег.  
- **Решение**: Прогнозирующий алгоритм, предоставляющий точные оценки рыночной цены квартиры на основе данных рынка недвижимости.  
- **Целевая аудитория**: Покупатели, продавцы и агентства недвижимости.  
- **Ценность**: Упрощение процесса оценки стоимости, экономия времени и снижение рисков переплаты или недооценки объекта.

---

## 3. Формулировка проблемы
- **Проблема**: На текущем рынке недвижимости большинство оценок стоимости квартир субъективны, требуют участия экспертов или основываются на устаревших данных. Это приводит к затягиванию сделок, финансовым потерям и недоверию между сторонами.  
- **Влияние**: Пользователи сталкиваются с неоправданными затратами на услуги оценщиков и с высоким риском неверной оценки.  
- **Существующие решения**: Ручные экспертные оценки, онлайн-калькуляторы с низкой точностью, основанные на ограниченных данных.

---

## 4. Описание решения
- **Как работает продукт**: Пользователь передаёт решению параметры квартиры (локация, площадь, количество комнат, состояние и т. д.), а алгоритм на основе больших данных и методов машинного обучения предсказывает актуальную рыночную цену.
- **Ключевые особенности**:  
  - Автоматизированный расчет стоимости.  
  - Прогноз на основе исторических данных и рыночных трендов.  
  - Визуализация факторов, влияющих на стоимость (расположение, инфраструктура, состояние рынка).  
- **Диаграмки**: [C4 (C3) as pdf](.static/Flats.pdf), [Direct Miro link](https://miro.com/app/board/uXjVL81exeg=/?share_link_id=400599468592)


---

## 5. Цели и задачи MVP
- **Основная цель**: Проверить гипотезу, что автоматическое прогнозирование цены квартиры будет востребовано среди пользователей.  
- **Краткосрочные цели**:  
  - Собрать базу данных и обучить минимально жизнеспособную модель прогнозирования.  
  - Запустить интерфейс для тестирования пользователей.  
- **Долгосрочные цели**:  
  - Увеличить точность модели до уровня профессиональных оценщиков.  
  - Внедрить продукт в рабочие процессы агентств недвижимости.
  - Предложить решение платформам объявлений, договориться об интеграции.

---

## 6. Целевая аудитория
- **Основные сегменты пользователей**:  
  - Частные лица, продающие или покупающие недвижимость.  
  - Риелторы, нуждающиеся в быстрой оценке объектов.  
  - Аналитические компании и банки, выдающие ипотечные кредиты.  
- **Их проблемы**:  
  - Отсутствие объективной оценки рыночной цены.  
  - Высокие затраты на традиционную оценку.

---

## 7. Основные функции MVP
- **Функции, которые будут реализованы**:  
  - Ввод базовых параметров квартиры.  
  - Предсказание цены на основе обученной модели.  
  - Вывод отчета с указанием ключевых факторов, влияющих на цену.  
- **Что исключено**: Анализ редких параметров (например, элитные квартиры) и поддержка всех регионов на этапе MVP.

---

## 8. Метрики успеха
- **Показатели для оценки MVP**:  
  - Точность модели (`R²`, `MAE`, `MSE`, etc.).  
  - Количество активных пользователей.  
  - Доля пользователей, готовых рекомендовать продукт (NPS).

---

## 9. Анализ конкурентов
- **Конкуренты**:  
  - Онлайн-калькуляторы стоимости ([Циан](https://www.cian.ru/kalkulator-nedvizhimosti/), [Домклик](https://price.domclick.ru/), [IRN](https://www.irn.ru/price/), [Дом.рф](https://спроси.дом.рф/services/ocenka-nedvizhimosti/)).  
  - Услуги профессиональных оценщиков.  
- **Наше преимущество**:
    - Агрегация данных со всех доступных платформ о продаже недвижимости. 
    - Дополнительный функционал (Уведомления по выставленным фильтрам).

---

## 10. Дорожная карта и сроки
- **Этапы реализации**:  
  - Этап 1: Сбор и обработка данных (сроки: ?).  
  - Этап 2: Разработка базовой модели прогнозирования (сроки: ?).  
  - Этап 3: Создание пользовательского интерфейса (сроки: ?).  
  - Этап 4: Тестирование и сбор обратной связи (сроки: ?).  

---

## 11. Риски и предположения
- **Основные риски**:  
  - Недостаточное количество данных для обучения модели.  
  - Низкая точность предсказаний на начальном этапе.  
- **Предположения**:  
  - Пользователи готовы использовать автоматизированные решения вместо традиционных методов оценки.

---

## 12. Призыв к действию
- **Что требуется**:  
  - Утвердить концепцию MVP.  
  - Определить ресурсы для сбора данных и разработки.  
  - Начать работу над продуктом для тестирования в реальных условиях.

