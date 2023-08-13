# AirBnB clone
![](aribnb.png.png)

 This project present a first step towards builduing the AirBnB web application.
 The Backend of this project is written with python.
 First we will use a command interpreter to manipulate data without a visual interface (perfect for development and debugging).
 This command line interpreter(called console) is based on  ``` cmd module ``` .

## Installation
``` $ git clone https://github.com/younessgt/AirBnB_clone.git ```

## How to Start it
``` 
$ cd AirBnB_clone
$ ./console.py
```


### Usage

#### Basic Usage of The Console
---
| **Function** | **Funcionality** | **Usage** |
| -------------- | ----------------- | ----------------- |
|create | Creates a new instance of a valid class(``` BaseModel```, ``` User```, ``` Place```, ``` City```, ``` State```, ``` Amenity```, ``` Review```). | create <class_name>
|count | Returns count of objects. | <class_name>.count() or count <class_name>
|destroy | Deletes an instance . | destroy <class_name> (<i_d>) 
|all | Prints all string representation of all instances based or not on the class name. | <class_name>.all() or all or all <class_name>
|show | Prints the string representation of an instance based on the class name and id. | <class_name>.show(<i_d>) or show <class_name> <i_d>
|update | Updates an instance based on the class name and id by adding or updating attribute. | update <class_name> <id> <attribute_name> "<attribute_value>" or <classname>.update(<i_d>, <attribute_name>, <attribute_value>) 
|EOF | Exit the console. | EOF or Ctrl+d
|quit | Exit the console. | quit
|help | Help method. | help




---
### Examples

Here are some illustrative examples showcasing the usage of the console:
  - This demonstrates how to create a BaseModel,
 utilize  show, all, destroy and update commands.
 - A similar process can be followed for the other classes as well.
Enjoy !
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update


(hbnb) create BaseModel
79de78e9-c848-4584-ba8d-27a73b3da42b
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (79de78e9-c848-4584-ba8d-27a73b3da42b) {'id': '79de78e9-c848-4584-ba8d-27a73b3da42b', 'created_at': datetime.datetime(2023, 8, 13, 13, 28, 18, 973409), 'updated_at': datetime.datetime(2023, 8, 13, 13, 28, 18, 973463)}"]
(hbnb)
(hbnb) show BaseModel
** instance id missing **
(hbnb)
(hbnb) show BaseModel 79de78e9-c848-4584-ba8d-27a73b3da42b
[BaseModel] (79de78e9-c848-4584-ba8d-27a73b3da42b) {'id': '79de78e9-c848-4584-ba8d-27a73b3da42b', 'created_at': datetime.datetime(2023, 8, 13, 13, 28, 18, 973409), 'updated_at': datetime.datetime(2023, 8, 13, 13, 28, 18, 973463)}
(hbnb)
(hbnb) destroy BaseModel 79de78e9-c848-4584-ba8d-27a73b3da42b
(hbnb)
(hbnb) show BaseModel 79de78e9-c848-4584-ba8d-27a73b3da42b
** no instance found **
(hbnb)
(hbnb) create BaseModel
130f3f19-4703-4551-aaf0-562e64eee47c
(hbnb)
(hbnb)  update BaseModel 130f3f19-4703-4551-aaf0-562e64eee47c name YOlei
(hbnb)
(hbnb) show BaseModel 130f3f19-4703-4551-aaf0-562e64eee47c
[BaseModel] (130f3f19-4703-4551-aaf0-562e64eee47c) {'id': '130f3f19-4703-4551-aaf0-562e64eee47c', 'created_at': datetime.datetime(2023, 8, 13, 13, 34, 4, 729735), 'updated_at': datetime.datetime(2023, 8, 13, 13, 38, 35, 561864), 'name': 'YOlei'}
```
### Authors
#### Youness Merzak
- Github: [younessgt](https://github.com/younessgt)

#### Leila Merzak
- Github: [leila](https://github.com/leila111111)

