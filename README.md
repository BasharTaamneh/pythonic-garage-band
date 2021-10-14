# pythonic-garage-band

This python script uses Object Oriented Programming methodoliges to structure a fictional band using classes and objects to layout the structure and composition of the band and their talents.

## Lab Submission Pull Requests

[Garage Band with OOP](https://github.com/BasharTaamneh/pythonic-garage-band/pull/1)

## Requirment

```javascript
poetry
python 3.9.7
pytest
```

## Getting started

```bash
poytry install
poetry shell
pytest
python -m Modules_and_Testing.math_series
```

**Collaboratores:**

- The whole class.

## pythonic-garage-band

**Band Tests**

- [x] A Band instance should have a name attribute which is a string.
  
- [x] A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
  
- [x] A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.

- [x] A Band instance should have appropriate __str__ and __repr__ methods.

- [x] A Band should have a class method to_list which returns a list of previously created Band instances
  
**Musician Subclass Tests**

- [x] Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
  
- [x] Each kind of Musician instance should have a get_instrument method that returns string.
  
- [x] Each kind of Musician instance should have a play_solo method that returns string.
