SELECT w2.Id FROM Weather w1, Weather w2
WHERE w1.Temperature < w2.Temperature
AND DATE_ADD(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate