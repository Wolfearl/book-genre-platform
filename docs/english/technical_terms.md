
| English Term | Перевод              | Контекст использования                  |
|--------------|----------------------|-----------------------------------------|
| framework    | фреймворк            | Django is a web <span style="color:yellow;">**framework**</span> |
| bootstrap    | начальная загрузка   | Run the following command to <span style="color:yellow;">**bootstrap**</span>  |
| built-in     | встроенный           | You’ll need to avoid naming projects after <span style="color:yellow;">**built-in**</span> Python or Django components|
| compatible   | совместимый          | ASGI-<span style="color:yellow;">**compatible**</span> web servers |
| boilerplate  | шаблонный код        | The command creates <span style="color:yellow;">**boilerplate**</span> code |
| deployment   | развертывание        | Ready for <span style="color:yellow;">**deployment**</span>                    |
| middleware   | промежуточное ПО     | <span style="color:yellow;">**Middleware**</span> for processing requests |
| perform      | выполнять            | <span style="color:yellow;">**Performing**</span> system checks |
| reference    | ссылка               | The include() function allows <span style="color:yellow;">**referencing**</span> other URLconfs |
| plug-and-play| подключи и играй     | To make it easy to <span style="color:yellow;">**plug-and-play**</span> URLs |
| pre-built    | предварительно построенный | Which is a <span style="color:yellow;">**pre-built**</span> URLconf |
| respond      | откликнуться         | It will <span style="color:yellow;">**respond**</span> with a JSON |
| query string   | строка запроса     | Parameter in the <span style="color:yellow;">**query string**</span> |
| overrides     | переопределяет      | Parameter value <span style="color:yellow;">**overrides**</span> the default value |
| fork          | развилка / загрузка | <span style="color:yellow;">**Fork**</span> the project from Github |
|  marshal instances | преобразование экземпляров | To automatically <span style="color:yellow;">**marshal instances**</span> |
| implementation     | реализация     | The <span style="color:yellow;">**implementation**</span> of the method |
| executable         | исполняемый    | Build an <span style="color:yellow;">**executable** </span> JAR |

<br>

---

<br>

| Django Term | Spring Boot Equivalent | Комментарии |
|-------------|------------------------| ------------|
| View        | Controller             |В Django "View" отвечает за обработку запроса и возврат ответа, а в Spring Boot роль этой части выполняет "Controller" |
| Model       | Entity                 | Django Model определяет структуру данных и бизнес-логику, аналогично Entity в Spring, которая отображает таблицу в базе данных |
| URL pattern | Request Mapping        | Django URL pattern - это правило маршрутизации в urls.py, аналог request mapping в Spring (аннотация @RequestMapping) |
| Migration   | Schema update          | Миграции Django - это управление изменениями схемы базы данных, в Spring Boot аналогом будет обновление схемы через Liquibase, Flyway или ручные скрипты. Термин "schema update" — общий |
| Serializer  | Jackson JSON           | Serializer в Django (DRF) отвечает за преобразование объектов в JSON и обратно, в Spring Boot Jackson — популярная библиотека для JSON-сериализации |