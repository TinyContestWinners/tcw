# TCW: Tiny Contest Winners
A simple web app to create ephemeral contests.

## Description
Allows someone to create a contest. When the contest has expired, the winners will be randomly selected and emailed to the original contest creator. Details about entrants to a contest are removed from the database once the winners have been picked.

## Contest Entrants
The contest creator is responsible for managing the link to the contest, and distributing it to potential entrants.
There is no search function, or recovery to find the link to a contest.

## Notifications
This app does not notify the winners. The contest creator will be notified by email of the winners once the contest expires. It is the responsibility of the contest creator to notify users if they won.

## Installation
```
$> pip install tcw
```
