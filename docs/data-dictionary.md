# Data Dictionary

## Requirements

> An API that stores "digital documents" in "folders". Folders or documents can have
> one or many associated "Topics", with short & long-form descriptors.

&ndash; Hammad (Spekit)

## v1

### Assumptions or Constraints:

- There is no mention of user roles or permissions, hence, user model is not needed.
    - No authentication features required.
- Do the digital document model include a file field or the content is stored in a text field?
    - Having the content stored in form of text field can make it easily indexable using Elastic Search.
        - Documents in PDF, DOCX etc. format would require ingestion to be indexable
    - For the sake of simplicity of the tech project, it would be more suitable to go with storing content in text
      field.
- Can a folder have multiple levels (that is, a folder inside a folder)?
    - This is a reasonable expectation of any file system to have multiple level hierarchy instead of a single flat
      level.
- What is considered the root folder?
    - All folders and documents which are not associated with a folder are considered to be in the root folder.

### Tables

From the above notes, we will have the following tables and attributes:

##### Document

| Name      | Type         | Description                                            | Properties   |
|-----------|--------------|--------------------------------------------------------|--------------|
| id        | uuid         | Primary key for Document model. Defaults to uuid4.     | pk, unique   |
| title     | text         | Title of the document. Defaults to "Untitled Document" |              |
| content   | text         | Content of the document. Defaults to blank             |              |
| folder_id | uuid         | Foreign key to Folder table.                           | fk, nullable |
| topics    | many to many | Many to many field to Topic model.                     |              |

#### Folder

| Name      | Type         | Description                                                                   | Properties   |
|-----------|--------------|-------------------------------------------------------------------------------|--------------|
| id        | uuid         | Primary key for Folder model. Defaults to uuid4.                              | pk, unique   |
| name      | text         | Name of the folder. Cannot be blank. Has to be unique with in the same level. |              |
| folder_id | uuid         | Foreign key to Folder table.                                                  | fk, nullable |
| topics    | many to many | Many to many field to Topic model.                                            | m2m          |

#### Topic

| Name             | Type         | Description                                                         | Properties |
|------------------|--------------|---------------------------------------------------------------------|------------|
| id               | uuid         | Primary key for the Topic model. Defaults to uuid4.                 | pk, unique |
| short_descriptor | char         | Short descriptor for the Topic. Max length is 255. Cannot be blank. | unique     |
| long_descriptor  | text         | Long descriptor for the Topic. Cannot be blank.                     | m2m        |

#### DocumentTopic

| Name        | Type | Description                                                 | Properties |
|-------------|------|-------------------------------------------------------------|------------|
| id          | uuid | Primary key for the DocumentTopic model. Defaults to uuid4. | pk, unique |
| topic_id    | uuid | Foreign key for Topic model.                                | fk         |
| document_id | uuid | Foreign key for Document model.                             | fk         |

#### FolderTopic

| Name      | Type | Description                                               | Properties |
|-----------|------|-----------------------------------------------------------|------------|
| id        | uuid | Primary key for the FolderTopic model. Defaults to uuid4. | pk, unique |
| topic_id  | uuid | Foreign key for Topic model.                              | fk         |
| folder_id | uuid | Foreign key for Folder model.                             | fk         |
