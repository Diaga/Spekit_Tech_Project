# Routes

### Assumptions & Constraints

- In absence of elastic search, it is assumed all searches will be made
  through [django-filter](https://django-filter.readthedocs.io/en/latest/index.html).
    - Routes with `Filter: Yes` support filtering.

## Document

### Create document

- **URL**: v1/document/
- **METHOD**: POST

#### Request

```json
{
  "title": "Spekit Help Document",
  "content": "This is the content for XX",
  "folder": "<uuid>"
}
```

#### Response

```json
{
  "id": "<uuid>",
  "title": "Spekit Help Document",
  "content": "This is the content for XX",
  "folder": "<uuid>"
}
```

### Retrieve documents

- **URL**: v1/document/
- **METHOD**: GET
- **FILTER**: Yes

#### Response

```json
[
  {
    "id": "<uuid>",
    "title": "Spekit Help Document",
    "content": "This is the content for XX",
    "folder": "<uuid>"
  }
]
```

### Retrieve document by id

- **URL**: v1/document/<:id>
- **METHOD**: GET

#### Response

```json
{
  "id": "<:id>",
  "title": "Spekit Help Document",
  "content": "This is the content for XX",
  "folder": "<uuid>"
}
```

### Update document

- **URL**: v1/document/<:id>/
- **METHOD**: PATCH

#### Request

```json
{
  "content": "This is new content for XX"
}
```

#### Response

```json
{
  "id": "<:id>",
  "title": "Spekit Help Document",
  "content": "This is new content for XX",
  "folder": "<uuid>"
}
```

### Delete document

- **URL**: v1/document/<:id>/
- **METHOD**: DELETE

#### Response

```json
{
  "id": "<:id>",
  "title": "Spekit Help Document",
  "content": "This is new content for XX",
  "folder": "<uuid>"
}
```

## Folder

### Create folder

- **URL**: v1/folder/
- **METHOD**: POST

#### Request

```json
{
  "name": "Help Folder",
  "folder": "<uuid>"
}
```

#### Response

```json
{
  "id": "<uuid>",
  "name": "Help Folder",
  "folder": "<uuid>"
}
```

### Retrieve folders

- **URL**: v1/folder/
- **METHOD**: GET
- **FILTER**: Yes

#### Response

```json
[
  {
    "id": "<uuid>",
    "name": "Help Folder",
    "folder": "<uuid>"
  }
]
```

### Retrieve folder by id

- **URL**: v1/folder/<:id>
- **METHOD**: GET

#### Response

```json
{
  "id": "<:id>",
  "name": "Help Folder",
  "folder": "<uuid>"
}
```

### Update folder

- **URL**: v1/folder/<:id>/
- **METHOD**: PATCH

#### Request

```json
{
  "name": "New Help Folder"
}
```

#### Response

```json
{
  "id": "<:id>",
  "name": "New Help Folder",
  "folder": "<uuid>"
}
```

### Delete folder

- **URL**: v1/folder/<:id>/
- **METHOD**: DELETE

#### Response

```json
{
  "id": "<:id>",
  "name": "Help Folder",
  "folder": "<uuid>"
}
```

## Topic

### Create topic

- **URL**: v1/topic/
- **METHOD**: POST

#### Request

```json
{
  "short_descriptor": "support",
  "long_descriptor": "support for developers"
}
```

#### Response

```json
{
  "id": "<uuid>",
  "short_descriptor": "support",
  "long_descriptor": "support for developers"
}
```

### Retrieve topics

- **URL**: v1/topic/
- **METHOD**: GET
- **FILTER**: Yes

#### Response

```json
[
  {
    "id": "<uuid>",
    "short_descriptor": "support",
    "long_descriptor": "support for developers"
  }
]
```

### Retrieve topic by id

- **URL**: v1/topic/<:id>
- **METHOD**: GET

#### Response

```json
{
  "id": "<:id>",
  "short_descriptor": "support",
  "long_descriptor": "support for developers"
}
```

### Update topic

- **URL**: v1/topic/<:id>/
- **METHOD**: PATCH

#### Request

```json
{
  "short_descriptor": "new support"
}
```

#### Response

```json
{
  "id": "<:id>",
  "short_descriptor": "new support",
  "long_descriptor": "support for developers"
}
```

### Delete topic

- **URL**: v1/topic/<:id>/
- **METHOD**: DELETE

#### Response

```json
{
  "id": "<:id>",
  "short_descriptor": "new support",
  "long_descriptor": "support for developers"
}
```

## FolderTopic

### Create folder topic

- **URL**: v1/m2m/folder/topic/
- **METHOD**: POST

#### Request

```json
{
  "folder": "<uuid>",
  "topic": "<uuid>"
}
```

#### Response

```json
{
  "id": "<uuid>",
  "folder": "<uuid>",
  "topic": "<uuid>"
}
```

### Delete folder topic

- **URL**: v1/m2m/folder/topic/<:id>
- **METHOD**: DELETE

#### Response

```json
{
  "id": "<:id>",
  "folder": "<uuid>",
  "topic": "<uuid>"
}
```

## DocumentTopic

### Create document topic

- **URL**: v1/m2m/document/topic/
- **METHOD**: POST

#### Request

```json
{
  "document": "<uuid>",
  "topic": "<uuid>"
}
```

#### Response

```json
{
  "id": "<uuid>",
  "document": "<uuid>",
  "topic": "<uuid>"
}
```

### Delete document topic

- **URL**: v1/m2m/document/topic/<:id>
- **METHOD**: DELETE

#### Response

```json
{
  "id": "<:id>",
  "document": "<uuid>",
  "topic": "<uuid>"
}
```

