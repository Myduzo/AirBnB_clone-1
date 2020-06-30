# AirBnB clone - The console
> The Holberton B&B.


![](header.png)

## AirBnB console

AirBnB console is so important because it is the first step to be used for the Holberton Airbnb clone. Our console can retrieve objects from a JSON.

## AirBnB console usage

This console allow us to be able to manage the objects of our project:

    * Create a new object (ex: a new User or a new Place)
    * Retrieve an object from a file, a database etc…
    * Do operations on objects (count, compute stats, etc…)
    * Update attributes of an object
    * Destroy an object


## classes

    * BaseModel
    * FileStorage
    * User
    * State
    * City
    * Amenity
    * Place
    * Review

## Commands

    * EOF: quit the console by end of file properly
    * quit: quit console
    * all: show all objects
    * help: list of available commands
    * create: create a new class instance
    * destroy: removes objects from storage
    * update: updates instances in storage

## Command Usage

EOF
```sh
EOF
```

Quit
```sh
quit
```

All
```sh
all <class name>
```

Help
```sh
help <command>
```

Create
```sh
create <class name>
```

Destroy
```sh
destroy <class name> <object id>
```

Update
```sh
update <class name> <id> <attribute name>
```

## AUTHOR

Mhamed Azouzi –
Youssef Sahli – Sahli.youssef@outlook.com
