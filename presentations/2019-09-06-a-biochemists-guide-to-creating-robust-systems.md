
# Enterprise software development from a biochemistry professor's point of view

* If they teach it, then it's not sticking

This is not a TED talk... where I can draw clear, helpful analogies to the
biological world I have, but I have tried not to create analogies for
aesthetic appeal.

## 

One person's opinion


Do the right thing

For the right reasons

People built open source tools and communities to solve their problems, to keep their freedoms, and to help others. 

[Right reasons]

Side effect: they built kick-ass systems.


Doing the right thing is likely to result in greatest ~~growth~~ / sustainability


keyword joke slides?

    synergy
    dynamic, scalable systems
    concurrency

## Isomorphism is the key to automation

    - DNA Replicase

## Replicating code allows for speciation!

    Kaibab vs. Abert's Grand Canyon speciation
    http://cosbiology.pbworks.com/f/1268762052/13.03.GeographicIsolationMap.JPG
    Potentially breaks isomorphism

## Hard shell, soft-squishy middle

    Internally, by implicit contract (typing?)
    Externally, expect anything that can go wrong to go wrong.

## DRY

Don't repeat yourself

## DRY is the key to discovering your language's potential

## 95% of the problems you face have already been solved

Learn your standard library

## More functional > better programming

Avoid side-effects
Stop modifying your objects

Why `sorted` is usually better than `sort`

## Immutability

Code like a functional programmer

## Solve problems "late"

## Dumb messages, smart consumers

Androgen Insensitivity Syndrome (AIS)

On estimates

pay attention to how long you think a project will take, vs. how long it took

(2 to 3 times)

Why?


list.each_cons(2) { }.map

for i in list:
  list[i], list[i+1]
  if i 


    
Write code for humans, not the machine


If you are using indices in your loop in a higher level language, you are
probably doing it wrong.

## Dumb messages, smart consumers

* Different communication patterns have different implications
* 


## Putting it together

```python
if connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_IDLE:
    return "TRANSACTION_STATUS_IDLE"
elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_ACTIVE:
    return "TRANSACTION_STATUS_ACTIVE"
elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_INTRANS:
    return "TRANSACTION_STATUS_INTRANS"
elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_INERROR:
    return "TRANSACTION_STATUS_INERROR"
elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_UNKNOWN:
    return "TRANSACTION_STATUS_UNKNOWN"
else:
    return "unknown transaction status"
```

* Not DRY
* logic is mixed with data

```python
CONNECTION_STATUSES = {
    psql.extensions.TRANSACTION_STATUS_IDLE: "TRANSACTION_STATUS_IDLE"
    psql.extensions.TRANSACTION_STATUS_ACTIVE: "TRANSACTION_STATUS_ACTIVE"
    psql.extensions.TRANSACTION_STATUS_INTRANS: "TRANSACTION_STATUS_INTRANS"
    psql.extensions.TRANSACTION_STATUS_INERROR: "TRANSACTION_STATUS_INERROR"
    psql.extensions.TRANSACTION_STATUS_UNKNOWN: "TRANSACTION_STATUS_UNKNOWN"
}
return statues.get(connection.status, "unknown transaction status")
```


Choose your ecosystem wisely and use it well
    * 
    * Use idioms

## drafting coefficient

the world is a network
    choose the data structure to solve your problem

Software ~~Coding~~ Processes

Fail fast
    - tight feedback loops
    - short generation time

Your ecosystem/constraints determines your approach 

# test the behavior you care about

use good tools

## goal fewest lines of code

    Best code is code that you don't have to write or maintain

## Open source what you can

    github - 



